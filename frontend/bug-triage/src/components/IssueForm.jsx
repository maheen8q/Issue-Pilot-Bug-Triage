import { useState } from "react";
import api from "../services/api";

function IssueForm() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    setLoading(true);
    setError("");

    try {
      const response = await api.post("/analyze", {
        title,
        description,
      });

      setResult(response.data);
    } catch (err) {
      setError("Failed to analyze issue.");
      console.error(err);
    }

    setLoading(false);
  };

  const getComponentIcon = (component) => {
    switch (component) {
      case "frontend":
        return "🎨";

      case "backend":
        return "🖥";

      case "api":
        return "⚙";

      case "database":
        return "🗄";

      case "auth":
        return "🔐";

      default:
        return "📦";
    }
  };

  return (
    <div className="form-card">
      <label>Issue Title</label>

      <input
        type="text"
        placeholder="Enter issue title..."
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />

      <label>Description</label>

      <textarea
        rows={7}
        placeholder="Describe the issue..."
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <button onClick={handleAnalyze}>
        {loading ? "Analyzing..." : "Run Triage"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div className="results">
          <h2>Prediction</h2>

          <div className="prediction-grid">
            <div className="card">
              <h3>Priority</h3>
              <span className={`badge ${result.priority}`}>
                {result.priority.toUpperCase()}
              </span>
            </div>
            <div className="card">
              <h3>Component</h3>

              <p className="component-text">
                {getComponentIcon(result.component)}{" "}
                {result.component.toUpperCase()}
              </p>
            </div>
          </div>

          <h2>Similar Issues</h2>

          <div className="similar-list">
            {result.similar_issues.map((issue, index) => (
              <div className="issue-card" key={index}>
                <h3>{issue.title}</h3>

                <p>
                  Similarity:
                  {(issue.similarity_score * 100).toFixed(1)}%
                </p>

                <a href={issue.issue_url} target="_blank" rel="noreferrer">
                  View on GitHub
                </a>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default IssueForm;
