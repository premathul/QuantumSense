"""Basic acoustic-phonon calculations."""

from __future__ import annotations

import math

from .constants import PLANCK_J_S, BOLTZMANN_J_K, ELECTRON_VOLT_J


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and > 0; got {value!r}.")
    return value


def phonon_energy_j(frequency_hz: float) -> float:
    """Single-phonon energy E = h f in joules."""
    f = _positive("frequency_hz", frequency_hz)
    return PLANCK_J_S * f


def phonon_energy_ev(frequency_hz: float) -> float:
    """Single-phonon energy in electron-volts."""
    return phonon_energy_j(frequency_hz) / ELECTRON_VOLT_J


def equivalent_temperature_k(frequency_hz: float) -> float:
    """Return h f / k_B in kelvin."""
    return phonon_energy_j(frequency_hz) / BOLTZMANN_J_K


def thermal_occupation(frequency_hz: float, temperature_k: float) -> float:
    """Bose-Einstein mean occupation of one harmonic mode."""
    f = _positive("frequency_hz", frequency_hz)
    t = _positive("temperature_k", temperature_k)
    x = PLANCK_J_S * f / (BOLTZMANN_J_K * t)

    # expm1 is accurate for small x. For very large x, nbar -> 0.
    if x > 700.0:
        return 0.0
    return 1.0 / math.expm1(x)


def bragg_period_m(frequency_hz: float, acoustic_velocity_m_s: float) -> float:
    """First-order 1D Bragg scale a ~ v/(2f).

    This is a geometric starting estimate, not a substitute for an elastic
    band-structure calculation.
    """
    f = _positive("frequency_hz", frequency_hz)
    v = _positive("acoustic_velocity_m_s", acoustic_velocity_m_s)
    return v / (2.0 * f)
