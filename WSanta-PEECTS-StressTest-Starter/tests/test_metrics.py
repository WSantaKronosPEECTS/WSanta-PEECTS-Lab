
from pipelines.common.eval_metrics import lead_time_gain, false_alarm_ratio, severity_hit_rate

def test_lead_time_gain():
    assert lead_time_gain(0, 3600) == 1.0

def test_false_alarm_ratio():
    assert false_alarm_ratio(1, 4) == 0.25

def test_severity_hit_rate():
    assert severity_hit_rate([1,2,3], [1,3,5], tol=1) == 1.0  # all within ±1
