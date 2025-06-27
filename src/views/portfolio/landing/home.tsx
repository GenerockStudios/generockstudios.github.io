import { Header } from "./header";
import { Main } from "./Main";
import { Footer } from "./footer";
import "../styles/home.scss";

export const Home = () => {
    return (
        <div className="app-home">
            <Header></Header>
            <Main></Main>
            <Footer></Footer>
        </div>
    )
}