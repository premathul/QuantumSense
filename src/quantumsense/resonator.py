"""Reduced-order model of a localized phononic resonator mode."""

from __future__ import annotations

from dataclasses import dataclass

from .phonons import (
    phonon_energy_j,
    phonon_energy_ev,
    equivalent_temperature_k,
    thermal_occupation,
)


@dataclass(frozen=True)
class PhononMode:
    """Single mechanical mode.

    quality_factor uses Q = omega/kappa. The reported lifetime is therefore
    the mechanical energy-decay time tau = 1/kappa = Q/(2*pi*f).
    """

    frequency_hz: float
    quality_factor: float
    temperature_k: float

    def __post_init__(self) -> None:
        if self.frequency_hz <= 0:
            raise ValueError("frequency_hz must be > 0.")
        if self.quality_factor <= 0:
            raise ValueError("quality_factor must be > 0.")
        if self.temperature_k <= 0:
            raise ValueError("temperature_k must be > 0.")

    @property
    def linewidth_hz(self) -> float:
        return self.frequency_hz / self.quality_factor

    @property
    def energy_lifetime_s(self) -> float:
        import math
        return self.quality_factor / (2.0 * math.pi * self.frequency_hz)

    @property
    def energy_j(self) -> float:
        return phonon_energy_j(self.frequency_hz)

    @property
    def energy_ev(self) -> float:
        return phonon_energy_ev(self.frequency_hz)

    @property
    def equivalent_temperature_k(self) -> float:
        return equivalent_temperature_k(self.frequency_hz)

    @property
    def n_thermal(self) -> float:
        return thermal_occupation(self.frequency_hz, self.temperature_k)

    def summary(self) -> str:
        return (
            f"Phonon mode: {self.frequency_hz/1e9:.3f} GHz\n"
            f"Q: {self.quality_factor:.3g}\n"
            f"Linewidth: {self.linewidth_hz/1e3:.3f} kHz\n"
            f"Energy lifetime: {self.energy_lifetime_s*1e6:.3f} us\n"
            f"Single-phonon energy: {self.energy_ev*1e6:.6f} ueV\n"
            f"h f / k_B: {self.equivalent_temperature_k*1e3:.3f} mK\n"
            f"Thermal occupation: {self.n_thermal:.6g}"
        )
