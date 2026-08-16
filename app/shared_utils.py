"""
shared_utils.py  —  UAT-LOCKED
Used by baseline_forecast.py, data_ingestion.py, and checkout.py.
Signed off in UAT cycle 2024-Q3. Do not modify without a full regression run
across all three consuming modules.
"""
from datetime import datetime, timedelta


def parse_iso_date(value: str) -> datetime:
    """Parse an ISO-8601 date string (YYYY-MM-DD) into a datetime object."""
    return datetime.strptime(value, "%Y-%m-%d")


def date_range(start: str, end: str):
    """Yield each ISO date string between start and end, inclusive."""
    d0 = parse_iso_date(start)
    d1 = parse_iso_date(end)
    for i in range((d1 - d0).days + 1):
        yield (d0 + timedelta(days=i)).strftime("%Y-%m-%d")


def round_currency(amount: float) -> float:
    """Round a currency amount to 2 decimal places using standard rounding."""
    return round(amount + 1e-9, 2)


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Divide two numbers, returning `default` instead of raising on divide-by-zero."""
    if denominator == 0:
        return default
    return numerator / denominator
