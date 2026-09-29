"""Reduced-order quantum-acoustic detector model."""

from __future__ import annotations

from dataclasses import dataclass
import math

from .resonator import PhononMode


def _probability(name: str, value: float) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must lie in [0, 1].")
    return value


@dataclass(frozen=True)
class PhononDetector:
    """Idealized single-mode quantum transducer.

    coupling_hz is g/(2*pi), i.e. the coupling quoted in cycles per second.
    A resonant Jaynes-Cummings exchange then gives P=sin^2(2*pi*g*t).
    """

    mode: PhononMode
    coupling_hz: float
    collection_efficiency: float = 0.2
    readout_fidelity: float = 0.98
    sensor_t1_s: float | None = None

    def __post_init__(self) -> None:
        if self.coupling_hz <= 0:
            raise ValueError("coupling_hz must be > 0.")
        _probability("collection_efficiency", self.collection_efficiency)
        _probability("readout_fidelity", self.readout_fidelity)
        if self.sensor_t1_s is not None and self.sensor_t1_s <= 0:
            raise ValueError("sensor_t1_s must be > 0 when supplied.")

    @property
    def ideal_full_swap_time_s(self) -> float:
        """First maximum of sin^2(2*pi*g*t): t = 1/(4g)."""
        return 1.0 / (4.0 * self.coupling_hz)

    def resonant_swap_probability(self, interaction_time_s: float) -> float:
        if interaction_time_s < 0:
            raise ValueError("interaction_time_s must be >= 0.")
        p = math.sin(2.0 * math.pi * self.coupling_hz * interaction_time_s) ** 2

        # Optional phenomenological survival factor for sensor relaxation.
        if self.sensor_t1_s is not None:
            p *= math.exp(-interaction_time_s / self.sensor_t1_s)
        return p

    def event_detection_probability(self, interaction_time_s: float | None = None) -> float:
        """Simple end-to-end probability for one incident, mode-matched phonon.

        This intentionally excludes false-positive probability and thermal
        background; use it only as a first feasibility metric.
        """
        if interaction_time_s is None:
            interaction_time_s = self.ideal_full_swap_time_s

        p_swap = self.resonant_swap_probability(interaction_time_s)
        return self.collection_efficiency * p_swap * self.readout_fidelity

    def cavity_to_swap_ratio(self) -> float:
        """Mechanical energy lifetime divided by ideal full-swap time."""
        return self.mode.energy_lifetime_s / self.ideal_full_swap_time_s

    def summary(self) -> str:
        p = self.event_detection_probability()
        return (
            f"Coupling g/2pi: {self.coupling_hz/1e6:.3f} MHz\n"
            f"Ideal full-swap time: {self.ideal_full_swap_time_s*1e9:.3f} ns\n"
            f"Cavity lifetime / swap time: {self.cavity_to_swap_ratio():.3f}\n"
            f"Collection efficiency: {self.collection_efficiency:.3f}\n"
            f"Readout fidelity: {self.readout_fidelity:.3f}\n"
            f"Idealized per-incident-phonon detection probability: {p:.4f}"
        )
