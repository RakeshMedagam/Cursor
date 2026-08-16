"""
promotion_uplift.SOLUTION.py  —  INSTRUCTOR REFERENCE SOLUTION (Day 4 Capstone)
Reference implementation for the Tredence-flavoured capstone brief.
Reads from baseline_forecast.py's output ONLY through its public function
(forecast_daily_demand) — never modifies it.
"""
from app.baseline_forecast import forecast_daily_demand
from app.shared_utils import safe_divide


def estimate_uplift(sku: str, store_cluster: str, history: list,
                     promo_units: dict, start: str, end: str) -> dict:
    """
    Estimate promotion uplift % and a cannibalisation flag for a SKU/store
    cluster/promo window, using the existing baseline forecast as the
    counterfactual ("what would have sold anyway").

    Args:
        promo_units: dict mapping date -> actual units sold during the promo.

    Returns:
        dict with uplift_percent, cannibalisation_flag, and the underlying
        baseline/actual totals for transparency.
    """
    baseline = forecast_daily_demand(sku, store_cluster, history, start, end)
    baseline_total = sum(baseline["forecast"].values())
    actual_total = sum(promo_units.get(d, 0) for d in baseline["forecast"])

    uplift_percent = safe_divide(actual_total - baseline_total, baseline_total, default=0.0) * 100

    # Simple heuristic: if actual sales barely exceed baseline (<5% uplift)
    # despite a promotion running, flag likely cannibalisation of future
    # full-price sales rather than genuine incremental demand.
    cannibalisation_flag = uplift_percent < 5.0

    return {
        "sku": sku,
        "store_cluster": store_cluster,
        "baseline_units": round(baseline_total, 1),
        "actual_units": actual_total,
        "uplift_percent": round(uplift_percent, 1),
        "cannibalisation_flag": cannibalisation_flag,
    }
