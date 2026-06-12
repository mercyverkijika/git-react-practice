from pathlib import Path


def test_report_readiness_file_exists():
    output_file = Path("report_readiness_decision.md")
    assert output_file.exists(), "The agent must create report_readiness_decision.md"


def test_decision_is_not_ready():
    content = Path("report_readiness_decision.md").read_text().upper()
    assert "NOT_READY" in content, "The decision must be NOT_READY"


def test_mentions_missing_actual_end_timestamps():
    content = Path("report_readiness_decision.md").read_text().lower()
    assert "actual_end" in content, "The output must mention missing actual_end timestamps"
    assert "v002" in content, "The output must mention visit V002"
    assert "v005" in content, "The output must mention visit V005"


def test_mentions_duplicate_visit_record():
    content = Path("report_readiness_decision.md").read_text().lower()
    assert "duplicate" in content, "The output must mention the duplicate visit record"
    assert "v004" in content, "The output must mention duplicate visit V004"


def test_mentions_reporting_rule():
    content = Path("report_readiness_decision.md").read_text().lower()
    assert "must not be sent" in content or "not send" in content
    assert "critical" in content or "duplicate" in content


def test_includes_recommendation():
    content = Path("report_readiness_decision.md").read_text().lower()
    assert "recommendation" in content, "The output must include a recommendation section"