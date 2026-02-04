import { useState } from "react";
import "./index.css";

const API_BASE =
  "https://learning-recommendation-system-1.onrender.com";

function App() {
  const [studentId, setStudentId] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const fetchRecommendations = async () => {
    if (!studentId) {
      setMessage("Please enter a Student ID");
      return;
    }

    setLoading(true);
    setMessage("");
    setRecommendations([]);

    try {
      const res = await fetch(`${API_BASE}/recommend/${studentId}`);
      if (!res.ok) throw new Error("API error");

      const data = await res.json();

      if (!data.recommendations || data.recommendations.length === 0) {
        setMessage(
          "Student is performing well. No weak topics detected."
        );
      } else {
        setRecommendations(data.recommendations);
      }
    } catch {
      setMessage(
        "Backend not reachable. Please try again later."
      );
    }

    setLoading(false);
  };

  const openExternalLink = (url) => {
    if (!url || !url.startsWith("http")) return;
    window.open(url, "_blank", "noopener,noreferrer");
  };

  return (
    <div className="page">
      {/* ================= INPUT CARD ================= */}
      <div className="main-card">
        <h1>📘 Learning Recommendation System</h1>

        <p className="subtitle">
          Personalized learning paths with explainable AI
        </p>

        <div className="input-section">
          <input
            type="number"
            placeholder="Enter Student ID (e.g. 1001)"
            value={studentId}
            onChange={(e) => setStudentId(e.target.value)}
          />

          <button onClick={fetchRecommendations}>
            Get Recommendations
          </button>
        </div>

        {loading && (
          <p className="status">
            🔍 Analyzing student performance…
          </p>
        )}

        {message && <p className="status">{message}</p>}
      </div>

      {/* ================= RESULTS ================= */}
      {recommendations.length > 0 && (
        <div className="results">
          <h2>📚 Recommended Resources</h2>

          <div className="results-grid">
            {recommendations.map((rec, idx) => (
              <div key={idx} className="result-card">
                <span className="topic">{rec.Topic}</span>

                <h3>{rec.Title}</h3>

                <p className="type">{rec.ResourceType}</p>

                {/* ===== STRUCTURED AI EXPLANATION ===== */}
                <details className="explain-box">
                  <summary>Why was this recommended?</summary>

                  {Array.isArray(rec.Explanation) ? (
                    <ul className="explanation-list">
                      {rec.Explanation.map((point, i) => (
                        <li key={i}>{point}</li>
                      ))}
                    </ul>
                  ) : (
                    <p className="explanation">
                      {rec.Explanation ||
                        "Explanation not available."}
                    </p>
                  )}
                </details>

                {/* ===== RESOURCE LINK / AI BADGE ===== */}
                {rec.Link && rec.Link.startsWith("http") ? (
                  <button
                    className="link-button"
                    onClick={() =>
                      openExternalLink(rec.Link)
                    }
                  >
                    Open Resource →
                  </button>
                ) : (
                  <span className="ai-badge">
                    🤖 AI-Generated Learning Plan
                  </span>
                )}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
