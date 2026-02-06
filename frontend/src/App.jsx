import { useState, useMemo } from "react";
import "./index.css";

const API_BASE = "http://127.0.0.1:5000";
const PARAGRAPHS_PER_LOAD = 3;

export default function App() {
  const [studentId, setStudentId] = useState("");
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(false);
  const [visibleCount, setVisibleCount] = useState(PARAGRAPHS_PER_LOAD);

  const generatePlan = async () => {
    if (!studentId) return;

    setLoading(true);
    setPlan(null);
    setVisibleCount(PARAGRAPHS_PER_LOAD);

    const res = await fetch(`${API_BASE}/recommend/${studentId}`);
    const json = await res.json();

    if (json.recommendations && json.recommendations.length > 0) {
      setPlan({
        topics: [...new Set(json.recommendations.map(r => r.Topic))],
        explanation: json.recommendations[0].Explanation,
        resources: json.recommendations
      });
    }

    setLoading(false);
  };

  const cleanText = (text) => {
    return text.replace(/\*\*/g, "");
  };

  const explanationParagraphs = useMemo(() => {
    if (!plan?.explanation) return [];
    return cleanText(plan.explanation)
      .split(/\n\s*\n/)
      .map(p => p.trim())
      .filter(Boolean);
  }, [plan]);

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

            <div className="explanation-wrapper">
              <div className="ai-box explanation">
                <h4>Why this was recommended</h4>

                {explanationParagraphs
                  .slice(0, visibleCount)
                  .map((para, i) => (
                    <p key={i} style={{ whiteSpace: "pre-line" }}>
                      {para}
                    </p>
                  ))}

                {visibleCount < explanationParagraphs.length && (
                  <button
                    onClick={() =>
                      setVisibleCount(v =>
                        Math.min(
                          v + PARAGRAPHS_PER_LOAD,
                          explanationParagraphs.length
                        )
                      )
                    }
                    style={{
                      marginTop: "32px",
                      background: "transparent",
                      border: "1px solid #6366f1",
                      color: "#a5b4fc",
                      padding: "12px 24px",
                      borderRadius: "12px",
                      cursor: "pointer",
                      fontSize: "1rem"
                    }}
                  >
                    Show more
                  </button>
                )}
              </div>
            </div>

            <div className="resource-section">
              <h4>Recommended Resources</h4>

              {plan.resources.map((res, i) => (
                <div key={i} className="resource-item">
                  <span className="resource-type">
                    {res.ResourceType}
                  </span>
                  <a
                    href={res.Link}
                    target="_blank"
                    rel="noreferrer"
                  >
                    {res.Title}
                  </a>
                </div>
              ))}
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
