from pathlib import Path


def test_release_decision_file_exists():
    output_file = Path("release_decision.md")
    assert output_file.exists(), "The agent must create release_decision.md"


def test_decision_is_not_ready():
    content = Path("release_decision.md").read_text().upper()
    assert "NOT_READY" in content, "The decision must be NOT_READY"


def test_mentions_failed_payment_test():
    content = Path("release_decision.md").read_text().lower()
    assert "payment" in content
    assert "failed" in content


def test_mentions_open_blocker_issue():
    content = Path("release_decision.md").read_text().lower()
    assert "blocker" in content
    assert "open" in content


def test_mentions_checklist_rule():
    content = Path("release_decision.md").read_text().lower()
    assert "checklist" in content or "must not be approved" in content


def test_includes_recommendation():
    content = Path("release_decision.md").read_text().lower()
    assert "recommendation" in content, "The output must include a recommendation section"