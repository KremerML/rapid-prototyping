"""
Run once to produce data/inventory.json.

The 25 hero SKUs are taken verbatim from the frontend catalogue so that
POST /api/recommendations/accept can always find them.  75 additional rows
pad the table to 100 items for a realistic inventory view.
"""
import json, random, datetime

random.seed(42)

STORES = ["Amsterdam Centrum", "Rotterdam Zuid", "Utrecht Hoog Catharijne", "Den Haag Centrum"]

# ── 25 hero SKUs copied from the frontend catalogue ──────────────────────────
HERO = [
    # Outerwear
    {"sku_id":"OW-001","product_name":"Winter Parka",     "category":"Outerwear",   "original_price":249.00,"current_price":249.00,"stock_quantity":260,"weeks_on_shelf":11,"status":"Active"},
    {"sku_id":"OW-002","product_name":"Trench Coat",      "category":"Outerwear",   "original_price":169.00,"current_price":169.00,"stock_quantity":145,"weeks_on_shelf":6, "status":"Active"},
    {"sku_id":"OW-003","product_name":"Rain Jacket",      "category":"Outerwear",   "original_price":109.00,"current_price":109.00,"stock_quantity":88, "weeks_on_shelf":4, "status":"Active"},
    {"sku_id":"OW-004","product_name":"Puffer Vest",      "category":"Outerwear",   "original_price":79.00, "current_price":79.00, "stock_quantity":72, "weeks_on_shelf":7, "status":"Active"},
    # Tops
    {"sku_id":"TP-001","product_name":"Oxford Shirt",     "category":"Tops",        "original_price":75.00, "current_price":75.00, "stock_quantity":200,"weeks_on_shelf":9, "status":"Active"},
    {"sku_id":"TP-002","product_name":"Linen Blouse",     "category":"Tops",        "original_price":59.00, "current_price":59.00, "stock_quantity":155,"weeks_on_shelf":5, "status":"Active"},
    {"sku_id":"TP-003","product_name":"Graphic Tee",      "category":"Tops",        "original_price":34.00, "current_price":34.00, "stock_quantity":95, "weeks_on_shelf":2, "status":"Active"},
    {"sku_id":"TP-004","product_name":"Crop Top",         "category":"Tops",        "original_price":29.00, "current_price":29.00, "stock_quantity":55, "weeks_on_shelf":2, "status":"Active"},
    # Bottoms
    {"sku_id":"BT-001","product_name":"Wide Leg Jeans",   "category":"Bottoms",     "original_price":119.00,"current_price":119.00,"stock_quantity":310,"weeks_on_shelf":5, "status":"Active"},
    {"sku_id":"BT-002","product_name":"Slim Chinos",      "category":"Bottoms",     "original_price":89.00, "current_price":89.00, "stock_quantity":180,"weeks_on_shelf":8, "status":"Active"},
    {"sku_id":"BT-003","product_name":"Track Pants",      "category":"Bottoms",     "original_price":68.00, "current_price":68.00, "stock_quantity":160,"weeks_on_shelf":6, "status":"Active"},
    {"sku_id":"BT-004","product_name":"Mini Skirt",       "category":"Bottoms",     "original_price":48.00, "current_price":48.00, "stock_quantity":45, "weeks_on_shelf":2, "status":"Active"},
    {"sku_id":"BT-005","product_name":"Cargo Shorts",     "category":"Bottoms",     "original_price":55.00, "current_price":55.00, "stock_quantity":40, "weeks_on_shelf":4, "status":"Active"},
    # Footwear
    {"sku_id":"FW-001","product_name":"Leather Sneakers", "category":"Footwear",    "original_price":195.00,"current_price":195.00,"stock_quantity":225,"weeks_on_shelf":9, "status":"Active"},
    {"sku_id":"FW-002","product_name":"Chelsea Boots",    "category":"Footwear",    "original_price":159.00,"current_price":159.00,"stock_quantity":148,"weeks_on_shelf":8, "status":"Active"},
    {"sku_id":"FW-003","product_name":"Sandals",          "category":"Footwear",    "original_price":72.00, "current_price":72.00, "stock_quantity":140,"weeks_on_shelf":3, "status":"Active"},
    {"sku_id":"FW-004","product_name":"Platform Clogs",   "category":"Footwear",    "original_price":92.00, "current_price":92.00, "stock_quantity":38, "weeks_on_shelf":5, "status":"Active"},
    # Accessories
    {"sku_id":"AC-001","product_name":"Wool Scarf",       "category":"Accessories", "original_price":62.00, "current_price":62.00, "stock_quantity":210,"weeks_on_shelf":12,"status":"Active"},
    {"sku_id":"AC-002","product_name":"Belt",             "category":"Accessories", "original_price":46.00, "current_price":46.00, "stock_quantity":95, "weeks_on_shelf":6, "status":"Active"},
    {"sku_id":"AC-003","product_name":"Sunglasses",       "category":"Accessories", "original_price":68.00, "current_price":68.00, "stock_quantity":35, "weeks_on_shelf":2, "status":"Active"},
    {"sku_id":"AC-004","product_name":"Canvas Tote",      "category":"Accessories", "original_price":28.00, "current_price":28.00, "stock_quantity":30, "weeks_on_shelf":1, "status":"Active"},
    # Knitwear
    {"sku_id":"KN-001","product_name":"Merino Sweater",   "category":"Knitwear",    "original_price":185.00,"current_price":185.00,"stock_quantity":195,"weeks_on_shelf":10,"status":"Active"},
    {"sku_id":"KN-002","product_name":"Cardigan",         "category":"Knitwear",    "original_price":89.00, "current_price":89.00, "stock_quantity":140,"weeks_on_shelf":8, "status":"Active"},
    {"sku_id":"KN-003","product_name":"Turtleneck",       "category":"Knitwear",    "original_price":76.00, "current_price":76.00, "stock_quantity":105,"weeks_on_shelf":7, "status":"Active"},
    {"sku_id":"KN-004","product_name":"Knit Vest",        "category":"Knitwear",    "original_price":55.00, "current_price":55.00, "stock_quantity":42, "weeks_on_shelf":4, "status":"Active"},
]

# Assign stores and last_updated to hero items
BASE_DT = datetime.datetime(2026, 4, 9, 10, 30)
for item in HERO:
    item["store"] = random.choice(STORES)
    days_ago = random.randint(0, item["weeks_on_shelf"] * 7)
    item["last_updated"] = (BASE_DT - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%S")

# ── 75 filler SKUs ────────────────────────────────────────────────────────────
EXTRA_PRODUCTS = {
    "Outerwear":   ["Denim Jacket","Quilted Gilet","Wool Overcoat","Fleece Half-Zip","Bomber Jacket"],
    "Tops":        ["Ribbed Tank","Oversized Sweatshirt","Silk Blouse","Printed Tee","Merino Jumper"],
    "Bottoms":     ["Linen Pant","Pleated Midi Skirt","Flare Jean","Utility Jogger","Wrap Skirt"],
    "Footwear":    ["Loafers","Espadrilles","High-Top Trainers","Mules","Ankle Boots"],
    "Accessories": ["Knit Beanie","Silk Scarf","Structured Crossbody","Baseball Cap","Bucket Hat"],
    "Knitwear":    ["Cable Knit Jumper","Rib-Knit Dress","Polo Neck","Knit Shorts","Open-Knit Top"],
    "Dresses":     ["Slip Dress","Shirt Dress","Wrap Dress","Midi Sundress","A-Line Dress"],
}
PRICE_RANGES = {
    "Outerwear":   (59.95, 249.95),
    "Tops":        (19.95, 75.95),
    "Bottoms":     (29.95, 119.95),
    "Footwear":    (49.95, 199.95),
    "Accessories": (9.95,  69.95),
    "Knitwear":    (49.95, 185.95),
    "Dresses":     (39.95, 99.95),
}
PREFIX = {
    "Outerwear":"OW","Tops":"TP","Bottoms":"BT","Footwear":"FW",
    "Accessories":"AC","Knitwear":"KN","Dresses":"DR",
}
COLOURS = ["Ecru","Sand","Navy","Olive","Terracotta","Stone","Black","Chalk","Slate","Forest"]

def snap(v):
    return round(round(v / 10) * 10 - 0.05, 2)

categories = list(EXTRA_PRODUCTS.keys())
counters   = {cat: 10 for cat in categories}  # start at 010 so no clash with hero IDs

fillers = []
for i in range(75):
    cat     = categories[i % len(categories)]
    counters[cat] += 1
    product = EXTRA_PRODUCTS[cat][counters[cat] % len(EXTRA_PRODUCTS[cat])]
    colour  = COLOURS[counters[cat] % len(COLOURS)]
    name    = f"{product} – {colour}"
    sku_id  = f"{PREFIX[cat]}-{counters[cat]:03d}"

    lo, hi         = PRICE_RANGES[cat]
    original_price = snap(random.uniform(lo, hi))
    weeks          = random.randint(1, 16)
    if weeks >= 8 and random.random() > 0.5:
        status        = "On Markdown"
        current_price = round(original_price * random.uniform(0.65, 0.85), 2)
    else:
        status        = "Active"
        current_price = original_price

    days_ago     = random.randint(0, weeks * 7)
    last_updated = (BASE_DT - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%S")

    fillers.append({
        "sku_id":         sku_id,
        "product_name":   name,
        "category":       cat,
        "original_price": original_price,
        "current_price":  current_price,
        "stock_quantity": random.randint(4, 80),
        "weeks_on_shelf": weeks,
        "store":          random.choice(STORES),
        "status":         status,
        "last_updated":   last_updated,
    })

all_skus = HERO
with open("data/inventory.json", "w") as f:
    json.dump(all_skus, f, indent=2)

print(f"Generated {len(all_skus)} SKUs → data/inventory.json")
