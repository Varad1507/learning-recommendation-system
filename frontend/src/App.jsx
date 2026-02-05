import { useState } from "react";
import "./index.css";

const API_BASE = "http://127.0.0.1:5000";

export default function App() {
  const [studentId, setStudentId] = useState("");
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(false);

  const generatePlan = async () => {
    if (!studentId) return;

    setLoading(true);
    setPlan(null);

    const res = await fetch(
      `${API_BASE}/recommend/${studentId}`
    );
    const json = await res.json();

    if (json.recommendations && json.recommendations.length > 0) {
      setPlan({
        topics: [...new Set(json.recommendations.map(r => r.Topic))],
        explanation: json.recommendations[0].Explanation
      });
    }

    setLoading(false);
  };

  return (
    <div className="page">
      <div className="hero-card">
        <h1>Learning Recommendation System</h1>
        <p className="subtitle">
          AI-powered personalized learning paths with explainable insights
        </p>

        <div className="input-group">
          <input
            type="number"
            placeholder="Enter Student ID"
            value={studentId}
            onChange={(e) => setStudentId(e.target.value)}
          />
          <button onClick={generatePlan}>
            Generate Plan
          </button>
        </div>
      </div>

      {loading && (
        <p className="loading-text">
          Generating AI learning plan…
        </p>
      )}

      {plan && (
        <div className="result-section">
          <h2>Your Personalized Learning Plan</h2>

          <div className="ai-card">
            <div className="topic-tags">
              {plan.topics.map((t, i) => (
                <span key={i}>{t}</span>
              ))}
            </div>

            <h3>AI-Generated Learning Plan</h3>
            <p className="ai-label">AI Recommendation</p>

            <div className="ai-box">
              <h4>Why this was recommended</h4>
              <p style={{ whiteSpace: "pre-line" }}>
                {plan.explanation}
              </p>
            </div>

            <p className="ai-footer">
              AI-Generated Learning Guidance
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
