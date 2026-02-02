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
      const res = await fetch(
        `${API_BASE}/recommend/${studentId}`
      );

      if (!res.ok) {
        throw new Error("API error");
      }

      const data = await res.json();

      if (!data.recommendations || data.recommendations.length === 0) {
        setMessage(
          "Student is performing well. No weak topics detected."
        );
      } else {
        setRecommendations(data.recommendations);
      }
    } catch (error) {
      setMessage(
        "Backend not reachable. Please try again later."
      );
    }

    setLoading(false);
  };

  return (
    <div className="page">
      {/* Main Input Card */}
      <div className="main-card">
        <h1>📘 Learning Recommendation System</h1>

        <p className="subtitle">
          Personalized learning paths with explainable AI (RAG)
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

      {/* Results Section */}
      {recommendations.length > 0 && (
        <div className="results">
          <h2>📚 Recommended Resources</h2>

          <div className="results-grid">
            {recommendations.map((rec, idx) => (
              <div key={idx} className="result-card">
                <span className="topic">{rec.Topic}</span>

                <h3>{rec.Title}</h3>

                <p className="type">
                  {rec.ResourceType}
                </p>

                {/* RAG Explanation */}
                <details className="explain-box">
                  <summary>
                    Why was this recommended?
                  </summary>
                  <p className="explanation">
                    {rec.Explanation ||
                      "Explanation not available."}
                  </p>
                </details>

                {/* Resource Link */}
                {rec.Link && (
                  <a
                    href={rec.Link}
                    target="_blank"
                    rel="noreferrer"
                  >
                    Open Resource →
                  </a>
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
