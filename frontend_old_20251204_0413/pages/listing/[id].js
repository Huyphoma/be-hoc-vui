import {useRouter} from 'next/router'
import useSWR from 'swr'
const fetcher = (url) => fetch(url).then(r=>r.json())

export default function ListingDetail(){
  const router = useRouter()
  const {id} = router.query
  const {data} = useSWR(id ? `/api/listings/${id}` : null, fetcher)
  if(!data) return <div>Loading...</div>
  return <div style={{padding:20}}><h2>{data.title}</h2><div>{data.description}</div><div>Images: {JSON.stringify(data.images)}</div></div>
}