# Cursor Track — Shared Sample Repository

This is the shared sample codebase used across Day 1, Day 2, and Day 3 of the
U-Next Cursor Training programme. It is a small, synthetic Retail/CPG-style
analytics service (in the spirit of Tredence's engagement domain) — no real
client code or data.

## Structure

```
app/
  baseline_forecast.py     UAT-LOCKED  — core demand forecasting logic
  data_ingestion.py        UAT-LOCKED  — feeds the client-facing dashboard
  shared_utils.py          UAT-LOCKED  — used by 3+ signed-off modules
  auth/session.py          UAT-LOCKED  — session/auth handling
  cart.py                  UAT-LOCKED  — shopping cart logic
  checkout.py              UAT-LOCKED  — checkout flow
  payments.py              UAT-LOCKED  — payment processing
  users.py                 editable    — user lookup/profile helpers
  invoicing.py             editable    — legacy, undocumented module (M4 target)
  buggy_service.py         editable    — 5 planted bugs (M7 debugging target)
  lint_errors_demo.py      editable    — 10 planted lint errors (M6 target)
  messy_validation.py      editable    — duplicated validation logic (M6 refactor target)
docs/
  api_reference.md         for @docs exercises
  architecture.md          for @docs / @codebase exercises
tests/
  test_baseline_forecast.py  existing regression tests (UAT baseline)
  test_users.py               starter tests
.cursorrules                skeleton — trainees fill this in during M2/M3
.github/workflows/ci.yml    skeleton pipeline — trainees complete during M11
```

## UAT-locked files (do not modify during Day 1–3 exercises)
- `app/baseline_forecast.py`
- `app/data_ingestion.py`
- `app/shared_utils.py`
- `app/auth/session.py`
- `app/cart.py`
- `app/checkout.py`
- `app/payments.py`

## Setup
```
pip install -r requirements.txt
pytest tests/
```

See `/solutions` (instructor copy only — do not distribute to trainees before
the relevant module) for reference answers to generation-heavy exercises.
