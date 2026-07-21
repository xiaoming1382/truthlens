"use client";

export default function Header() {
  return (
    <header style={{
      borderBottom: "1px solid var(--border-color)",
      padding: "16px 0",
      position: "sticky",
      top: 0,
      zIndex: 100,
      background: "rgba(10, 10, 10, 0.85)",
      backdropFilter: "blur(12px)",
    }}>
      <div className="container" style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
          <span style={{
            fontSize: "28px",
            fontFamily: "var(--font-mono)",
            color: "var(--accent)",
          }}>⌬</span>
          <div>
            <h1 style={{
              fontSize: "18px",
              fontWeight: 700,
              letterSpacing: "-0.5px",
            }}>TruthLens</h1>
            <p style={{
              fontSize: "11px",
              color: "var(--text-muted)",
              fontFamily: "var(--font-mono)",
            }}>POWERED BY TELEGRAPH PROTOCOL</p>
          </div>
        </div>
        <div style={{ display: "flex", gap: "8px" }}>
          <a
            href="https://hackathon.telegraphprotocol.com"
            target="_blank"
            rel="noopener noreferrer"
            className="btn btn-secondary"
            style={{ fontSize: "12px", padding: "8px 16px" }}
          >
            Telegraph Hackathon
          </a>
          <a
            href="https://github.com/telegraph-protocol"
            target="_blank"
            rel="noopener noreferrer"
            className="btn btn-secondary"
            style={{ fontSize: "12px", padding: "8px 16px" }}
          >
            GitHub
          </a>
        </div>
      </div>
    </header>
  );
}