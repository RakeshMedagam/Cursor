"""
lint_errors_demo.py  —  editable
Contains 10 intentionally planted lint errors for Module 6 exercises.
Instructor: see /solutions/lint_errors_demo.FIXED.py for the corrected
version with each fix annotated. Do not share with trainees before the
exercise.
"""
import os                                    # 1. unused import (F401)
from os import *                             # 2. wildcard import (F403)


def compute_total(items, tax_rate=[0.08]):   # 3. mutable default argument (B006)
    unused_flag = True                       # 4. unused variable (F841)
    total=0                                  # 5. missing whitespace around operator (E225)
    for item in items:
        total += item["price"]*item["qty"]   # 6. missing whitespace around operator (E225)
    if tax_rate[0] == None:                  # 7. comparison to None with == instead of is (E711)
        tax_rate[0] = 0.08
    try:
        result = total * (1 + tax_rate[0])
    except:                                  # 8. bare except (E722)
        result = total
    if result == True:                       # 9. comparison to True with == instead of truthiness (E712)
        result = 0
    a = 1; b = 2                             # 10. multiple statements on one line (E702)
    return result + a - b
