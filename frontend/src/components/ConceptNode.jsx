import { useState } from "react";

export default function ConceptNode({ concept }) {
  const [open, setOpen] = useState(false);
  const subConcepts = concept?.sub_concepts || [];

  return (
    <div className="concept-card">
      <div className="concept-title" onClick={() => setOpen(!open)}>
        <span className="chevron">{open ? "▼" : "▶"}</span>
        <span>{concept?.label || "Concept"}</span>
        {subConcepts.length > 0 && <span className="chip">{subConcepts.length} ideas</span>}
      </div>

      {open ? (
        subConcepts.length > 0 ? (
          <ul className="sub-list">
            {subConcepts.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        ) : (
          <span className="small-label">No sub-concepts provided</span>
        )
      ) : null}
    </div>
  );
}
