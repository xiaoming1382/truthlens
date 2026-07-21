"use client";

import { useState, useEffect } from "react";
import type { SignalItem } from "@/types";
import { getTopSignals } from "@/lib/api";

export default function SignalFeed() {
  const [signals, setSignals] = useState<SignalItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchSignals = async () => {
    try {
      const data = await getTopSignals(6, 8);
      setSignals(data.results || []);
      setError(null);
    } catch {
      setError("Failed to fetch signals from Telegraph Daemon");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSignals();
    const interval = setInterval(fetchSignals, 30000);
    return () => clearInterval(interval);
  }, []);

  const getCategoryColor = (cat: string) => {
    const colors: Record<string, string> = {
      CLIMATE: "#4488ff",
      FINANCE: "#00ff88",
      CRYPTO: "#ff8844",
      TECHNOLOGY: "#aa44ff",
      POLITICS: "#ff4444",
      SOCIAL: "#ff44ff",
    };
    return colors[cat] || "var(--text-muted)";
  };

  return (
    <div className="card animate-in">
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: "20px" }}>
        <div>
          <h2 style={{ fontSize: "16px", fontWeight: 600 }}>Live Signal Feed</h2>
          <p style={{ fontSize: "12px", color: "var(--text-muted)" }}>
            Verified intelligence from Telegraph Daemon
          </p>
        </div>
        <span className="badge badge-verified">LIVE</span>
      </div>

      {loading && (
        <div style={{ textAlign: "center", padding: "40px", color: "var(--text-muted)" }}>
          <span className="animate-pulse">Loading signals...</span>
        </div>
      )}

      {error && (
        <div style={{
          padding: "16px",
          background: "#ff444410",
          border: "1px solid #ff444430",
          borderRadius: "var(--radius-sm)",
          color: "#ff4444",
          fontSize: "14px",
        }}>
          {error}
        </div>
      )}

      <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
        {signals.map((signal) => (
          <div
            key={signal.id}
            style={{
              padding: "12px 16px",
              background: "var(--bg-primary)",
              borderRadius: "var(--radius-sm)",
              border: "1px solid var(--border-color)",
              display: "flex",
              alignItems: "flex-start",
              justifyContent: "space-between",
              gap: "12px",
            }}
          >
            <div style={{ flex: 1 }}>
              <p style={{ fontSize: "13px", fontWeight: 500, marginBottom: "4px" }}>
                {signal.question.text}
              </p>
              <div style={{ display: "flex", gap: "8px", alignItems: "center" }}>
                <span style={{
                  fontSize: "11px",
                  fontFamily: "var(--font-mono)",
                  color: getCategoryColor(signal.question.category),
                  fontWeight: 600,
                }}>
                  {signal.question.category}
                </span>
                <span style={{ fontSize: "11px", color: "var(--text-muted)" }}>
                  via {signal.routing.subnet_name.split("-").pop()}
                </span>
              </div>
            </div>
            <div style={{ textAlign: "right" }}>
              <span style={{
                fontSize: "16px",
                fontWeight: 700,
                fontFamily: "var(--font-mono)",
                color: signal.question.interest_score >= 7 ? "var(--accent)" : "var(--text-muted)",
              }}>
                {signal.question.interest_score.toFixed(1)}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}