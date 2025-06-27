import "../styles/home.scss";

export const Skills = () => {
  return (
    <>
      <div className="title-center">
        <h1>Mes compétences</h1>
      </div>

      <div className="main-techno-container">
        <div className="techno-container">
          <img src="images/svg/csharp.svg" alt="Github" />
          <h2>C#</h2>
        </div>
        <div className="techno-container">
          <img src="images/svg/javascript.svg" alt="JavaScript" />
          <h2>JavaScript</h2>
        </div>
        <div className="techno-container">
          <img src="images/svg/github.svg" alt="ASP.NET" />
          <h2>ASP.NET</h2>
        </div>
        <div className="techno-container">
          <img src="images/svg/react.svg" alt="React" />
          <h2>React</h2>
        </div>
        <div className="techno-container">
          <img src="images/svg/css.svg" alt="CSS" />
          <h2>CSS</h2>
        </div>
        <div className="techno-container">
          <img src="images/svg/github.svg" alt="CSS" />
          <h2>Git & Github</h2>
        </div>
        <div className="techno-container">
          <img src="images/svg/typescript.svg" alt="TypeScript" />
          <h2>TypeScript</h2>
        </div>
        <div className="techno-container">
          <img src="images/svg/database.svg" alt="CSS" />
          <h2>MSSQL server & Postgres SQL</h2>
        </div>
      </div>
    </>
  );
};

export const Projects = () => {
  return (
    <div className="main-projects" id="Projects">
      <div className="title-center">
        <h1>Mes projets</h1>
      </div>
      <div className="header-developper-presentation-container">
        <div className="box">
          <span></span>
          <div className="content"></div>
        </div>
      </div>
    </div>
  );
};

export const Contact = () => {
  return (
    <div className="main-contact" id="Contact">
      <div className="title-center">
        <h1>Contactez moi</h1>
      </div>

      <div className="main-techno-container">
        <a href="https://wa.me/237671194872" className="techno-container">
          <img src="images/svg/whatsapp.svg" alt="Whatsapp" />
          <h2>Whatsapp</h2>
        </a>
        <a href="https://linkedin.com/in/jean-eric-tsala-ntonga/" className="techno-container">
          <img src="images/svg/linkedin.svg" alt="LinkedIn" />
          <h2>LinkedIn</h2>
        </a>
        <div className="techno-container">
          <img src="images/svg/gmail.svg" alt="Email" />
          <h2>generockstudios@gmail.com</h2>
        </div>
        <div className="techno-container">
          <img src="images/svg/phone.svg" alt="Phone number" />
          <h2>+237 696 81 82 82</h2>
        </div>
      </div>
    </div>
  );
};

export const Main = () => {
  return (
    <main className="app-main-container mg-top-2">
      <Skills></Skills>
      <Projects></Projects>
      <Contact></Contact>
    </main>
  );
};
