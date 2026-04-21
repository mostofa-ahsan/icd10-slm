"""Test the document → phrases splitter."""
from src.note_chunker import chunk_note


def test_basic_chunking():
    note = """Chief Complaint: 55yo M with chest pain.
PMH: Hypertension; Type 2 Diabetes.
Assessment:
  1. Acute coronary syndrome
  2. Uncontrolled hypertension
"""
    phrases = chunk_note(note)
    assert len(phrases) >= 3
    # Should split sections and produce codable phrases
    assert any("chest pain" in p.lower() for p in phrases)
    assert any("coronary" in p.lower() for p in phrases)
    assert any("type 2 diabetes" in p.lower() for p in phrases)


def test_dedup():
    note = "Chief complaint: cough. Cough. Cough."
    phrases = chunk_note(note)
    cough_phrases = [p for p in phrases if p.lower() == "cough"]
    assert len(cough_phrases) <= 1  # deduped


def test_respects_length_limits():
    note = "a. " + "x" * 500  # one tiny + one giant
    phrases = chunk_note(note, min_len=4, max_len=100)
    for p in phrases:
        assert 4 <= len(p) <= 100
