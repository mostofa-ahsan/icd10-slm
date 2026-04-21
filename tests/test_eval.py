"""Smoke tests — run before committing to catch obvious breakage."""
import pytest
from src.eval import exact_match, category_match, is_valid_format


def test_exact_match():
    assert exact_match("E11.9", "E11.9")
    assert exact_match("e11.9", "E11.9")
    assert not exact_match("E11.9", "E11.8")


def test_category_match():
    assert category_match("E11.9", "E11.8")
    assert not category_match("E11.9", "E10.9")


def test_valid_format():
    assert is_valid_format("E11.9")
    assert is_valid_format("J45.909")
    assert is_valid_format("A00")
    assert not is_valid_format("11.9")
    assert not is_valid_format("foo")
