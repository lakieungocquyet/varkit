import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router'
import App from './views/App.jsx'


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <BrowserRouter basename={"/varkit/"}>
        <App />
      </BrowserRouter>
  </React.StrictMode>,
)
