const backendUrl = process.env.BACKEND_URL || "http://149.28.142.220:8000";

export async function apiGet(path) {
    const res = await fetch(backendUrl + path);
    if (!res.ok) {
        throw new Error("Request failed: " + res.status);
    }
    return res.json();
}
