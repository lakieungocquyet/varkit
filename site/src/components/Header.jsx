import { Link, useNavigate } from 'react-router';
import Dropdown_1 from './Dropdown.jsx';
import Logo from './Logo.jsx'
import { useEffect, useState, useRef } from 'react';

function Header() {
  useEffect(() => {
  fetch('http://localhost:3000/auth/me', {
    credentials: 'include'
  })
    .then(res => res.ok ? res.json() : null)
    .then(data => {
      if (data) setUser(data); // chứa avatar, username, email...
    });
}, []);
  const [authUser, setAuthUser] = useState(null);
  const [menuOpen, setMenuOpen] = useState(false);
  const menuRef = useRef(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetch('http://localhost:3000/me', { credentials: 'include' })
      .then(r => r.ok ? r.json() : null)
      .then(data => setAuthUser(data))
      .catch(() => setAuthUser(null));
  }, []);

  useEffect(() => {
    const onClickOutside = (e) => {
      if (menuRef.current && !menuRef.current.contains(e.target)) setMenuOpen(false);
    };
    document.addEventListener('mousedown', onClickOutside);
    return () => document.removeEventListener('mousedown', onClickOutside);
  }, []);

  const handleLogout = async () => {
    try {
      await fetch('http://localhost:3000/logout', {
        method: 'POST',
        credentials: 'include'
      });
    window.location.reload();
    } catch {}
    setAuthUser(null);
    setMenuOpen(false);
    navigate('/');
  };

  return (
    <div className="Header">
      <Logo></Logo>
      <nav className="nav_menu">
        <Dropdown_1></Dropdown_1>
      </nav>
      <div className="Account_actions" ref={menuRef} style={{ position: 'relative' }}>
        {authUser ? (
          <>
            <button className="User_button" onClick={() => setMenuOpen(v => !v)}>
              <img className="User_avatar"
                src={authUser.avatar || '/public/15685793.png'}
                alt={authUser.username || 'User'}
              />
            </button>
            {menuOpen && (
              <div
                style={{
                  position: 'absolute',
                  top: 40,
                  right: 0,
                  background: '#fff',
                  border: '1px solid #e5e5e5',
                  borderRadius: 8,
                  boxShadow: '0 4px 16px rgba(0,0,0,0.08)',
                  padding: 8,
                  zIndex: 1000,
                  minWidth: 160
                }}
              >
                <div style={{ padding: '8px 10px', fontSize: 13, color: '#666' }}>
                  {authUser.username || 'User'}
                </div>
                <button
                  onClick={handleLogout}
                  style={{
                    width: '100%',
                    textAlign: 'left',
                    padding: '8px 10px',
                    background: 'transparent',
                    border: 'none',
                    cursor: 'pointer'
                  }}
                >
                  Log out
                </button>
              </div>
            )}
          </>
        ) : (
          <>
            <button  className="Sign_up" onClick={() => navigate("/signup")}>
              Sign up
            </button>
            <button className="Log_in" onClick={() => navigate("/login")}>
                Log in
            </button>
          </>
        )}
      </div>
    </div>
  );
}

export default Header;