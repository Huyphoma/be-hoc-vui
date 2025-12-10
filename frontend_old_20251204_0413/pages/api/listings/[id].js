export default async function handler(req, res){
  const id = req.query.id
  const r = await fetch(process.env.BACKEND_URL + '/listings/' + id)
  const data = await r.json()
  res.status(200).json(data)
}