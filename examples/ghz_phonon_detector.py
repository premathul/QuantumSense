"""Example feasibility calculation for a 1.5 GHz detector concept."""

from quantumsense import PhononMode, PhononDetector, bragg_period_m
from quantumsense.signal import difference_snr


def main() -> None:
    mode = PhononMode(
        frequency_hz=1.5e9,
        quality_factor=1.0e4,
        temperature_k=0.020,
    )

    detector = PhononDetector(
        mode=mode,
        coupling_hz=1.0e6,
        collection_efficiency=0.20,
        readout_fidelity=0.98,
        sensor_t1_s=1.0e-3,
    )

    period = bragg_period_m(
        frequency_hz=mode.frequency_hz,
        acoustic_velocity_m_s=5000.0,
    )

    print("=== QuantumSense: GHz phonon detector ===")
    print(mode.summary())
    print()
    print(detector.summary())
    print()
    print(f"First-order Bragg length scale: {period*1e6:.3f} um")

    # Illustration only: compare two empirically measured probabilities in a
    # future experiment. These are not predicted detector backgrounds.
    snr = difference_snr(
        signal_probability=0.25,
        background_probability=0.05,
        shots=1000,
    )
    print(f"Example 1000-shot probability-difference SNR: {snr:.3f}")


if __name__ == "__main__":
    main()
