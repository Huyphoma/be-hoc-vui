import {useState} from 'react'

export default function CreateListing(){
  const [title,setTitle]=useState('')
  const [price,setPrice]=useState('')
  async function submit(){
    const token = localStorage.getItem('bds_token')
    const res = await fetch('/api/listings', {method:'POST', headers:{'Content-Type':'application/json','Authorization': 'Bearer '+token}, body: JSON.stringify({title,price})})
    const data = await res.json()
    alert(JSON.stringify(data))
  }
  return (<div style={{padding:20}}><h2>Create Listing</h2><input placeholder='title' value={title} onChange={e=>setTitle(e.target.value)} /><input placeholder='price' value={price} onChange={e=>setPrice(e.target.value)} /><button onClick={submit}>Create</button></div>)
}