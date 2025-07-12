import "../styles/home.scss";

export const Header = () => {
  return (
    <div className="header-home-header">
      <div className="header-logo-navbar-container">
        <div className="header-logo-container">
          <img
            src="images/generockstudioswithoutbg.png"
            alt="Generock Studio - Logo"
            className="m-2 w-[45px] h-[45px]"
          />
        </div>

        <nav className="header-navbar-container">
          <ul className="header-nav-link">
            <li>
              <a href="#">Home</a>
            </li>
            <li>
              <a href="#Projects">Projects</a>
            </li>
            <li>
              <a href="#Contact">Contact</a>
            </li>
            <li>
              <div className="languages-toggle-container">
                <select name="languages" id="" className="languages-toggle">
                  <option value="English">English</option>
                  <option value="French">French</option>
                </select>
              </div>
            </li>
          </ul>

          <div className="utils-social-container">
            <div className="socials-media-container">
              <ul className="social-media-list">
                <li>
                  <a href="https://github.com/GenerockStudios">
                    <img src="images/svg/github.svg" alt="Github" />
                  </a>
                </li>
                <li>
                  <a href="https://wa.me/237671194872">
                    <img src="images/svg/whatsapp.svg" alt="Whatsapp" />
                  </a>
                </li>
                <li>
                  <a href="https://linkedin.com/in/jean-eric-tsala-ntonga/">
                    <img src="images/svg/linkedin.svg" alt="LinkedIn" />
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>

      <div className="header-developper-presentation-container">
        <div className="box">
          <span></span>
          <div className="content">
            <div className="developper-presentation-image-container">
              <img
                src="images/portfolio/mypicture-removebg-preview.png"
                alt="TSALA NTONGA JEAN ERIC - Erock - Generock Studios"
              />
            </div>
            <div className="developper-presentation-description-container">
              <h1 className="developper-name">TSALA NTONGA JEAN ERIC</h1>
              <h2 className="developper-function">Backend Developper .NET</h2>
              <p>
                En tant que développeur Backend .NET passionné par le
                développement web, je me spécialise dans la création de
                solutions robustes et performantes. Mon expertise s'articule
                autour de C# et ASP.NET Core, me permettant de concevoir des API
                solides et des architectures backend efficaces.
                <br />
                Mon profil est complété par de solides compétences en React.js,
                ce qui me permet d'appréhender le développement web de manière
                holistique, du backend à l'interface utilisateur.
                <br />
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
