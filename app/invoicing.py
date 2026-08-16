import app.shared_utils as su


def gen(o, r=0.08, d=None):
    s = sum(i["q"] * i["p"] for i in o["items"])
    if d:
        s = s - (s * d)
    t = su.round_currency(s * r)
    return {"ref": o["id"], "sub": su.round_currency(s), "tax": t, "tot": su.round_currency(s + t)}


def batch(orders, r=0.08):
    out = []
    for o in orders:
        try:
            out.append(gen(o, r))
        except Exception:
            pass
    return out
