"""Model size + inference speed benchmarks. Used by Notebook 3."""
from __future__ import annotations
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass
class BenchmarkResult:
    config: str
    disk_size_mb: float
    tokens_per_second: float
    first_token_latency_ms: float
    device: str       # "cuda" | "cpu"
    peak_vram_mb: float = 0.0
    peak_ram_mb: float = 0.0


def measure_disk_size(path: Path) -> float:
    """Return total MB on disk (single file or directory recursively)."""
    p = Path(path)
    if p.is_file():
        return p.stat().st_size / 1024 / 1024
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file()) / 1024 / 1024


def benchmark_generation(
    generate_fn,                      # callable: (prompt, max_new_tokens) -> (output_text, n_tokens)
    prompts: list[str],
    max_new_tokens: int = 32,
    warmup: int = 1,
) -> dict:
    """Benchmark avg tokens/sec and first-token latency."""
    # Warmup
    for _ in range(warmup):
        generate_fn(prompts[0], max_new_tokens)

    total_tokens = 0
    total_time = 0.0
    first_token_latencies = []

    for prompt in prompts:
        t0 = time.perf_counter()
        _, n_out = generate_fn(prompt, max_new_tokens)
        dt = time.perf_counter() - t0

        # Approximate first-token latency (full request time / n_tokens ratio)
        # Real FTL needs streaming; this is a proxy for "perceived latency"
        first_token_latencies.append(dt / max(n_out, 1) * 1000)
        total_tokens += n_out
        total_time += dt

    return {
        "tokens_per_second": total_tokens / total_time if total_time > 0 else 0,
        "first_token_latency_ms": sum(first_token_latencies) / len(first_token_latencies),
        "total_tokens": total_tokens,
        "total_time_s": total_time,
    }


def pi_feasibility_check(model_size_mb: float, pi_ram_gb: int = 4) -> dict:
    """Return theoretical Pi deployment analysis."""
    headroom_mb = pi_ram_gb * 1024 - model_size_mb - 512   # reserve ~500MB for OS
    return {
        "model_size_mb": model_size_mb,
        "pi_ram_gb": pi_ram_gb,
        "fits": model_size_mb < pi_ram_gb * 1024 - 512,
        "headroom_mb": headroom_mb,
        "note": (
            f"Model uses {model_size_mb:.0f} MB of {pi_ram_gb*1024} MB Pi RAM; "
            f"{headroom_mb:.0f} MB free after OS reserve."
        ),
    }
