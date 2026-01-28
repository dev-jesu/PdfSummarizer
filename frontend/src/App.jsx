import { useState } from "react";
import UploadForm from "./components/UploadForm";
import MindMap from "./components/MindMap.jsx";
import "./App.css";
import "./styles/mindmap.css";

function App() {
  const [summary, setSummary] = useState(null);

  return (
    <div className="page">
      <header className="hero">
        <span className="badge">Gemini powered</span>
        <h1>Transform any PDF or TXT into a living mind map</h1>
        <p>
          Upload a document and the backend will distill it into key ideas,
          then render an interactive, elegant mind map for quick comprehension.
        </p>
        <div className="motto-row">
          <span className="motto-chip">Learn faster</span>
          <span className="motto-chip">See the structure</span>
          <span className="motto-chip">Remember more</span>
          <span className="motto-chip">Share clarity</span>
        </div>
      </header>

      <div className="cards">
        <div className="card">
          <h3>Upload a document</h3>
          <p className="subtext">
            Supported formats: PDF and TXT. We keep the backend untouched—just
            a refined UI to visualize your summaries.
          </p>
          <UploadForm onSuccess={setSummary} />
        </div>

        <div className="card">
          <h3>Tips for best maps</h3>
          <ul className="tips">
            <li>Prefer concise source docs for cleaner concept clusters.</li>
            <li>Group related topics in one file to see stronger links.</li>
            <li>Re-run uploads after edits to see the map update instantly.</li>
            <li>PDF tables are supported via backend extraction—no changes here.</li>
          </ul>
        </div>
      </div>

      <section className="mindmap-section">
        <div className="section-header">
          <h2>Mind Map</h2>
          <span className="pill">{summary ? "Ready" : "Awaiting upload"}</span>
        </div>

        {summary ? (
          <MindMap summary={summary} />
        ) : (
          <div className="empty-state">
            <strong>No map yet.</strong> Upload a PDF or TXT to generate an
            interactive map of the core ideas, branches, and subtopics.
          </div>
        )}
      </section>
    </div>
  );
}

export default App;
