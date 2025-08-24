
from typing import Optional, Sequence, Tuple

def lead_time_gain(peects_actionable_utc: float, baseline_actionable_utc: float) -> float:
    """Return lead-time gain in hours (positive = earlier than baseline).
    Inputs are POSIX timestamps in seconds.
    """
    return (baseline_actionable_utc - peects_actionable_utc) / 3600.0

def false_alarm_ratio(false_alerts: int, total_alerts: int) -> float:
    if total_alerts <= 0:
        return 0.0
    return false_alerts / float(total_alerts)

def severity_hit_rate(y_true: Sequence[int], y_pred: Sequence[int], tol: int = 1) -> float:
    assert len(y_true) == len(y_pred)
    if len(y_true) == 0:
        return 0.0
    hits = sum(1 for t, p in zip(y_true, y_pred) if abs(t - p) <= tol)
    return hits / len(y_true)

def iou_polygon(poly_a: Sequence[Tuple[float, float]], poly_b: Sequence[Tuple[float, float]]) -> Optional[float]:
    """Placeholder IoU for polygons (lon, lat). Implement with shapely if available.
    For now, returns None; replace with actual area-based IoU when dependencies are allowed.
    """
    return None
