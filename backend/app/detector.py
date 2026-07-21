"""
Detection engine that calls Telegraph miners via x402 payment flow.
For hackathon demo, supports mock mode when no wallet is configured.
"""
import base64
import httpx
from app.config import TELEGRAPH_DISPATCHER_URL

# Miner IDs for detection capabilities
MINER_ITS_AI = 32       # AI text detection
MINER_BITMIND = 34      # Deepfake / media authenticity
MINER_OPENAI = 102      # LLM analysis (fallback)


async def call_miner_with_mock(miner_id: int, content: str, content_type: str) -> dict:
    """
    Call a Telegraph miner. In hackathon demo mode, returns mock results
    based on content analysis heuristics so the app is fully functional
    even without testnet USDC setup.
    """
    # Try real call first
    try:
        result = await _call_miner_x402(miner_id, content, content_type)
        if result:
            return result
    except Exception:
        pass

    # Fallback to mock for demo
    return _generate_mock_result(miner_id, content, content_type)


async def _call_miner_x402(miner_id: int, content: str, content_type: str) -> dict | None:
    """
    Attempt a real x402 payment call to a Telegraph miner.
    Returns None if payment fails (e.g., no USDC configured).
    """
    base_url = f"{TELEGRAPH_DISPATCHER_URL}/v1/{miner_id}"

    async with httpx.AsyncClient() as client:
        # Step 1: Make request, expect 402
        if content_type == "text":
            resp = await client.get(
                f"{base_url}/detect",
                params={"text": content[:500]},
                timeout=30,
            )
        else:
            resp = await client.get(
                f"{base_url}/analyze",
                params={"url": content},
                timeout=30,
            )

        if resp.status_code == 402:
            # Payment required — in production, use PayAI SDK here
            # For hackathon demo, we return mock
            return None

        if resp.status_code == 200:
            return resp.json()

        return None


def _generate_mock_result(miner_id: int, content: str, content_type: str) -> dict:
    """Generate realistic mock detection result for demo purposes."""
    # Heuristic-based mock scoring
    text_lower = content.lower()
    suspicious_keywords = [
        "free money", "click here", "act now", "limited time",
        "congratulations", "you won", "urgent", "verify your",
        "crypto giveaway", "double your", "send bitcoin",
    ]
    ai_keywords = [
        "as a language model", "i'm sorry", "as an ai",
        "it's important to note", "in conclusion",
        "delve into", "leverage", "streamline",
        "tapestry", "testament", "symphony of",
    ]

    score = 0.85  # Start with high authenticity

    if content_type == "text":
        for kw in suspicious_keywords:
            if kw in text_lower:
                score -= 0.12
        for kw in ai_keywords:
            if kw in text_lower:
                score -= 0.06
        if len(content) < 20:
            score -= 0.05
        if content.count("!") > 5:
            score -= 0.1

    score = max(0.05, min(0.98, score))

    miner_names = {
        MINER_ITS_AI: "ItsAI Text Detector",
        MINER_BITMIND: "BitMind Authenticity",
        MINER_OPENAI: "OpenAI Analysis",
    }

    if score >= 0.75:
        verdict = "authentic"
    elif score >= 0.45:
        verdict = "suspicious"
    else:
        verdict = "likely_fake"

    return {
        "miner_id": miner_id,
        "miner_name": miner_names.get(miner_id, f"Miner #{miner_id}"),
        "confidence_score": round(score, 3),
        "verdict": verdict,
        "analysis_details": {
            "content_length": len(content),
            "content_type": content_type,
            "suspicious_indicators": sum(1 for kw in suspicious_keywords if kw in text_lower),
            "ai_indicators": sum(1 for kw in ai_keywords if kw in text_lower),
        },
        "telegraph_verified": False,  # Mock result, not telegraph-verified
        "demo_mode": True,
    }


def select_miner(content_type: str) -> int:
    """Select the appropriate miner based on content type."""
    if content_type == "text":
        return MINER_ITS_AI
    else:
        return MINER_BITMIND
