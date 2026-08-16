"""
buggy_service.py  —  editable
Inventory / promotion-eligibility helper service.
Contains 5 intentionally planted bugs for Module 7 debugging exercises.
Instructor: see /solutions/buggy_service.FIXED.py for the fix + root cause
of each. Do not share the solutions file with trainees before the exercise.
"""


def apply_discount(items, discount_percent=[]):
    # BUG 1: mutable default argument — a list is reused across calls and
    # will silently accumulate state between invocations.
    discount_percent.append(discount_percent[-1] if discount_percent else 0)
    results = []
    for item in items:
        price = item["price"] * (1 - discount_percent[-1] / 100)
        results.append({"sku": item["sku"], "price": round(price, 2)})
    return results


def get_low_stock_skus(inventory, threshold=10):
    # BUG 2: off-by-one — uses `<` instead of `<=`, so items exactly at the
    # threshold are missed even though the spec says "at or below threshold".
    return [sku for sku, qty in inventory.items() if qty < threshold]


def average_daily_sales(sales_by_day):
    total = sum(sales_by_day.values())
    count = len(sales_by_day)
    # BUG 3: divide-by-zero not handled when sales_by_day is empty.
    return total / count


def eligible_for_promo(item, min_margin=0.15):
    margin = (item["price"] - item["cost"]) / item["price"]
    # BUG 4: wrong comparison operator — should be >= to include items
    # exactly at the minimum margin threshold, but uses > and silently
    # excludes them (mirrors a real off-by-boundary defect).
    return margin > min_margin


def merge_promo_flags(base_items, promo_skus):
    merged = []
    for item in base_items:
        flagged = item
        # BUG 5: variable shadowing — reassigns `item` inside the loop
        # instead of creating a new dict, so the original list `base_items`
        # gets mutated as a side effect (the function looks pure but isn't).
        item["on_promo"] = item["sku"] in promo_skus
        merged.append(flagged)
    return merged
