import { Header } from "./header";
import { Main } from "./Main";
import { Footer } from "./footer";
import "../styles/home.scss";

export const Home = () => {
  return (
    <div className="app-home space-background">
      {/*// 
    //     <div className="bg-blue-600 h-[3px] w-[50vw] fixed z-50 top-0 left-0 right-0"></div>

    //   <div className="overflow-hidden  bg-red-500">
    //   </div>
    */}
      <Header></Header>
      <Main></Main>
      <Footer></Footer>
    </div>
  );
};
