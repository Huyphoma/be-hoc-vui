import { useState } from 'react'

export default function Login(){
  const [phone, setPhone] = useState('')
  const [token, setToken] = useState('')
  async function doLogin(){
    const res = await fetch('/api/auth/login', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({phone})})
    const data = await res.json()
    if(data.access_token){
      localStorage.setItem('bds_token', data.access_token)
      setToken(data.access_token)
      alert('Logged in')
    } else {
      alert('Login failed')
    }
  }
  return (
    <div style={{padding:20}}>
      <h2>Login (demo)</h2>
      <input placeholder="phone" value={phone} onChange={e=>setPhone(e.target.value)} />
      <button onClick={doLogin}>Login (stub)</button>
      <pre>{token}</pre>
    </div>
  )
}