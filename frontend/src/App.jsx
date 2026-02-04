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
        setMessage("Student is performing well. No weak topics detected.");
      } else {
        setRecommendations(data.recommendations);
      }
    } catch {
      setMessage("Backend not reachable. Please try again later.");
    }

    setLoading(false);
  };

  return (
    <div className="page">
      {/* Header */}
      <header className="header">
        <h1>Learning Recommendation System</h1>
        <p>AI-powered personalized learning with explainability</p>
      </header>

      {/* Input Card */}
      <div className="card input-card">
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

      {loading && <p className="status loading">Analyzing student performance…</p>}
      {message && <p className="status">{message}</p>}

      {/* Results */}
      {recommendations.length > 0 && (
        <section className="results">
          <h2>Recommended Learning Resources</h2>

          <div className="results-grid">
            {recommendations.map((rec, idx) => (
              <div key={idx} className="card resource-card">
                <div className="card-header">
                  <span className="topic-tag">{rec.Topic}</span>
                  <span className="type-tag">{rec.ResourceType}</span>
                </div>

                <h3>{rec.Title}</h3>

                {/* Structured Explanation */}
                <div className="explanation-box">
                  <h4>Why this was recommended</h4>
                  <ul>
                    {Array.isArray(rec.Explanation)
                      ? rec.Explanation.map((point, i) => (
                          <li key={i}>{point}</li>
                        ))
                      : <li>{rec.Explanation}</li>}
                  </ul>
                </div>

                {/* Resource Action */}
                {rec.Link && rec.Link.startsWith("http") ? (
                  <a
                    href={rec.Link}
                    target="_blank"
                    rel="noreferrer"
                    className="resource-link"
                  >
                    Open Resource →
                  </a>
                ) : (
                  <span className="ai-badge">
                    AI-Generated Learning Plan
                  </span>
                )}
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}

export default App;
