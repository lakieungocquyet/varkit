import { Link, useLocation } from "react-router";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router";
import Logo from "../components/Logo.jsx";

function Complete_profile() {
  	const navigate = useNavigate();
    const location = useLocation();
    const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [username, setUsername] = useState("");
	const [errors, setErrors] = useState({});
	const [passwordVisible, setPasswordVisible] = useState(false);
  	const [confirmPasswordVisible, setConfirmPasswordVisible] = useState(false);

    useEffect(() => {
        if (location.state?.email) { setEmail(location.state.email); }
		if (location.state?.type) console.log("Email type:", location.state.type);
    }, [location.state]);

    useEffect(() => {
		const params = new URLSearchParams(location.search);
		const emailParam = params.get("email");
		const usernameParam = params.get("username");

		if (emailParam) setEmail(emailParam);
		if (usernameParam) setUsername(usernameParam);
  	}, [location.search]);

	const handleCreateAccount = async () => {
    	const newErrors = {};

		if (!password.trim()) {
		newErrors.password = (
			<>
				<svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#EA3323">
					<path d="M480-96q-16 0-28-5t-23-16L117-429q-11-11-16-23t-5-28q0-16 5-28t15.7-22.7L429-843q11-11 23-16t28-5q16 0 28 5t23 16l312 312q11 11 16 23t5 28q0 16-5 28t-16 23L530.7-116.7Q520-106 508-101t-28 5Zm0-72 312-312-312-312-312 312 312 312Zm-36-288h72v-216h-72v216Zm35.79 120q15.21 0 25.71-10.29t10.5-25.5q0-15.21-10.29-25.71t-25.5-10.5q-15.21 0-25.71 10.29t-10.5 25.5q0 15.21 10.29 25.71t25.5 10.5Zm.21-144Z"/>
				</svg>
				{" "}
				Password is required.
			</>
		);
		}

		if (!confirmPassword.trim()) {
		newErrors.confirmPassword = (
			<>
				<svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#EA3323">
					<path d="M480-96q-16 0-28-5t-23-16L117-429q-11-11-16-23t-5-28q0-16 5-28t15.7-22.7L429-843q11-11 23-16t28-5q16 0 28 5t23 16l312 312q11 11 16 23t5 28q0 16-5 28t-16 23L530.7-116.7Q520-106 508-101t-28 5Zm0-72 312-312-312-312-312 312 312 312Zm-36-288h72v-216h-72v216Zm35.79 120q15.21 0 25.71-10.29t10.5-25.5q0-15.21-10.29-25.71t-25.5-10.5q-15.21 0-25.71 10.29t-10.5 25.5q0 15.21 10.29 25.71t25.5 10.5Zm.21-144Z"/>
				</svg>
				{" "}
				Please confirm your password.
			</>
		);
		} else if (confirmPassword !== password) {
		newErrors.confirmPassword = (
			<>
				<svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#EA3323">
					<path d="M480-96q-16 0-28-5t-23-16L117-429q-11-11-16-23t-5-28q0-16 5-28t15.7-22.7L429-843q11-11 23-16t28-5q16 0 28 5t23 16l312 312q11 11 16 23t5 28q0 16-5 28t-16 23L530.7-116.7Q520-106 508-101t-28 5Zm0-72 312-312-312-312-312 312 312 312Zm-36-288h72v-216h-72v216Zm35.79 120q15.21 0 25.71-10.29t10.5-25.5q0-15.21-10.29-25.71t-25.5-10.5q-15.21 0-25.71 10.29t-10.5 25.5q0 15.21 10.29 25.71t25.5 10.5Zm.21-144Z"/>
				</svg>
				{" "}
				Passwords do not match.
			</>
		);
		}

		if (!username.trim()) {
		newErrors.username = (
			<>
				<svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#EA3323">
					<path d="M480-96q-16 0-28-5t-23-16L117-429q-11-11-16-23t-5-28q0-16 5-28t15.7-22.7L429-843q11-11 23-16t28-5q16 0 28 5t23 16l312 312q11 11 16 23t5 28q0 16-5 28t-16 23L530.7-116.7Q520-106 508-101t-28 5Zm0-72 312-312-312-312-312 312 312 312Zm-36-288h72v-216h-72v216Zm35.79 120q15.21 0 25.71-10.29t10.5-25.5q0-15.21-10.29-25.71t-25.5-10.5q-15.21 0-25.71 10.29t-10.5 25.5q0 15.21 10.29 25.71t25.5 10.5Zm.21-144Z"/>
				</svg>
				{" "}
				Username is required.
			</>
		);
    }

    setErrors(newErrors);

    if (Object.keys(newErrors).length === 0) {
      	console.log("Submit form:", { email, password, confirmPassword, username });
      
      	try {
      		const response = await fetch("http://localhost:3000/register", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
        	},
			body: JSON.stringify({
				email,
				password,
				username,
				type: location.state?.type || "MANUAL"
			}),
		});

      const data = await response.json();

      if (response.ok) {
        alert("Tạo tài khoản thành công!");
        console.log("Server response:", data);
        navigate("/login", { state: { email } });
      } else {
        alert(data.message || "Đăng ký thất bại, vui lòng thử lại.");
        console.error("Error from server:", data);
      }
    } catch (error) {
      console.error("Request error:", error);
      alert("Không thể kết nối tới server. Kiểm tra lại backend.");
    }
    }
  };
  return (
    <div className="Complete_profile">
    <div className="Complete_profile_frame">
        <Logo/>
        <span className="Complete_profile_title">
            Complete your profile
        </span>
		<div className="Complete_profile_form">
			<span>Email adress</span>
			<input type='text' value={email} disabled/>
			<span>Password</span>
			<div className="Password_wrapper">
          <input type={passwordVisible ? "text" : "password"} placeholder="Enter password" onChange={(e) => setPassword(e.target.value)} className={errors.password ? "input-error" : ""}/>
          <button className="Set_password_visible" onClick={() => setPasswordVisible(!passwordVisible)}>
            {passwordVisible ? 
			(<svg xmlns="http://www.w3.org/2000/svg" height="18px" viewBox="0 -960 960 960" width="18px" fill="#555555ff">
				<path d="m644-428-58-58q9-47-27-88t-93-32l-58-58q17-8 34.5-12t37.5-4q75 0 127.5 52.5T660-500q0 20-4 37.5T644-428Zm128 126-58-56q38-29 67.5-63.5T832-500q-50-101-143.5-160.5T480-720q-29 0-57 4t-55 12l-62-62q41-17 84-25.5t90-8.5q151 0 269 83.5T920-500q-23 59-60.5 109.5T772-302Zm20 246L624-222q-35 11-70.5 16.5T480-200q-151 0-269-83.5T40-500q21-53 53-98.5t73-81.5L56-792l56-56 736 736-56 56ZM222-624q-29 26-53 57t-41 67q50 101 143.5 160.5T480-280q20 0 39-2.5t39-5.5l-36-38q-11 3-21 4.5t-21 1.5q-75 0-127.5-52.5T300-500q0-11 1.5-21t4.5-21l-84-82Zm319 93Zm-151 75Z"/>
			</svg>) : 
			(<svg xmlns="http://www.w3.org/2000/svg" height="18px" viewBox="0 -960 960 960" width="18px" fill="#555555ff">
				<path d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Zm0-300Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z"/>
			</svg>)}
          </button>
		  </div>
		  {errors.password && <span className="error-text">{errors.password}</span>}			
		  <span>Confirm Password</span>
			<div className="Confirm_password_wrapper">
          <input type={confirmPasswordVisible ? "text" : "password"} placeholder="Enter password" onChange={(e) => setConfirmPassword(e.target.value)} className={errors.confirmPassword ? "input-error" : ""}/>
          <button className="Set_confirm_password_visible" onClick={() => setConfirmPasswordVisible(!confirmPasswordVisible)}>
            {confirmPasswordVisible ? 
			(<svg xmlns="http://www.w3.org/2000/svg" height="18px" viewBox="0 -960 960 960" width="18px" fill="#555555ff">
				<path d="m644-428-58-58q9-47-27-88t-93-32l-58-58q17-8 34.5-12t37.5-4q75 0 127.5 52.5T660-500q0 20-4 37.5T644-428Zm128 126-58-56q38-29 67.5-63.5T832-500q-50-101-143.5-160.5T480-720q-29 0-57 4t-55 12l-62-62q41-17 84-25.5t90-8.5q151 0 269 83.5T920-500q-23 59-60.5 109.5T772-302Zm20 246L624-222q-35 11-70.5 16.5T480-200q-151 0-269-83.5T40-500q21-53 53-98.5t73-81.5L56-792l56-56 736 736-56 56ZM222-624q-29 26-53 57t-41 67q50 101 143.5 160.5T480-280q20 0 39-2.5t39-5.5l-36-38q-11 3-21 4.5t-21 1.5q-75 0-127.5-52.5T300-500q0-11 1.5-21t4.5-21l-84-82Zm319 93Zm-151 75Z"/>
			</svg>) : 
			(<svg xmlns="http://www.w3.org/2000/svg" height="18px" viewBox="0 -960 960 960" width="18px" fill="#555555ff">
				<path d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Zm0-300Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z"/>
			</svg>)}
          </button>
		  </div>
		  {errors.confirmPassword && <span className="error-text">{errors.confirmPassword}</span>}
			<span>Username</span>
			<input type='text' value={username} onChange={(e) => setUsername(e.target.value)} className={errors.username ? "input-error" : ""}/>
			{errors.username && <span className="error-text">{errors.username}</span>}
			<button className="Create_account_button" onClick={handleCreateAccount}>Create an account</button>
		</div>
    </div>
    </div>
  );
}

export default Complete_profile;



  