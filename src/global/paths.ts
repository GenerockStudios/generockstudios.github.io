import { RouteObject } from "react-router-dom";
import { createLazyRoute } from "../routes/globalPaths.ts";


//const homeRoute = createLazyRoute("/", "/src/views/portfolio/landing/home.tsx", "Home", [])
const TextEditorRoute = createLazyRoute("/text-editor", "../library/components/TextEditor/TextEditor.tsx", "TextEditor", [])


export const globalPaths: RouteObject[] = [
    {
      path: "/",
      async lazy() {
         
        const components = await import("../views/portfolio/landing/home.tsx");
        return { Component: components["Home"] };
      },
      children: []
    },
    //homeRoute,
    TextEditorRoute
]
