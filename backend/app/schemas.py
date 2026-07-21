from pydantic import BaseModel
from typing import Optional, Any


class DetectionRequest(BaseModel):
    content_type: str  # "text" or "image_url"
    content: str  # text content or image URL


class DetectionResult(BaseModel):
    content_type: str
    content_preview: str
    miner_id: int
    miner_name: str
    confidence_score: float  # 0.0 to 1.0, higher = more likely authentic
    verdict: str  # "authentic", "suspicious", "likely_fake"
    raw_response: Optional[Any] = None
    telegraph_verified: bool = True
    timestamp: str


class SignalItem(BaseModel):
    id: str
    source: str
    status: str
    created_at: str
    question_text: str
    category: str
    interest_score: float


class HealthResponse(BaseModel):
    status: str
    telegraph_daemon: str
    telegraph_dispatcher: str
