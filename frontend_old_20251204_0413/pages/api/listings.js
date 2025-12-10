export default async function handler(req, res) {
  const r = await fetch(process.env.BACKEND_URL + '/listings');
  const data = await r.json();
  res.status(200).json(data);
}