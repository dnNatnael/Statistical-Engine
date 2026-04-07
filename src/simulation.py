"""Monte Carlo simulation utilities for applied probability demos."""

from __future__ import annotations

import random
from typing import Dict, Iterable, List, Tuple


def simulate_crashes(days: int, crash_probability: float = 0.045) -> Tuple[int, float]:
    """Simulate daily server crashes and return (total_crashes, crash_rate)."""
    if not isinstance(days, int) or days <= 0:
        raise ValueError("days must be a positive integer.")
    if not (0.0 <= crash_probability <= 1.0):
        raise ValueError("crash_probability must be in [0, 1].")

    crashes = 0
    for _ in range(days):
        if random.random() < crash_probability:
            crashes += 1

    return crashes, crashes / days


def run_crash_scenarios(day_counts: Iterable[int]) -> List[Dict[str, float]]:
    """Run simulations for multiple day counts."""
    results: List[Dict[str, float]] = []
    for days in day_counts:
        crashes, simulated_probability = simulate_crashes(days)
        results.append(
            {
                "days": float(days),
                "crashes": float(crashes),
                "simulated_probability": simulated_probability,
            }
        )
    return results
