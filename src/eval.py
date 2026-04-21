"""Evaluation metrics & harness. Used by Notebooks 2, 3, 4."""
from __future__ import annotations
import re
import time
from collections.abc import Callable
from dataclasses import dataclass


ICD10_CODE_RE = re.compile(r"^[A-TV-Z][0-9][A-Z0-9](?:\.[A-Z0-9]{1,4})?$")


def exact_match(pred: str, gold: str) -> bool:
    return pred.strip().upper() == gold.strip().upper()


def category_match(pred: str, gold: str) -> bool:
    return pred.strip().upper()[:3] == gold.strip().upper()[:3]


def is_valid_format(pred: str) -> bool:
    return bool(ICD10_CODE_RE.match(pred.strip().upper()))


def is_valid_code(pred: str, codebook: set[str]) -> bool:
    return pred.strip().upper() in codebook


@dataclass
class EvalResult:
    config: str
    exact_match: float
    category_match: float
    valid_format: float
    valid_in_codebook: float
    avg_latency_ms: float
    n: int


def evaluate(predict_fn: Callable[[str], str],
             test_examples: list[dict],
             codebook: set[str],
             config_name: str) -> EvalResult:
    """Run predict_fn across all test examples and aggregate metrics."""
    hits_exact = hits_cat = hits_fmt = hits_codebook = 0
    total_ms = 0.0

    for ex in test_examples:
        t0 = time.perf_counter()
        pred = predict_fn(ex["input"])
        total_ms += (time.perf_counter() - t0) * 1000

        hits_exact    += exact_match(pred, ex["gold"])
        hits_cat      += category_match(pred, ex["gold"])
        hits_fmt      += is_valid_format(pred)
        hits_codebook += is_valid_code(pred, codebook)

    n = len(test_examples)
    return EvalResult(
        config=config_name,
        exact_match=hits_exact / n,
        category_match=hits_cat / n,
        valid_format=hits_fmt / n,
        valid_in_codebook=hits_codebook / n,
        avg_latency_ms=total_ms / n,
        n=n,
    )
