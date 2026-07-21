import type { Metadata } from "next";
import "@/styles/globals.css";

export const metadata: Metadata = {
  title: "TruthLens — AI Content Authenticity Detector",
  description: "Detect AI-generated content, deepfakes, and misinformation using verified Telegraph Protocol miners.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}