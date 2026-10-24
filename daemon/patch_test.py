import json

WINDOW_PAYLOADS = {"primary": "cxd", "secondary": "cxw"}

def _tokens(rate_limits: dict | None, now: float) -> dict[str, int]:
    starts = {}
    for window, key in WINDOW_PAYLOADS.items():
        limit = (rate_limits or {}).get(window)
        try:
            starts[key] = float(limit["resets_at"]) - float(limit["window_minutes"]) * 60
        except (KeyError, TypeError, ValueError):
            if rate_limits is not None:
                starts[key] = now - (300 * 60 if key == "cxd" else 10080 * 60)
            continue
    return starts

print(_tokens({"limit_id": "premium"}, 10000000))
