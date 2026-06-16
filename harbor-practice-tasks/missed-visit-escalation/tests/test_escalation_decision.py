from pathlib import Path


def test_escalation_decision_file_exists():
    output_file = Path("escalation_decision.md")
    assert output_file.exists(), "The agent must create escalation_decision.md"


def test_decision_is_escalate():
    content = Path("escalation_decision.md").read_text().upper()
    assert "ESCALATE" in content, "The decision must be ESCALATE"


def test_mentions_missed_visit():
    content = Path("escalation_decision.md").read_text().lower()
    assert "missed" in content, "The output must mention the missed visit"
    assert "v014" in content, "The output must mention visit V014"
    assert "c204" in content, "The output must mention client C204"


def test_mentions_medication_support():
    content = Path("escalation_decision.md").read_text().lower()
    assert "medication" in content, "The output must mention medication support"
    assert "support" in content, "The output must mention the visit type"


def test_mentions_same_day_escalation_rule():
    content = Path("escalation_decision.md").read_text().lower()
    assert "same-day" in content or "same day" in content, "The output must mention same-day escalation"
    assert "policy" in content or "risk" in content, "The output must connect the decision to the policy"


def test_includes_recommendation():
    content = Path("escalation_decision.md").read_text().lower()
    assert "recommendation" in content, "The output must include a recommendation section"