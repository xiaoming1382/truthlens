import httpx
from app.config import TELEGRAPH_DAEMON_URL, TELEGRAPH_DISPATCHER_URL


async def get_daemon_health():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{TELEGRAPH_DAEMON_URL}/health", timeout=10)
        return resp.json()


async def get_dispatcher_health():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{TELEGRAPH_DISPATCHER_URL}/healthz", timeout=10)
        return resp.json()


async def get_available_miners():
    """Get list of registered miners with schemas and prices."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{TELEGRAPH_DISPATCHER_URL}/integrations", timeout=15)
        return resp.json()


async def get_daemon_signals(
    category: str | None = None,
    limit: int = 20,
    offset: int = 0,
    sort: str = "recent",
    min_interest: float | None = None,
):
    """Fetch signals from the Daemon feed (free, no payment needed)."""
    params = {"limit": limit, "offset": offset, "sort": sort}
    if category:
        params["category"] = category
    if min_interest is not None:
        params["min_interest"] = min_interest

    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{TELEGRAPH_DAEMON_URL}/api/questions",
            params=params,
            timeout=15,
        )
        return resp.json()


async def get_top_signals(since_hours: int = 1, limit: int = 10):
    """Fetch top signals by interest score."""
    params = {"since_hours": since_hours, "limit": limit}
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{TELEGRAPH_DAEMON_URL}/api/questions/top",
            params=params,
            timeout=15,
        )
        return resp.json()


async def get_categories():
    """Get all signal categories with stats."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{TELEGRAPH_DAEMON_URL}/api/categories", timeout=15)
        return resp.json()
