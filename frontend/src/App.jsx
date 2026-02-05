import { useState } from "react";
import "./index.css";

const API_BASE =
  "https://learning-recommendation-system-1.onrender.com";

export default function App() {
  const [studentId, setStudentId] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

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
        throw new Error("API Error");
      }

      const data = await res.json();

      // ✅ BACKEND RETURNS ARRAY, NOT { recommendations }
      if (!Array.isArray(data) || data.length === 0) {
        setMessage(
          "This student is performing well. No weak topics detected."
        );
      } else {
        setRecommendations(data);
      }
    } catch (err) {
      console.error(err);
      setMessage(
        "Unable to connect to backend. Please try again."
      );
    }

    setLoading(false);
  };

  return (
    <div className="app-wrapper">
      {/* HERO CARD */}
      <div className="hero-card">
        <h1>Learning Recommendation System</h1>
        <p className="hero-subtitle">
          AI-powered personalized learning paths with explainable insights
        </p>

        <div className="input-row">
          <input
            type="number"
            placeholder="Enter Student ID (e.g. 1001)"
            value={studentId}
            onChange={(e) => setStudentId(e.target.value)}
          />
          <button onClick={fetchRecommendations}>
            Generate Plan
          </button>
        </div>

        {loading && (
          <p className="status loading">
            Analyzing performance & generating recommendations…
          </p>
        )}

        {message && (
          <p className="status">{message}</p>
        )}
      </div>

      {/* RESULTS SECTION */}
      {recommendations.length > 0 && (
        <div className="results-section">
          <h2>Your Personalized Learning Plan</h2>

          <div className="cards-grid">
            {recommendations.map((rec, idx) => (
              <div key={idx} className="resource-card">
                <div className="topic-chip">
                  {rec.Topic}
                </div>

                <h3>{rec.Title}</h3>

                <p className="resource-type">
                  {rec.ResourceType}
                </p>

                {/* Explanation */}
                <div className="explanation-box">
                  <h4>Why this was recommended</h4>
                  <p style={{ whiteSpace: "pre-line" }}>
                    {rec.Explanation}
                  </p>
                </div>

                {/* Resource Link */}
                {rec.Link &&
                rec.Link.startsWith("http") ? (
                  <a
                    href={rec.Link}
                    target="_blank"
                    rel="noreferrer"
                    className="resource-link"
                  >
                    Open Learning Resource →
                  </a>
                ) : (
                  <span className="ai-only">
                    AI-Generated Learning Guidance
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
