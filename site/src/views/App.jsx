import { Routes, Route } from 'react-router'
import React, { useState, useEffect } from 'react'
import Home from '../pages/Home.jsx'
import Login from '../pages/Log_in.jsx'
import Sign_up from '../pages/Sign_up.jsx'
import Complete_profile from '../pages/Complete_profile.jsx'
import '../styles/App.scss'
import '../styles/Login_page.scss'
import '../styles/Signup_page.scss'
import '../styles/Complete_profile.scss'
function App() {
    const [size, setSize] = useState({ width: 0, height: 0 })

  useEffect(() => {
    const appElement = document.querySelector('.App')

    const updateSize = () => {
      if (appElement) {
        setSize({
          width: appElement.offsetWidth,
          height: appElement.offsetHeight
        })
      }
    }
    // Lần đầu đo
    updateSize()
    // Lắng nghe thay đổi kích thước cửa sổ
    window.addEventListener('resize', updateSize)
    return () => {
      window.removeEventListener('resize', updateSize)
    }
  }, [])
  useEffect(() => {
    console.log(`📏 App size: ${size.width}x${size.height}`)
  }, [size])
  return (
      <div className="App">
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/login" element={<Login/>}/>
          <Route path="/signup" element={<Sign_up/>}/>
          <Route path="/complete-profile" element={<Complete_profile/>}/>
        </Routes>
      </div>
  )
}

export default App
