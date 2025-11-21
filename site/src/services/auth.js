export async function loginWithGoogle(idToken) {
  const res = await fetch("http://localhost:8000/auth/google", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ idToken }),
  });
  if (!res.ok) {
    const msg = await res.text().catch(() => '');
    throw new Error(msg || 'Google login failed');
  }
  return res.json();
}