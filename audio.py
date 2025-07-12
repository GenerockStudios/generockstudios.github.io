import PyPDF2
from docx import Document
from gtts import gTTS
import os
from pydub import AudioSegment
# from pydub.playback import play # Décommentez si vous voulez jouer l'audio directement

# --- Fonctions d'extraction de texte (inchangées) ---
def extract_text_from_pdf(pdf_path):
    """
    Extrait le texte d'un fichier PDF.
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Erreur lors de l'extraction du texte du PDF : {e}")
    return text

def extract_text_from_docx(docx_path):
    """
    Extrait le texte d'un fichier DOCX.
    """
    text = ""
    try:
        doc = Document(docx_path)
        for para in doc.paragraphs:
            if para.text:
                text += para.text + "\n"
    except Exception as e:
        print(f"Erreur lors de l'extraction du texte du DOCX : {e}")
    return text

# --- Fonction de division du texte améliorée ---
def split_text_for_tts(text, max_chars=4900):
    """
    Divise un long texte en morceaux gérables pour gTTS,
    en privilégiant les séparations logiques (paragraphes, phrases).
    """
    text = text.replace('\r\n', '\n').replace('\r', '\n') # Normalise les sauts de ligne
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()] # Divise par paragraphes (double saut de ligne)

    if not paragraphs: # Si pas de double saut de ligne, essaie avec simple saut de ligne
        paragraphs = [p.strip() for p in text.split('\n') if p.strip()]

    chunks = []
    current_chunk = ""

    for para in paragraphs:
        # Tente d'ajouter un paragraphe entier si cela ne dépasse pas la limite
        if len(current_chunk) + len(para) + 2 < max_chars: # +2 pour le saut de ligne à ajouter
            if current_chunk:
                current_chunk += "\n\n" + para
            else:
                current_chunk = para
        else:
            # Si le paragraphe entier est trop long, on doit le diviser par phrases
            if current_chunk: # Ajoute le chunk précédent avant de traiter le nouveau paragraphe
                chunks.append(current_chunk.strip())
                current_chunk = ""

            sentences = [s.strip() for s in para.split('. ') if s.strip()] # Divise le paragraphe en phrases
            if not sentences: # Si le paragraphe n'a pas de points, traite-le comme une seule "phrase"
                sentences = [para.strip()]
                
            for sentence in sentences:
                if len(current_chunk) + len(sentence) + 2 < max_chars: # +2 pour le ". " ou le saut de ligne
                    if current_chunk:
                        current_chunk += ". " + sentence
                    else:
                        current_chunk = sentence
                else:
                    if current_chunk:
                        chunks.append(current_chunk.strip() + (". " if current_chunk.endswith('.') else "")) # Ajoute le point si la phrase s'est terminée par un point
                    current_chunk = sentence # Commence un nouveau chunk avec la phrase actuelle

    if current_chunk: # Ajoute le dernier chunk restant
        chunks.append(current_chunk.strip())
    
    # Cas de secours : si le texte est très long et n'a pas pu être divisé logiquement (ex: un très long paragraphe)
    if not chunks and len(text) > max_chars:
        print("Avertissement: Texte très long sans séparateurs logiques clairs. Division brute par caractères.")
        for i in range(0, len(text), max_chars):
            chunks.append(text[i:i+max_chars].strip())
    elif not chunks and len(text) <= max_chars: # Cas où le texte est court et n'a pas été divisé
        chunks.append(text.strip())

    return chunks

# --- Fonction de conversion audio (utilise la nouvelle fonction split_text_for_tts) ---
def convert_long_text_to_audio(text, output_audio_path="output.mp3", lang='fr'):
    """
    Convertit un long texte en un fichier audio MP3 en utilisant Google Text-to-Speech
    et en gérant la segmentation du texte.
    """
    if not text.strip():
        print("Le texte est vide, aucune conversion audio n'a été effectuée.")
        return False

    text_chunks = split_text_for_tts(text) # Utilise la fonction améliorée
    temp_audio_files = []
    
    print(f"Le texte sera divisé en {len(text_chunks)} parties pour la synthèse vocale.")

    for i, chunk in enumerate(text_chunks):
        if not chunk.strip(): # Ignore les morceaux vides
            continue
        temp_file_path = f"temp_audio_part_{i}.mp3"
        try:
            print(f"Conversion de la partie {i+1}/{len(text_chunks)}...")
            tts = gTTS(text=chunk, lang=lang, slow=False)
            tts.save(temp_file_path)
            temp_audio_files.append(temp_file_path)
        except Exception as e:
            print(f"Erreur lors de la conversion de la partie {i+1} : {e}")
            print("Veuillez vérifier votre connexion Internet ou le texte source. Tentative de nettoyage des fichiers temporaires...")
            for f in temp_audio_files:
                if os.path.exists(f):
                    os.remove(f)
            return False

    if not temp_audio_files:
        print("Aucun fichier audio temporaire n'a été généré. Le texte était peut-être trop court ou vide après nettoyage.")
        return False

    print("Concaténation des fichiers audio...")
    try:
        combined_audio = None
        for i, f_path in enumerate(temp_audio_files):
            if os.path.exists(f_path):
                segment = AudioSegment.from_mp3(f_path)
                if combined_audio is None:
                    combined_audio = segment
                else:
                    combined_audio += segment
            else:
                print(f"Avertissement: Le fichier temporaire {f_path} n'a pas été trouvé. Il pourrait y avoir un problème.")
        
        if combined_audio:
            combined_audio.export(output_audio_path, format="mp3")
            print(f"Fichier audio final créé avec succès : {output_audio_path}")
            return True
        else:
            print("Aucun segment audio à combiner. La concaténation a échoué.")
            return False
    except Exception as e:
        print(f"Erreur lors de la concaténation des fichiers audio. Assurez-vous que FFmpeg est installé et accessible dans votre PATH : {e}")
        return False
    finally:
        print("Nettoyage des fichiers temporaires...")
        for f in temp_audio_files:
            if os.path.exists(f):
                os.remove(f)

# --- Fonction principale (inchangée) ---
def main():
    """
    Fonction principale pour gérer le processus de conversion.
    """
    file_path = input("Entrez le chemin complet de votre fichier Word (.docx) ou PDF : ")

    text_content = ""
    output_filename = "audio_output.mp3"

    if file_path.lower().endswith('.pdf'):
        text_content = extract_text_from_pdf(file_path)
        output_filename = os.path.splitext(os.path.basename(file_path))[0] + ".mp3"
    elif file_path.lower().endswith('.docx'):
        text_content = extract_text_from_docx(file_path)
        output_filename = os.path.splitext(os.path.basename(file_path))[0] + ".mp3"
    else:
        print("Type de fichier non pris en charge. Veuillez fournir un fichier .docx ou .pdf.")
        return

    if text_content:
        # Nettoyage de base du texte (supprimer les espaces multiples, etc.)
        # Normalisation des sauts de ligne et suppression des lignes complètement vides
        text_content = os.linesep.join([s for s in text_content.splitlines() if s.strip()])
        # Remplace les multiples espaces par un seul, mais garde les sauts de ligne pour les paragraphes
        # Cette étape est moins agressive car split_text_for_tts gère mieux les paragraphes
        # text_content = ' '.join(text_content.split()) # L'ancienne ligne, moins adaptée si on veut garder la structure

        # Vous pouvez spécifier la langue ici ('fr' pour français, 'en' pour anglais, etc.)
        if convert_long_text_to_audio(text_content, output_filename, lang='fr'):
            print("\nProcessus terminé.")
            # Optionnel : Jouer l'audio immédiatement (nécessite 'pydub' et FFmpeg)
            # try:
            #     print("Lecture de l'audio...")
            #     audio = AudioSegment.from_mp3(output_filename)
            #     play(audio)
            # except Exception as e:
            #     print(f"Impossible de lire le fichier audio : {e}. Assurez-vous d'avoir FFmpeg installé.")
    else:
        print("Impossible d'extraire le contenu du fichier ou le contenu était vide. Veuillez vérifier le fichier.")

if __name__ == "__main__":
    main()