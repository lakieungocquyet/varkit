import { Link, useLocation } from "react-router";
import { useState, useEffect } from "react";
import Logo from "../components/Logo.jsx";

function Log_in () {
  const location = useLocation();
  const [email, setEmail] = useState("");

  useEffect(() => {
    if (location.state?.email) {
      setEmail(location.state.email);
    }
  }, [location.state]);

    const handleLogin = async () => {
  if (!email) return alert("Please enter email");
  const password = document.querySelector("input[type='text']")?.value; // hoặc thêm state cho password

  try {
    const res = await fetch("http://localhost:3000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include", // để cookie refreshToken gửi đi
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    if (!res.ok) return alert(data.message);

    // lưu access token vào localStorage
    localStorage.setItem("accessToken", data.accessToken);
    localStorage.setItem("user", JSON.stringify(data.user));

    // redirect về dashboard
    window.location.href = `/dashboard/${data.user.id}`;
  } catch (err) {
    console.error(err);
    alert("Login failed");
  }
};

    return(        
            <div className="Login_page">
                <div className="Login_frame">
                    <Logo/>
                    <span className="Login_title">
                        Log in to Bio solution
                    </span>
                    <div className="Login_form">
                        <span>Email adress</span>
                        <input type='text' value={email}  onChange={(e) => setEmail(e.target.value)}/>
                        <span>Password</span>
                        <input type='text'/>
                        <button onClick={handleLogin}>Log in</button>
                    </div>
                    <span>
                        Want to create an account?
                        {'  '}
                        <Link to="/signup" className="Sign_up">
                            Create an account
                        </Link>
                    </span> 
                </div>                
            </div>
    )
}
export default Log_in;