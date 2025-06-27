import { RouteObject } from "react-router-dom";
import { createLazyRoute } from "../routes/globalPaths.ts";


const homeRoute = createLazyRoute("/", "../views/portfolio/landing/home.tsx", "Home", [])
const TextEditorRoute = createLazyRoute("/text-editor", "../library/components/TextEditor/TextEditor.tsx", "TextEditor", [])


export const globalPaths: RouteObject[] = [
    homeRoute,
    TextEditorRoute
]
