"""Matching test file — written BEFORE the implementation, per the EDD workflow (Module 10)."""
from solutions.promotion_uplift_SOLUTION import estimate_uplift  # adjust import to your module path


def test_uplift_positive_when_actual_exceeds_baseline():
    history = [{"date": "2026-02-01", "units": 10}, {"date": "2026-02-02", "units": 10}]
    promo_units = {"2026-02-10": 40}
    result = estimate_uplift("SKU1", "CL1", history, promo_units, "2026-02-10", "2026-02-10")
    assert result["uplift_percent"] > 0
    assert result["cannibalisation_flag"] is False


def test_flags_cannibalisation_when_uplift_is_flat():
    history = [{"date": "2026-02-01", "units": 20}]
    promo_units = {"2026-02-10": 20}
    result = estimate_uplift("SKU1", "CL1", history, promo_units, "2026-02-10", "2026-02-10")
    assert result["cannibalisation_flag"] is True


def test_handles_zero_baseline_without_crashing():
    result = estimate_uplift("SKU1", "CL1", [], {}, "2026-02-10", "2026-02-10")
    assert result["baseline_units"] == 0
    assert result["uplift_percent"] == 0.0
