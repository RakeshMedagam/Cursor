"""Existing regression tests — UAT baseline. Must stay green throughout Day 1-3."""
from app.baseline_forecast import forecast_daily_demand, forecast_revenue


def test_forecast_daily_demand_empty_history():
    result = forecast_daily_demand("SKU1", "CL1", [], "2026-01-01", "2026-01-02")
    assert result["forecast"]["2026-01-01"] == 0.0
    assert result["forecast"]["2026-01-02"] == 0.0


def test_forecast_daily_demand_basic():
    history = [{"date": "2026-01-01", "units": 10}, {"date": "2026-01-02", "units": 20}]
    result = forecast_daily_demand("SKU1", "CL1", history, "2026-01-05", "2026-01-05")
    assert result["sku"] == "SKU1"
    assert "2026-01-05" in result["forecast"]


def test_forecast_revenue():
    history = [{"date": "2026-01-01", "units": 10}]
    revenue = forecast_revenue("SKU1", "CL1", history, unit_price=5.0, start="2026-01-01", end="2026-01-01")
    assert revenue >= 0
