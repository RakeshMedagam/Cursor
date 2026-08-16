# API Reference (Internal) — Cursor Track Sample Repo

## `data_ingestion.normalize_sales_record(raw: dict) -> dict`
Normalizes a raw sales record. Required fields: `sku`, `store_id`, `date`,
`units_sold`. Raises `IngestionError` if any are missing or the date is not
valid ISO-8601 (YYYY-MM-DD).

## `baseline_forecast.forecast_daily_demand(sku, store_cluster, history, start, end) -> dict`
Returns `{"sku", "store_cluster", "forecast": {date: units}}` using a
rolling-average model with day-of-week seasonality. `history` must be a list
of `{"date", "units"}` records.

## `baseline_forecast.forecast_revenue(sku, store_cluster, history, unit_price, start, end) -> float`
Returns forecasted total revenue for the window, rounded to 2 decimal places.

## `shared_utils`
- `parse_iso_date(value) -> datetime`
- `date_range(start, end) -> generator[str]`
- `round_currency(amount) -> float`
- `safe_divide(numerator, denominator, default=0.0) -> float`

## `users.get_user(user_id) -> dict | None`
## `users.list_users_by_region(region) -> list[dict]`

## `cart.Cart` — `.add_item(sku, quantity, unit_price)`, `.remove_item(sku)`, `.total() -> float`
## `checkout.checkout(cart, tax_rate=0.08) -> dict`
## `payments.process_payment(amount, method) -> dict` — methods: card, wallet, bank_transfer
