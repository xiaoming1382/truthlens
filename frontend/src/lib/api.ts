const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";

export async function detectContent(contentType: string, content: string): Promise<any> {
  const res = await fetch(`${API_BASE}/detect`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ content_type: contentType, content }),
  });
  if (!res.ok) throw new Error("Detection failed");
  return res.json();
}

export async function getSignals(category?: string, limit = 20): Promise<any> {
  const params = new URLSearchParams({ limit: String(limit) });
  if (category) params.set("category", category);
  const res = await fetch(`${API_BASE}/signals?${params}`);
  return res.json();
}

export async function getTopSignals(sinceHours = 1, limit = 10): Promise<any> {
  const res = await fetch(`${API_BASE}/signals/top?since_hours=${sinceHours}&limit=${limit}`);
  return res.json();
}

export async function getMiners(): Promise<any> {
  const res = await fetch(`${API_BASE}/miners`);
  return res.json();
}

export async function getHealth(): Promise<any> {
  const res = await fetch(`${API_BASE}/health`);
  return res.json();
}

export async function getCategories(): Promise<any> {
  const res = await fetch(`${API_BASE}/categories`);
  return res.json();
}