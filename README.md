# TruthLens

**AI Content Authenticity Detector powered by Telegraph Protocol**

> Built for the [Telegraph Hackathon](https://hackathon.telegraphprotocol.com) — Track 3: Applications

## What is TruthLens?

TruthLens is a web application that detects AI-generated content, deepfakes, and misinformation using **Telegraph Protocol's verified miners**. Instead of trusting a single model, TruthLens routes content analysis through Telegraph's decentralized miner network — where responses are graded by independent validators and settled on-chain.

### Key Features

- **Text Authenticity Detection** — Paste any text to check if it's AI-generated, spam, or misinformation via the ItsAI miner (#32)
- **Deepfake / Media Detection** — Submit image URLs to detect manipulated media via the BitMind miner (#34)
- **Verifiable Results** — Every detection can be traced back to a Telegraph miner with on-chain settlement proof
- **Live Signal Feed** — Real-time verified intelligence from the Telegraph Daemon, showing what the network is currently analyzing
- **Zero-Trust Architecture** — No single point of failure; miners compete on quality, validators grade independently

## How It Works

```
User Content
    ↓
TruthLens App (Next.js + FastAPI)
    ↓ POST /api/v1/detect
Telegraph Miner Dispatcher
    ↓ Route to best-ranked miner (x402 payment)
Miner (ItsAI / BitMind / OpenAI)
    ↓ Return analysis
Validators (WASM scoring + BFT consensus)
    ↓ Finalized score
TruthLens displays result with confidence + verdict
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 14, React 18, TypeScript |
| Backend | FastAPI, Python 3.11, httpx |
| Protocol | Telegraph Protocol (x402 payments, Daemon signals) |
| Chain | Base (Ethereum L2) |
| Miners Used | ItsAI (#32) — text detection, BitMind (#34) — deepfake detection |

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 20+
- (Optional) Base Sepolia testnet USDC for x402 payments

### 1. Start the Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs available at: http://localhost:8000/docs

### 2. Start the Frontend

```bash
cd frontend
npm install
npm run dev
```

App available at: http://localhost:3000

### 3. Demo Mode

TruthLens works out of the box in **demo mode** — it uses heuristic-based mock results when no testnet USDC wallet is configured. This means the app is fully functional for hackathon demos without any blockchain setup.

To enable real Telegraph miner calls via x402:
1. Get testnet USDC on Base Sepolia
2. Configure the PayAI SDK in `backend/app/detector.py`

## Project Structure

```
truthlens/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entry
│   │   ├── routes.py            # API routes (detect, signals, miners, WebSocket)
│   │   ├── detector.py          # Detection engine (x402 + mock fallback)
│   │   ├── telegraph_client.py  # Telegraph Daemon/Dispatcher client
│   │   ├── schemas.py           # Pydantic models
│   │   └── config.py            # Environment config
│   ├── requirements.txt
│   ├── .env
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── layout.tsx       # Root layout
│   │   │   └── page.tsx         # Main page
│   │   ├── components/
│   │   │   ├── Header.tsx       # Navigation bar
│   │   │   ├── DetectionPanel.tsx  # Core detection UI
│   │   │   ├── SignalFeed.tsx   # Live signal feed
│   │   │   └── MinerList.tsx    # Active miners
│   │   ├── lib/
│   │   │   └── api.ts           # API client
│   │   ├── types/
│   │   │   └── index.ts         # TypeScript types
│   │   └── styles/
│   │       └── globals.css      # Dark theme
│   ├── package.json
│   ├── Dockerfile
│   └── .env.local
├── docker-compose.yml
└── README.md
```

## Telegraph Integration

### Miners Used

| Miner | ID | Capability | Use Case |
|-------|----|-----------|----------|
| ItsAI | 32 | AI text detection | Detect AI-generated text, spam patterns |
| BitMind | 34 | Deepfake / media authenticity | Detect manipulated images and deepfakes |
| OpenAI | 102 | LLM analysis | Fallback analysis for complex content |

### Data Sources

- **Daemon Signal Feed** (free, no payment): Real-time verified intelligence from Telegraph's autonomous Daemon
- **On-Demand Inference** (x402 payment): Direct miner calls for custom content analysis

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/detect` | POST | Analyze content via Telegraph miner |
| `/api/v1/signals` | GET | Fetch Daemon signal feed |
| `/api/v1/signals/top` | GET | Top signals by interest score |
| `/api/v1/miners` | GET | List active Telegraph miners |
| `/api/v1/categories` | GET | Signal categories with stats |
| `/api/v1/health` | GET | Backend + Telegraph connectivity status |
| `/api/v1/ws/signals` | WebSocket | Real-time signal push |

## Hackathon Submission

- **Track**: Track 3 — Applications
- **Project Name**: TruthLens
- **Miners**: Financial Data, On-chain Analysis, Social Sentiment, AI / LLM Inference
- **Tech Stack**: Python, FastAPI, Next.js, TypeScript, httpx, Telegraph x402 Protocol

## License

MIT
