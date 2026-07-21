"use client";

import { useState, useEffect } from "react";
import type { MinerInfo } from "@/types";
import { getMiners } from "@/lib/api";

export default function MinerList() {
  const [miners, setMiners] = useState<MinerInfo[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getMiners().then((data) => {
      setMiners(data.miners || []);
      setLoading(false);
    });
  }, []);

  return (
    <div className="card animate-in">
      <h2 style={{ fontSize: "16px", fontWeight: 600, marginBottom: "4px" }}>
        Active Miners
      </h2>
      <p style={{ fontSize: "12px", color: "var(--text-muted)", marginBottom: "16px" }}>
        Detection capabilities powered by Telegraph miners
      </p>

      {loading ? (
        <div style={{ textAlign: "center", padding: "24px", color: "var(--text-muted)" }}>Loading...</div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
          {miners.map((miner) => (
            <div
              key={miner.id}
              style={{
                padding: "12px 16px",
                background: "var(--bg-primary)",
                borderRadius: "var(--radius-sm)",
                border: "1px solid var(--border-color)",
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
              }}
            >
              <div>
                <span style={{
                  fontSize: "14px",
                  fontWeight: 600,
                  fontFamily: "var(--font-mono)",
                }}>
                  #{miner.id}
                </span>
                <span style={{ fontSize: "14px", marginLeft: "8px" }}>
                  {miner.capability}
                </span>
              </div>
              {miner.min_price !== undefined && (
                <span style={{
                  fontSize: "13px",
                  fontFamily: "var(--font-mono)",
                  color: "var(--accent)",
                }}>
                  ${miner.min_price.toFixed(2)}/call
                </span>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}