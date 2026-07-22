"""Simple risk scoring utilities."""

from __future__ import annotations


def clamp_score(value: float) -> float:
    return max(0.0, min(10.0, value))


def weighted_average(values: dict[str, float], weights: dict[str, float]) -> float:
    total_weight = sum(weights.get(key, 0.0) for key in values)
    if total_weight <= 0:
        return 0.0
    score = sum(values[key] * weights.get(key, 0.0) for key in values) / total_weight
    return clamp_score(score)
