from pathlib import Path


def test_release_decision_file_exists():
    output_file = Path("release_decision.md")
    assert output_file.exists(), "The agent must create release_decision.md"


def test_decision_is_not_ready():
    content = Path("release_decision.md").read_text().upper()
    assert "NOT_READY" in content, "The decision must be NOT_READY"


def test_mentions_failed_payment_integration_test():
    content = Path("release_decision.md").read_text().lower()
    assert "payment" in content, "The output must mention payment evidence"
    assert "integration" in content, "The output must mention the integration test context"
    assert "failed" in content, "The output must state that the payment integration test failed"


def test_mentions_specific_open_blocker_issue():
    content = Path("release_decision.md").read_text().lower()
    assert "issue-127" in content, "The output must mention ISSUE-127"
    assert "blocker" in content, "The output must mention that ISSUE-127 is a blocker"
    assert "open" in content, "The output must mention that ISSUE-127 is open"


def test_mentions_checklist_rule():
    content = Path("release_decision.md").read_text().lower()
    assert "checklist" in content or "must not be approved" in content


def test_includes_recommendation():
    content = Path("release_decision.md").read_text().lower()
    assert "recommendation" in content, "The output must include a recommendation section"


def test_mentions_duplicate_transaction_risk():
    content = Path("release_decision.md").read_text().lower()
    assert "duplicate" in content, "The output must mention the duplicate transaction risk"
    assert "transaction" in content, "The output must mention transaction evidence"