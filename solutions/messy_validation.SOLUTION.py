"""
messy_validation.SOLUTION.py  —  INSTRUCTOR REFERENCE SOLUTION (Module 6)
Duplicated validation logic extracted into one shared function. Public
behaviour of all three original functions is unchanged (same UAT contract):
same inputs still produce the same (bool, error_message) outputs.
"""


def _validate_core_fields(order):
    """Shared validation extracted from validate_new_order / validate_order_update
    / validate_bulk_order. Returns (True, None) or (False, error_message)."""
    if "sku" not in order or not order["sku"]:
        return False, "Missing SKU"
    if "quantity" not in order or order["quantity"] <= 0:
        return False, "Quantity must be positive"
    if "store_id" not in order or not order["store_id"]:
        return False, "Missing store ID"
    return True, None


def validate_new_order(order):
    return _validate_core_fields(order)


def validate_order_update(order):
    ok, err = _validate_core_fields(order)
    if not ok:
        return ok, err
    if "update_reason" not in order or not order["update_reason"]:
        return False, "Missing update reason"
    return True, None


def validate_bulk_order(orders):
    for order in orders:
        ok, err = _validate_core_fields(order)
        if not ok:
            return ok, err
    return True, None
