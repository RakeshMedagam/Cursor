"""
baseline_forecast.py  —  UAT-LOCKED
Core demand forecasting model. Feeds the client-facing dashboard directly.
Signed off in UAT cycle 2024-Q3. Any change requires a full regression run
and dashboard team sign-off. DO NOT MODIFY during Day 1-3 exercises.
"""
from app.shared_utils import date_range, round_currency, safe_divide

# Simplified synthetic "model": rolling average of historical daily sales,
# with a mild day-of-week seasonality multiplier. This stands in for a real
# forecasting model for training purposes.
_SEASONALITY = {0: 0.95, 1: 0.97, 2: 1.00, 3: 1.02, 4: 1.10, 5: 1.25, 6: 1.15}


def forecast_daily_demand(sku: str, store_cluster: str, history: list, start: str, end: str) -> dict:
    """
    Forecast baseline daily demand for a SKU/store cluster over a date range.

    Args:
        sku: SKU identifier.
        store_cluster: store cluster identifier.
        history: list of {"date": "YYYY-MM-DD", "units": int} historical sales records.
        start: ISO start date of the forecast window.
        end: ISO end date of the forecast window.

    Returns:
        dict mapping each date in the range to a forecasted unit count.
    """
    if not history:
        base_rate = 0.0
    else:
        total_units = sum(h["units"] for h in history)
        base_rate = safe_divide(total_units, len(history))

    forecast = {}
    for i, d in enumerate(date_range(start, end)):
        import datetime as _dt
        weekday = _dt.datetime.strptime(d, "%Y-%m-%d").weekday()
        multiplier = _SEASONALITY.get(weekday, 1.0)
        forecast[d] = round(base_rate * multiplier, 1)
    return {
        "sku": sku,
        "store_cluster": store_cluster,
        "forecast": forecast,
    }


def forecast_revenue(sku: str, store_cluster: str, history: list, unit_price: float, start: str, end: str) -> float:
    """Forecast total revenue for a SKU/store cluster over a date range."""
    result = forecast_daily_demand(sku, store_cluster, history, start, end)
    total_units = sum(result["forecast"].values())
    return round_currency(total_units * unit_price)
