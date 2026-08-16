"""
data_ingestion.py  —  UAT-LOCKED
Ingests raw sales/promotion records and normalizes them for downstream
modules (baseline_forecast.py, dashboard export). Signed off UAT 2024-Q3.
DO NOT MODIFY during Day 1-3 exercises.
"""
from app.shared_utils import parse_iso_date


class IngestionError(Exception):
    pass


def normalize_sales_record(raw: dict) -> dict:
    """
    Normalize a raw sales record into the internal schema.
    Raises IngestionError on missing required fields.
    """
    required = ("sku", "store_id", "date", "units_sold")
    missing = [f for f in required if f not in raw]
    if missing:
        raise IngestionError(f"Missing required fields: {missing}")

    parse_iso_date(raw["date"])  # validates date format, raises on bad input

    return {
        "sku": str(raw["sku"]).strip().upper(),
        "store_id": str(raw["store_id"]).strip(),
        "date": raw["date"],
        "units": int(raw["units_sold"]),
        "promo_flag": bool(raw.get("promo_flag", False)),
    }


def ingest_batch(raw_records: list) -> list:
    """Normalize a batch of raw sales records, skipping and logging invalid ones."""
    clean = []
    errors = []
    for r in raw_records:
        try:
            clean.append(normalize_sales_record(r))
        except IngestionError as e:
            errors.append({"record": r, "error": str(e)})
    return clean
