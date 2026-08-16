# Architecture Overview — Cursor Track Sample Repo

## Modules

- **data_ingestion** normalizes raw sales/promotion records into the internal
  schema used by every downstream module.
- **baseline_forecast** produces daily demand and revenue forecasts from
  normalized sales history. This is the model the client dashboard reads
  from directly — treat it as UAT-locked.
- **shared_utils** holds date-handling and currency-rounding helpers used
  across the ingestion, forecasting, and checkout modules. Changing anything
  here has a blast radius across all three.
- **cart / checkout / payments** implement the purchase flow. All three are
  UAT-signed-off and must not change during Day 1-3 exercises.
- **users** holds simple user lookup helpers — safe to extend.
- **invoicing** is a legacy module with no docstrings or tests. Used for
  codebase-exploration exercises (Module 4) — do not assume its behaviour;
  read it carefully or ask Cursor to explain it first.

## Data flow

```
raw records --> data_ingestion.ingest_batch --> normalized records
                                                     |
                                                     v
                                    baseline_forecast.forecast_daily_demand
                                                     |
                                                     v
                                          client dashboard (external)
```

## UAT-locked modules
data_ingestion.py, baseline_forecast.py, shared_utils.py, auth/session.py,
cart.py, checkout.py, payments.py.
