"""
payments.py  —  UAT-LOCKED
Payment processing (mock/synthetic — no real payment gateway). Signed off
UAT 2024-Q1. DO NOT MODIFY during Day 1-3 exercises — this is the file
used in the Module 1 "payments bug-fix ticket" scenario.
"""


class PaymentError(Exception):
    pass


def process_payment(amount: float, method: str) -> dict:
    if amount <= 0:
        raise PaymentError("Amount must be positive")
    if method not in ("card", "wallet", "bank_transfer"):
        raise PaymentError(f"Unsupported payment method: {method}")
    return {"status": "success", "amount": amount, "method": method}
