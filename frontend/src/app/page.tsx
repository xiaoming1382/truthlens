import Header from "@/components/Header";
import DetectionPanel from "@/components/DetectionPanel";
import SignalFeed from "@/components/SignalFeed";
import MinerList from "@/components/MinerList";

export default function Home() {
  return (
    <>
      <Header />
      <main className="container" style={{ padding: "32px 24px 64px" }}>
        {/* Hero */}
        <section style={{ textAlign: "center", marginBottom: "48px" }}>
          <h1 style={{
            fontSize: "clamp(32px, 5vw, 56px)",
            fontWeight: 800,
            letterSpacing: "-2px",
            lineHeight: 1.1,
            marginBottom: "16px",
          }}>
            Can you trust what you
            <br />
            <span style={{ color: "var(--accent)" }}>see and read?</span>
          </h1>
          <p style={{
            fontSize: "17px",
            color: "var(--text-secondary)",
            maxWidth: "600px",
            margin: "0 auto",
          }}>
            TruthLens uses Telegraph Protocol&apos;s verified miners to detect AI-generated
            text, deepfakes, and misinformation. Every result is cryptographically verifiable.
          </p>
        </section>

        {/* Main Detection Area */}
        <section style={{ maxWidth: "800px", margin: "0 auto 48px" }}>
          <DetectionPanel />
        </section>

        {/* Bottom Grid: Signals + Miners */}
        <section className="grid-2">
          <SignalFeed />
          <MinerList />
        </section>

        {/* Footer */}
        <footer style={{
          marginTop: "64px",
          textAlign: "center",
          color: "var(--text-muted)",
          fontSize: "13px",
          borderTop: "1px solid var(--border-color)",
          paddingTop: "24px",
        }}>
          <p>TruthLens — Built for Telegraph Protocol Hackathon 2026</p>
          <p style={{ marginTop: "4px" }}>
            Powered by{" "}
            <a href="https://telegraphprotocol.com" target="_blank" rel="noopener noreferrer">
              Telegraph Protocol
            </a>{" "}
            on Base
          </p>
        </footer>
      </main>
    </>
  );
}