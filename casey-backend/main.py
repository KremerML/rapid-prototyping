import asyncio
import json
import datetime
from pathlib import Path
from typing import AsyncIterator

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(title="MoreWear Inventory API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# In-memory state
# ---------------------------------------------------------------------------

DATA_FILE = Path(__file__).parent / "data" / "inventory.json"

with open(DATA_FILE) as f:
    _raw = json.load(f)

# Keyed by sku_id for O(1) lookups
inventory: dict[str, dict] = {item["sku_id"]: item for item in _raw}

# SSE subscriber queues — one per connected client
_subscribers: list[asyncio.Queue] = []

# ---------------------------------------------------------------------------
# Schemas
# ---------------------------------------------------------------------------

class AcceptRecommendation(BaseModel):
    sku_id: str
    recommended_price: float

# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/api/inventory")
def get_inventory():
    return list(inventory.values())


@app.post("/api/recommendations/accept")
async def accept_recommendation(body: AcceptRecommendation):
    sku = inventory.get(body.sku_id)
    if sku is None:
        raise HTTPException(status_code=404, detail=f"SKU '{body.sku_id}' not found")

    sku["current_price"] = round(body.recommended_price, 2)
    sku["status"]        = "On Markdown"
    sku["last_updated"]  = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    # Broadcast to all SSE subscribers
    payload = json.dumps(sku)
    for q in list(_subscribers):
        await q.put(payload)

    return sku


@app.get("/api/inventory/stream")
async def inventory_stream():
    """SSE endpoint — clients receive updated SKU objects in real time."""
    queue: asyncio.Queue = asyncio.Queue()
    _subscribers.append(queue)

    async def event_generator() -> AsyncIterator[dict]:
        try:
            # Send a heartbeat immediately so the browser knows it's connected
            yield {"event": "connected", "data": "stream open"}
            while True:
                try:
                    data = await asyncio.wait_for(queue.get(), timeout=20)
                    yield {"event": "sku_update", "data": data}
                except asyncio.TimeoutError:
                    # Keep-alive ping every 20 s to prevent proxy timeouts
                    yield {"event": "ping", "data": ""}
        finally:
            _subscribers.remove(queue)

    return EventSourceResponse(event_generator())


# ---------------------------------------------------------------------------
# Serve inventory UI
# ---------------------------------------------------------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/inventory.html")
