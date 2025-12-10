export default async function handler(req, res) {
  const r = await fetch(process.env.BACKEND_URL + '/auth/login', {method: 'POST', headers:{'Content-Type':'application/json'}, body: req.body});
  const data = await r.json();
  res.status(200).json(data);
}