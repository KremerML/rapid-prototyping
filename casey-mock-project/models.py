from pydantic import BaseModel


class Product(BaseModel):
    product_id: str
    product_name: str
    category: str
    current_price: float
    proposed_markdown_price: float
    clearance_price: float
    stock_on_hand: int
    remaining_days_in_season: int
    estimated_sales_per_day_if_wait: float
    estimated_sales_per_day_if_reduce: float
    expected_revenue_if_wait: float
    expected_revenue_if_reduce: float
    recommendation: str  # "WAIT" | "REDUCE"
    expected_revenue_uplift_from_recommendation: float
    confidence_score: float  # 0.0–1.0
    store_region: str | None = None
    channel: str | None = None


class AcceptResponse(BaseModel):
    product_id: str
    accepted: bool
    accepted_at: str
