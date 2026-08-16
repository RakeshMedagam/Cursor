"""
messy_validation.py  —  editable
Order/customer validation with duplicated logic across functions.
Stands in for the Module 6 "400-line module cleanup" scenario — the same
validation block is copy-pasted three times below. Refactor target: extract
a single shared validator without changing any function's public behaviour
(the UAT contract — same inputs must produce the same outputs/errors).
"""


def validate_new_order(order):
    if "sku" not in order or not order["sku"]:
        return False, "Missing SKU"
    if "quantity" not in order or order["quantity"] <= 0:
        return False, "Quantity must be positive"
    if "store_id" not in order or not order["store_id"]:
        return False, "Missing store ID"
    return True, None


def validate_order_update(order):
    if "sku" not in order or not order["sku"]:
        return False, "Missing SKU"
    if "quantity" not in order or order["quantity"] <= 0:
        return False, "Quantity must be positive"
    if "store_id" not in order or not order["store_id"]:
        return False, "Missing store ID"
    if "update_reason" not in order or not order["update_reason"]:
        return False, "Missing update reason"
    return True, None


def validate_bulk_order(orders):
    for order in orders:
        if "sku" not in order or not order["sku"]:
            return False, "Missing SKU"
        if "quantity" not in order or order["quantity"] <= 0:
            return False, "Quantity must be positive"
        if "store_id" not in order or not order["store_id"]:
            return False, "Missing store ID"
    return True, None
