# PDF Summarizer

A small full-stack application that extracts text from uploaded PDFs/TXT files, uses a generative LLM (Gemini) to derive concepts and build a summarized/mindmap-style output. The repository contains a FastAPI backend and a Vite + React frontend.

---

## Repository layout

- `backend/` - FastAPI application
  - `app/` - application package
    - `routers/` - API routes (see `/api/summarize`, `/db-test`, root)
    - `services/` - PDF/TXT readers and summarization logic (calls Gemini)
    - `core/config.py` - loads environment variables (GEMINI_API_KEY)
  - `requirements.txt` - Python dependencies
  - `.env` - environment file used locally (do not commit secrets)

- `frontend/` - Vite + React frontend
  - `package.json` - frontend scripts and dependencies

---

## Prerequisites

- Python 3.11+ (or supported Python version on your system)
- Node.js (16+/18+ recommended) and npm
- A Gemini (or compatible) API key if you want the summarization to call the remote generative model

---

## Backend — quick start (Windows PowerShell)

1. Open a PowerShell terminal and change directory to the backend folder:

```powershell
cd c:\Users\jesua\OneDrive\Desktop\pdf_summarizer\backend
```

2. Create and activate a virtual environment (if not already created), upgrade pip, and install dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Configure environment variables.

- The backend reads `GEMINI_API_KEY` from `backend/.env` or from your shell environment. Example `.env` (local only — do not commit your real key):

```
GEMINI_API_KEY=your_real_api_key_here
```

Note: The repository may contain a placeholder or redacted `.env`. Replace the placeholder with your key locally, or set the environment variable in your shell.

4. Run the FastAPI server with uvicorn:

```powershell
# from backend/ with the venv activated
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

This starts the backend at http://127.0.0.1:8000. The open API docs are available at `http://127.0.0.1:8000/docs`.

### Important endpoints

- `GET /` — simple health/heartbeat returning `{ "status": "Backend running" }`.
- `POST /api/summarize` — upload a `pdf` or `txt` file as multipart/form-data. Returns `{ status, file_name, summary }`.
  - Supported file types: `.pdf`, `.txt`.
  - Example curl (from a shell that supports curl):

```bash
curl -F "file=@/path/to/file.pdf" http://127.0.0.1:8000/api/summarize
```

- `GET /db-test` — quick DB test route (connects to DB via `app.database.get_db_connection()`), returns a simple result. Useful if your project uses a local DB.


---

## Frontend — quick start

1. Change directory to the frontend folder and install dependencies:

```powershell
cd c:\Users\jesua\OneDrive\Desktop\pdf_summarizer\frontend
npm install
```

2. Start the dev server:

```powershell
npm run dev
```

By default Vite serves on `http://localhost:5173`. The backend allows CORS for `http://localhost:5173` (see `backend/app/main.py`).

---

## Development notes

- The backend uses the Gemini generative API via the `google-generativeai` package (see `backend/requirements.txt`). Ensure your API key has the proper permissions and usage quotas.

- Sensitive information (API keys) must remain local. Do not commit real keys to the repo. The project includes `.gitignore` to avoid committing virtualenvs, build artifacts, and editor files.

- I removed debug prints that accidentally exposed the API key in `app/core/config.py`. If you need to debug environment values, use logging at an appropriate level and avoid printing secrets.

- The summarizer route will raise HTTP 400 if no file is uploaded, the file type is unsupported, or the file contains no readable text.

---

## Troubleshooting

- If you get import errors, ensure the virtual environment is activated and `pip install -r requirements.txt` completed successfully.
- If the frontend cannot reach the backend, check the backend is running and that CORS is configured for `http://localhost:5173`.
- If API calls to Gemini fail, verify `GEMINI_API_KEY` is set and network access is available.

---

## Contact / Next steps

If you want, I can:
- Add a small `.env.example` with the expected variables and instructions.
- Add a script to automate backend setup (venv + pip install).
- Add a simple smoke-test script for the summarize endpoint.

