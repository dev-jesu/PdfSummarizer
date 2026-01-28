import ConceptNode from "./ConceptNode";

export default function MindMap({ summary }) {
  const concepts = summary?.concepts || [];

  return (
    <div className="mindmap-wrapper">
      <div className="central-node">
        <span className="chip">Root topic</span>
        <div className="central-title">{summary?.main_topic || "Mind map"}</div>
        <span className="small-label">Click nodes to expand details</span>
      </div>

      <div className="mindmap-grid">
        {concepts.map((concept, index) => (
          <ConceptNode key={index} concept={concept} />
        ))}
      </div>
    </div>
  );
}
