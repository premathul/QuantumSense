"""QuantumSense: reduced-order tools for quantum acoustic detector design."""

from .phonons import (
    phonon_energy_j,
    phonon_energy_ev,
    equivalent_temperature_k,
    thermal_occupation,
    bragg_period_m,
)
from .resonator import PhononMode
from .detector import PhononDetector

__all__ = [
    "phonon_energy_j",
    "phonon_energy_ev",
    "equivalent_temperature_k",
    "thermal_occupation",
    "bragg_period_m",
    "PhononMode",
    "PhononDetector",
]

__version__ = "0.1.0"
