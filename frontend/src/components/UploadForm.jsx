import { useState } from "react";
import { uploadFile } from "../services/api";

export default function UploadForm({ onSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    try {
      setLoading(true);
      setError("");
      const result = await uploadFile(file);
      onSuccess(result.summary);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="upload-form">
      <div>
        <label className="subtext">Choose a PDF or TXT file</label>
        <input
          className="file-input"
          type="file"
          accept=".pdf,.txt"
          onChange={(e) => setFile(e.target.files[0])}
        />
        {file && <span className="small-label">Selected: {file.name}</span>}
      </div>

      <button className="primary-btn" type="submit" disabled={loading}>
        {loading ? "Processing with Gemini…" : "Upload & visualize"}
      </button>

      <div className="form-footer">
        {error ? (
          <span className="error-text">{error}</span>
        ) : (
          <span>We call the existing backend—no integration changes.</span>
        )}
      </div>
    </form>
  );
}
