"""
buggy_service.FIXED.py  —  INSTRUCTOR REFERENCE SOLUTION (Module 7)
Each fix below is annotated with the root cause. Compare against
app/buggy_service.py to see the diff.
"""


def apply_discount(items, discount_percent=None):
    # FIX 1: use None as the default, create a fresh list inside the
    # function. Root cause: mutable default arguments are created once at
    # function-definition time and reused across every call.
    if discount_percent is None:
        discount_percent = []
    results = []
    pct = discount_percent[-1] if discount_percent else 0
    for item in items:
        price = item["price"] * (1 - pct / 100)
        results.append({"sku": item["sku"], "price": round(price, 2)})
    return results


def get_low_stock_skus(inventory, threshold=10):
    # FIX 2: use <= so items exactly at the threshold are included, matching
    # the spec ("at or below threshold"). Root cause: off-by-one boundary.
    return [sku for sku, qty in inventory.items() if qty <= threshold]


def average_daily_sales(sales_by_day):
    total = sum(sales_by_day.values())
    count = len(sales_by_day)
    # FIX 3: guard against division by zero when the input dict is empty.
    if count == 0:
        return 0.0
    return total / count


def eligible_for_promo(item, min_margin=0.15):
    margin = (item["price"] - item["cost"]) / item["price"]
    # FIX 4: use >= so items exactly at the minimum margin are included.
    return margin >= min_margin


def merge_promo_flags(base_items, promo_skus):
    merged = []
    for item in base_items:
        # FIX 5: copy the dict before mutating it, so the original
        # base_items list passed in by the caller is never modified as a
        # side effect. Root cause: `item` and `flagged` referenced the same
        # dict object, so "flagged = item" did not create a real copy.
        flagged = dict(item)
        flagged["on_promo"] = flagged["sku"] in promo_skus
        merged.append(flagged)
    return merged
