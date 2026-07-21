export interface DetectionResult {
  content_type: string;
  content_preview: string;
  miner_id: number;
  miner_name: string;
  confidence_score: number;
  verdict: string;
  raw_response: {
    content_length?: number;
    content_type?: string;
    suspicious_indicators?: number;
    ai_indicators?: number;
  } | null;
  telegraph_verified: boolean;
  timestamp: string;
}

export interface SignalItem {
  id: string;
  source: string;
  status: string;
  created_at: string;
  question: {
    text: string;
    category: string;
    interest_score: number;
  };
  routing: {
    subnet_name: string;
    intent: string;
  };
}

export interface MinerInfo {
  id: number;
  slug: string;
  capability: string;
  min_price?: number;
}