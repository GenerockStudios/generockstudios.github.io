import { RouteObject } from "react-router-dom";

export const createLazyRoute = (route: string,
     pathImport: string,
     nameComponent : string,
     children: RouteObject[]) : RouteObject => {
    const routeObject : RouteObject = 
    {
      path: route,
      async lazy() {
         
        const components = await import(/* @vite-ignore */pathImport);
        return { Component: components[nameComponent] };
      },
      children: children
    } 
    return routeObject
}