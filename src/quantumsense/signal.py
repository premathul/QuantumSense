"""Simple statistical tools for event discrimination."""

from __future__ import annotations

import math


def binomial_standard_error(probability: float, shots: int) -> float:
    if not 0.0 <= probability <= 1.0:
        raise ValueError("probability must lie in [0, 1].")
    if shots <= 0:
        raise ValueError("shots must be > 0.")
    return math.sqrt(probability * (1.0 - probability) / shots)


def difference_snr(
    signal_probability: float,
    background_probability: float,
    shots: int,
) -> float:
    """Approximate SNR for the difference of two independent binomial rates."""
    if not 0.0 <= signal_probability <= 1.0:
        raise ValueError("signal_probability must lie in [0, 1].")
    if not 0.0 <= background_probability <= 1.0:
        raise ValueError("background_probability must lie in [0, 1].")
    if shots <= 0:
        raise ValueError("shots must be > 0.")

    var = (
        signal_probability * (1.0 - signal_probability)
        + background_probability * (1.0 - background_probability)
    ) / shots

    if var == 0.0:
        return math.inf if signal_probability != background_probability else 0.0

    return abs(signal_probability - background_probability) / math.sqrt(var)
