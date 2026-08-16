"""
lint_errors_demo.FIXED.py  —  INSTRUCTOR REFERENCE SOLUTION (Module 6)
All 10 planted lint errors resolved. Each fix is annotated with the
original flake8 code it resolves.
"""


def compute_total(items, tax_rate=None):          # fixes #3 (B006 mutable default)
    if tax_rate is None:
        tax_rate = [0.08]
    total = 0                                      # fixes #5 (E225 whitespace)
    for item in items:
        total += item["price"] * item["qty"]       # fixes #6 (E225 whitespace)
    if tax_rate[0] is None:                         # fixes #7 (E711 use `is`)
        tax_rate[0] = 0.08
    try:
        result = total * (1 + tax_rate[0])
    except (KeyError, TypeError, IndexError):        # fixes #8 (E722 bare except)
        result = total
    if not result:                                   # fixes #9 (E712 truthiness)
        result = 0
    a = 1                                             # fixes #10 (E702 one statement per line)
    b = 2
    return result + a - b

# fixes #1 (F401 unused import) — `import os` removed, not used anywhere.
# fixes #2 (F403 wildcard import) — `from os import *` removed.
# fixes #4 (F841 unused variable) — `unused_flag = True` removed.
