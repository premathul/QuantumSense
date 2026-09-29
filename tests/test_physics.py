import math

from quantumsense import (
    PhononMode,
    PhononDetector,
    equivalent_temperature_k,
    thermal_occupation,
    bragg_period_m,
)


def test_1ghz_temperature_scale():
    assert math.isclose(equivalent_temperature_k(1e9), 0.04799243, rel_tol=2e-6)


def test_thermal_occupation_positive():
    n = thermal_occupation(1e9, 0.020)
    assert 0.0 < n < 1.0


def test_resonator_relations():
    mode = PhononMode(1e9, 1e4, 0.020)
    assert math.isclose(mode.linewidth_hz, 1e5)
    assert math.isclose(mode.energy_lifetime_s, 1e4 / (2 * math.pi * 1e9))


def test_bragg_scale():
    assert math.isclose(bragg_period_m(2e9, 5000), 1.25e-6)


def test_full_swap():
    mode = PhononMode(1.5e9, 1e4, 0.020)
    det = PhononDetector(mode, coupling_hz=1e6)
    p = det.resonant_swap_probability(det.ideal_full_swap_time_s)
    assert math.isclose(p, 1.0, rel_tol=1e-12, abs_tol=1e-12)


def test_efficiency_chain():
    mode = PhononMode(1.5e9, 1e4, 0.020)
    det = PhononDetector(
        mode,
        coupling_hz=1e6,
        collection_efficiency=0.25,
        readout_fidelity=0.96,
    )
    assert math.isclose(det.event_detection_probability(), 0.24, rel_tol=1e-12)
