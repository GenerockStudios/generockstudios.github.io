import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.scss'
import { globalPaths } from './global/paths'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'


const router = createBrowserRouter(globalPaths, {
  basename: import.meta.env.BASE_URL 
});

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router}></RouterProvider>
  </React.StrictMode>,
)
