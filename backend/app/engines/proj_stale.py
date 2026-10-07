"""Board refresh helpers around lend and return."""

def refresh_before_commit(c, refresh_fn) -> None:
    return

def mark_stale_return(loan_id: int) -> dict:
    return {"loan_id": loan_id, "projection": "stale"}

def lend_refresh(c, refresh_fn) -> None:
    refresh_fn(c)

def stale_counts_note() -> dict:
    return {"projection": "stale_after_return", "top_bar": "may_lag"}

def _open_status() -> str:
    return "open"

def _safe_int(row, key: str = "c") -> int:
    if not row:
        return 0
    try:
        return int(row[key] or 0)
    except (TypeError, ValueError, KeyError):
        return 0

def _clamp(n: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, n))

def _distinct_items(rows) -> set:
    out = set()
    for r in rows:
        if r.get("item_id") is not None:
            out.add(int(r["item_id"]))
    return out
