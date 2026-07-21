from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
from datetime import datetime, timezone
from app.schemas import DetectionRequest, DetectionResult, SignalItem, HealthResponse
from app.telegraph_client import (
    get_daemon_health,
    get_dispatcher_health,
    get_available_miners,
    get_daemon_signals,
    get_top_signals,
    get_categories,
)
from app.detector import call_miner_with_mock, select_miner
import httpx
import asyncio

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    try:
        daemon = await get_daemon_health()
        daemon_status = daemon.get("status", "unknown")
    except Exception:
        daemon_status = "offline"

    try:
        dispatcher = await get_dispatcher_health()
        dispatcher_status = dispatcher.get("status", "ok")
    except Exception:
        dispatcher_status = "offline"

    return HealthResponse(
        status="ok" if daemon_status != "offline" else "degraded",
        telegraph_daemon=daemon_status,
        telegraph_dispatcher=dispatcher_status,
    )


@router.get("/miners")
async def list_miners():
    """List all available Telegraph miners."""
    miners = await get_available_miners()
    return {"miners": miners, "total": len(miners) if isinstance(miners, list) else 0}


@router.post("/detect", response_model=DetectionResult)
async def detect_content(request: DetectionRequest):
    """
    Detect content authenticity using Telegraph miners.
    Routes to the appropriate miner based on content type.
    """
    miner_id = select_miner(request.content_type)
    result = await call_miner_with_mock(
        miner_id=miner_id,
        content=request.content,
        content_type=request.content_type,
    )

    return DetectionResult(
        content_type=request.content_type,
        content_preview=request.content[:200] + ("..." if len(request.content) > 200 else ""),
        miner_id=result["miner_id"],
        miner_name=result["miner_name"],
        confidence_score=result["confidence_score"],
        verdict=result["verdict"],
        raw_response=result.get("analysis_details"),
        telegraph_verified=result.get("telegraph_verified", False),
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@router.get("/signals")
async def list_signals(
    category: str | None = None,
    limit: int = 20,
    offset: int = 0,
    min_interest: float | None = None,
):
    """Fetch signals from the Telegraph Daemon feed."""
    data = await get_daemon_signals(
        category=category,
        limit=limit,
        offset=offset,
        min_interest=min_interest,
    )
    return data


@router.get("/signals/top")
async def top_signals(since_hours: int = 1, limit: int = 10):
    """Fetch top signals by interest score."""
    data = await get_top_signals(since_hours=since_hours, limit=limit)
    return data


@router.get("/categories")
async def list_categories():
    """Get all signal categories with stats."""
    data = await get_categories()
    return data


@router.websocket("/ws/signals")
async def websocket_signals(websocket: WebSocket):
    """WebSocket endpoint for real-time signal updates."""
    await websocket.accept()
    try:
        while True:
            try:
                signals = await get_top_signals(since_hours=1, limit=5)
                await websocket.send_json({"type": "signals", "data": signals})
                await asyncio.sleep(30)  # Poll every 30 seconds
            except httpx.HTTPError:
                await asyncio.sleep(10)
    except WebSocketDisconnect:
        pass
