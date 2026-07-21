"use client";

import { useState } from "react";
import type { DetectionResult } from "@/types";
import { detectContent } from "@/lib/api";

export default function DetectionPanel() {
  const [tab, setTab] = useState<"text" | "image_url">("text");
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<DetectionResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleDetect = async () => {
    if (!content.trim()) return;
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const data = await detectContent(tab, content);
      setResult(data);
    } catch (err) {
      setError("Detection failed. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  const getScoreColor = (score: number) => {
    if (score >= 0.75) return "#00ff88";
    if (score >= 0.45) return "#ffaa00";
    return "#ff4444";
  };

  const getVerdictClass = (verdict: string) => {
    switch (verdict) {
      case "authentic": return "badge-authentic";
      case "suspicious": return "badge-suspicious";
      case "likely_fake": return "badge-fake";
      default: return "";
    }
  };

  return (
    <div className="card animate-in">
      <div style={{ marginBottom: "20px" }}>
        <h2 style={{ fontSize: "16px", fontWeight: 600, marginBottom: "12px" }}>
          Content Detection
        </h2>
        <div className="tab-group">
          <button
            className={`tab ${tab === "text" ? "tab-active" : ""}`}
            onClick={() => setTab("text")}
          >
            📝 Text
          </button>
          <button
            className={`tab ${tab === "image_url" ? "tab-active" : ""}`}
            onClick={() => setTab("image_url")}
          >
            🖼️ Image URL
          </button>
        </div>
      </div>

      {tab === "text" ? (
        <textarea
          className="detection-input"
          placeholder="Paste text here to check for AI-generated content, spam, or misinformation..."
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
      ) : (
        <input
          className="detection-input"
          style={{ minHeight: "auto" }}
          type="url"
          placeholder="Enter image URL to check for deepfakes or manipulation..."
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
      )}

      <div style={{ marginTop: "16px", display: "flex", alignItems: "center", gap: "12px" }}>
        <button
          className="btn btn-primary"
          onClick={handleDetect}
          disabled={loading || !content.trim()}
        >
          {loading ? (
            <>
              <span className="animate-pulse">⏳</span>
              Analyzing via Telegraph...
            </>
          ) : (
            <>🔍 Detect Authenticity</>
          )}
        </button>
        {content && (
          <span style={{ fontSize: "12px", color: "var(--text-muted)" }}>
            {content.length} characters
          </span>
        )}
      </div>

      {error && (
        <div style={{
          marginTop: "16px",
          padding: "12px 16px",
          background: "#ff444410",
          border: "1px solid #ff444430",
          borderRadius: "var(--radius-sm)",
          color: "#ff4444",
          fontSize: "14px",
        }}>
          {error}
        </div>
      )}

      {result && (
        <div className="animate-in" style={{
          marginTop: "24px",
          padding: "24px",
          background: "var(--bg-primary)",
          borderRadius: "var(--radius-sm)",
          border: "1px solid var(--border-color)",
        }}>
          <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: "16px" }}>
            <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
              <span className={`badge ${getVerdictClass(result.verdict)}`}>
                {result.verdict.toUpperCase()}
              </span>
              {result.telegraph_verified && (
                <span className="badge badge-verified">TELEGRAPH VERIFIED</span>
              )}
            </div>
            <span style={{ fontSize: "12px", color: "var(--text-muted)" }}>
              {new Date(result.timestamp).toLocaleTimeString()}
            </span>
          </div>

          {/* Score Bar */}
          <div style={{ marginBottom: "16px" }}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "6px" }}>
              <span style={{ fontSize: "13px", color: "var(--text-secondary)" }}>Confidence Score</span>
              <span style={{
                fontSize: "20px",
                fontWeight: 700,
                fontFamily: "var(--font-mono)",
                color: getScoreColor(result.confidence_score),
              }}>
                {(result.confidence_score * 100).toFixed(1)}%
              </span>
            </div>
            <div className="score-bar">
              <div
                className="score-bar-fill"
                style={{
                  width: `${result.confidence_score * 100}%`,
                  background: getScoreColor(result.confidence_score),
                }}
              />
            </div>
          </div>

          {/* Details */}
          <div className="grid-2" style={{ gap: "16px" }}>
            <div>
              <span style={{ fontSize: "12px", color: "var(--text-muted)" }}>Miner</span>
              <p style={{ fontSize: "14px", fontWeight: 600 }}>
                {result.miner_name} <span style={{ color: "var(--text-muted)" }}>#{result.miner_id}</span>
              </p>
            </div>
            <div>
              <span style={{ fontSize: "12px", color: "var(--text-muted)" }}>Content Type</span>
              <p style={{ fontSize: "14px" }}>{result.content_type}</p>
            </div>
          </div>

          {result.raw_response && (
            <div style={{
              marginTop: "16px",
              padding: "12px",
              background: "var(--bg-card)",
              borderRadius: "var(--radius-sm)",
              fontSize: "13px",
              fontFamily: "var(--font-mono)",
            }}>
              {Object.entries(result.raw_response).map(([key, value]) => (
                <div key={key} style={{ display: "flex", justifyContent: "space-between", padding: "4px 0" }}>
                  <span style={{ color: "var(--text-muted)" }}>{key}:</span>
                  <span style={{ color: "var(--text-primary)" }}>{String(value)}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}