"""
checkout.py  —  UAT-LOCKED
Checkout flow. Signed off UAT 2024-Q3. DO NOT MODIFY during Day 1-3 exercises
— used in the Module 5 discount-calculation scenario ("without touching
the existing checkout flow").
"""
from app.cart import Cart
from app.shared_utils import round_currency


def checkout(cart: Cart, tax_rate: float = 0.08) -> dict:
    subtotal = cart.total()
    tax = round_currency(subtotal * tax_rate)
    return {
        "subtotal": subtotal,
        "tax": tax,
        "total": round_currency(subtotal + tax),
        "item_count": len(cart.items),
    }
