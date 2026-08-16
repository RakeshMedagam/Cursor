"""
wishlist.SOLUTION.py  —  INSTRUCTOR REFERENCE SOLUTION (Module 5, Module 8)
New "wishlist" feature, generated to satisfy the scenario: add a feature
without touching the UAT-locked cart.py or checkout.py. Only imports from
them read-only (does not modify).
"""
from typing import Optional


class Wishlist:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self._skus: set[str] = set()

    def add(self, sku: str) -> None:
        self._skus.add(sku)

    def remove(self, sku: str) -> None:
        self._skus.discard(sku)

    def contains(self, sku: str) -> bool:
        return sku in self._skus

    def items(self) -> list[str]:
        return sorted(self._skus)


def move_to_cart(wishlist: "Wishlist", sku: str, cart, unit_price: float, quantity: int = 1) -> Optional[str]:
    """
    Move a wishlist item into the (UAT-locked) Cart via its existing public
    API only — add_item(). Does not modify cart.py itself.
    """
    if not wishlist.contains(sku):
        return f"SKU {sku} is not in the wishlist"
    cart.add_item(sku, quantity, unit_price)
    wishlist.remove(sku)
    return None
