import Logo from "../components/Logo.jsx";
import { useState } from "react";
import { useNavigate } from "react-router";
function Sign_up () {
const [email, setEmail] = useState("");
  	const navigate = useNavigate();

	const detectEmailType = (email) => {
		const domain = email.split("@")[1]?.toLowerCase();
		if (!domain) return "UNKNOWN";

		if (domain.includes("gmail.com")) return "GOOGLE";
		if (domain.includes("yahoo.com")) return "YAHOO";
		if (domain.includes("outlook.com") || domain.includes("hotmail.com")) return "MICROSOFT";
		if (domain.includes("edu")) return "EDU";
		if (domain.includes("bio")) return "BIO_ORG";
		return "OTHER";
 	};
  	const handleCreateAccount = async () => {
		if (!email) {
			alert("Please enter your email");
			return;
		}
		try {
			const res = await fetch("http://localhost:3000/auth/check-email", {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify({ email }),
			});
			const data = await res.json();
			const type = detectEmailType(email);
			if (data.exists) {
				navigate("/login", { state: { email } });
			} else {
				navigate("/complete-profile", { state: { email, type } });
			}
		} catch (err) {
			console.error(err);
			alert("Error checking email");
		}
  	};
    const handleGoogleLogin = () => {
        window.location.href = "http://localhost:3000/auth/google";
    };
    return (
        <>
            <div className="Signup_page">
                <div className="Signup_frame">
                    <Logo/>
                    <span className="Signup_title">
                        Sign up to Bio solution
                    </span>
                    <div className="Signup_form">
                        <span>Email adress</span>
                        <input type='text'
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}/>
                        <button onClick={handleCreateAccount}>Create an account</button>
                    </div>
                    <div className="Signup_separator"><span>or</span></div>
                    <button onClick={handleGoogleLogin}>
                        <svg aria-hidden="true" focusable="false" width="18" height="18" viewBox="0 0 533.5 544.3">
                            <path fill="#4285f4" d="M533.5 278.4c0-18.7-1.7-37.1-5-54.8H272v103.7h147c-6.3 34.1-25.3 63-54 82.3v68h87.2c51.1-47 81.3-116.3 81.3-199.2z"/>
                            <path fill="#34a853" d="M272 544.3c73.4 0 135-24.3 180-66.1l-87.2-68c-24.2 16.3-55.2 26-92.8 26-71.4 0-131.9-48.2-153.6-113.2H28v70.9c45.2 89.6 138.9 150.4 244 150.4z"/>
                            <path fill="#fbbc05" d="M118.4 323c-10.8-32.3-10.8-67.4 0-99.7V152.4H28c-43.4 86.8-43.4 189.6 0 276.4z"/>
                            <path fill="#ea4335" d="M272 106.5c39.9-.6 78.2 14.7 107.3 42.9l80-80C410.8 24.2 344.8-.1 272 0 166.9 0 73.2 60.8 28 150.4l90.4 70.9C140.1 154.3 200.6 106.5 272 106.5z"/>
                        </svg>
                        <span>Continue with Google</span>
                    </button>
                </div>
            </div>
        </>
    )
}
export default Sign_up;