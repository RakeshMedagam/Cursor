# SKILL.md — INSTRUCTOR REFERENCE SOLUTION (Module 1b)
# Example reusable skill: "Add a new REST endpoint"

## Name
add-rest-endpoint

## Trigger
Use when asked to add a new read or write REST endpoint to this service.

## Description
Scaffolds a new Flask-style endpoint: route handler, request validation,
and a matching test file. Never touches existing endpoints or UAT-locked
modules.

## Constraints (NEVER_MODIFY)
- app/baseline_forecast.py
- app/data_ingestion.py
- app/shared_utils.py
- app/auth/session.py
- app/cart.py
- app/checkout.py
- app/payments.py

## Steps
1. Confirm the endpoint's method, path, request schema, and response schema
   with the requester before generating anything.
2. Create the route handler in a new or existing *non-locked* module.
3. Validate inputs explicitly; return a 400 with a clear message on
   invalid input rather than letting an exception propagate.
4. Generate a test file covering: happy path, invalid input, and one edge
   case relevant to the endpoint's domain.
5. Run the full test suite and confirm no UAT-locked file appears in
   `git diff --name-only`.

## Example invocation
"Using the add-rest-endpoint skill, add a GET /users/<id>/orders endpoint
that returns a user's last 10 orders."
