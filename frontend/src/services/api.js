const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function uploadFile(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE_URL}/api/summarize`, {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || "Upload failed");
  }

  return response.json();
}
