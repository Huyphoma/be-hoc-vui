export default async function handler(req, res){
  const r = await fetch(process.env.BACKEND_URL + '/listings', {method: req.method, headers: {'Content-Type':'application/json'}, body: req.method === 'POST' ? req.body : undefined})
  const data = await r.json()
  res.status(200).json(data)
}