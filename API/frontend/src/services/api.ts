const BASE_URL = "http://localhost:8000/api";

async function request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const response = await fetch(`${BASE_URL}${endpoint}`, {
    headers: {
      "Content-Type": "application/json",
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`Erro na requisição: ${response.statusText}`);
  }

  return response.json();
}

export default request;
