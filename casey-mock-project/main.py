from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from mock_data import PRODUCTS
from models import AcceptResponse

app = FastAPI(title="MarkdownIQ")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
def root():
    return RedirectResponse("/static/index.html")


@app.get("/api/products")
def get_products():
    return sorted(
        PRODUCTS,
        key=lambda p: p.expected_revenue_uplift_from_recommendation,
        reverse=True,
    )


@app.post("/api/products/{product_id}/accept", response_model=AcceptResponse)
def accept_product(product_id: str):
    if not any(p.product_id == product_id for p in PRODUCTS):
        raise HTTPException(status_code=404, detail="Product not found")
    return AcceptResponse(
        product_id=product_id,
        accepted=True,
        accepted_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    )
