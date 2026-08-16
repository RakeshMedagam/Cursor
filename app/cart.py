"""
cart.py  —  UAT-LOCKED
Shopping cart logic. Signed off UAT 2024-Q3. DO NOT MODIFY during Day 1-3
exercises — used in the Module 5 "wishlist feature, cart untouched" scenario.
"""
from app.shared_utils import round_currency


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, sku: str, quantity: int, unit_price: float):
        self.items.append({"sku": sku, "quantity": quantity, "unit_price": unit_price})

    def remove_item(self, sku: str):
        self.items = [i for i in self.items if i["sku"] != sku]

    def total(self) -> float:
        return round_currency(sum(i["quantity"] * i["unit_price"] for i in self.items))
