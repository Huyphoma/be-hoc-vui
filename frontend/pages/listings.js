import useSWR from 'swr'
const fetcher = (url) => fetch(url).then(r=>r.json())

export default function Listings(){
  const {data} = useSWR('/api/listings', fetcher)
  return (
    <div style={{padding: 20}}>
      <h2>Listings (stub)</h2>
      <a href="/create_listing">Create new listing</a>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  )
}