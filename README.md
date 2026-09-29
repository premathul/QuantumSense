# QuantumSense

**A physics-first simulation and design toolkit for a cryogenic GHz phonon detector based on a nanomechanical/phononic resonator coupled to a semiconductor quantum sensor.**

QuantumSense is intended as a research repository for asking a concrete engineering question:

> Can a fabricated nanoscale device capture a short-duration acoustic-phonon excitation, confine it in a phononic resonator, convert the mechanical excitation into a measurable quantum-state change, and distinguish that event from thermal and readout noise?

The first target is **high-frequency acoustic phonons in the ~0.1–10 GHz range**, with a design point near **1–2 GHz**. The initial implementation is not presented as a completed experimental detector. It is a quantitative design and feasibility framework for a cryogenic prototype that could be fabricated using electron-beam lithography, dry etching, metal-gate deposition and suspended or partially released nanostructures.

The long-term device concept is especially motivated by Ge/SiGe hole-spin systems, where spin-orbit coupling provides a route for converting strain into a measurable change of the spin Hamiltonian.

---

## 1. Device concept

The proposed detector contains five physical elements:

1. **Phonon collection region** — a membrane, nanobeam or acoustic waveguide receives propagating acoustic phonons.
2. **Phononic crystal filter** — periodic patterning rejects frequencies outside a designed acoustic passband or band-edge region.
3. **Defect cavity** — a local defect confines a selected mechanical mode and increases its interaction time.
4. **Quantum transducer** — a quantum dot, hole-spin qubit or other two-level system converts cavity strain into a frequency shift, transition, or state-dependent signal.
5. **Electrical readout** — charge sensing, gate reflectometry, spin-to-charge conversion, or another experimentally appropriate readout records the event.

Conceptually:

```text
incoming acoustic pulse
        |
        v
+-----------------+      +-----------------------+
| phonon collector|----->| phononic-crystal guide|
+-----------------+      +-----------+-----------+
                                  |
                                  v
                         +------------------+
                         | defect resonator |
                         |   localized mode |
                         +--------+---------+
                                  |
                              strain field
                                  |
                                  v
                         +------------------+
                         | quantum sensor   |
                         | Ge hole spin /   |
                         | quantum dot      |
                         +--------+---------+
                                  |
                         electrical readout
                                  |
                                  v
                           detection event
```

A first laboratory implementation should be understood as a **cryogenic device**, not a room-temperature handheld sensor.

---

## 2. Why GHz phonons?

A phonon with frequency \(f\) has energy

\[
E_{\mathrm{ph}} = h f.
\]

Its corresponding temperature scale is

\[
T_{\mathrm{ph}} = \frac{h f}{k_B}.
\]

At 1 GHz,

\[
\frac{hf}{k_B} \approx 48~\mathrm{mK}.
\]

The thermal occupation of a single harmonic mode is

\[
\bar n_{\mathrm{th}} =
\frac{1}{\exp(hf/k_BT)-1}.
\]

This is why the lowest-occupation GHz experiments naturally point toward dilution-refrigerator temperatures.

Higher frequencies reduce thermal occupation but impose tighter fabrication tolerances. For acoustic velocity \(v\), a first-order 1D Bragg length scale is approximately

\[
a \sim \frac{v}{2f}.
\]

For \(v=5000~\mathrm{m/s}\) and \(f=2~\mathrm{GHz}\), this gives \(a\sim1.25~\mu\mathrm{m}\). This is only an initial scale estimate: the actual phononic-crystal dimensions must come from an elastic band-structure calculation for the complete geometry and material stack.

---

## 3. Detection mechanism

The most conservative architecture is **resonant strain transduction**.

A mechanical mode produces a strain field \(\epsilon(\mathbf r,t)\). A semiconductor quantum state can respond through deformation-potential coupling, spin-orbit-mediated \(g\)-tensor modulation or another strain-sensitive Hamiltonian term. At the effective level,

\[
\delta f_q =
\frac{\partial f_q}{\partial \epsilon}\,
\delta\epsilon.
\]

For a quantized mechanical mode,

\[
\epsilon =
\epsilon_{\mathrm{zpf}}
(a+a^\dagger),
\]

and an effective coupling can be parameterized as

\[
g_{\mathrm{sp}} =
\left|
\frac{\partial f_q}{\partial\epsilon}
\right|
\epsilon_{\mathrm{zpf}}.
\]

QuantumSense does **not** treat an assumed value of \(g_{\mathrm{sp}}\) as a prediction. It remains an explicit input until obtained from a validated microscopic or finite-element model.

### Resonant detection

Tune the quantum transition near the mechanical resonance. In the ideal resonant reduced model,

\[
P_{\mathrm{swap}}(t)=\sin^2(2\pi g_{\mathrm{sp}}t)
\]

when \(g_{\mathrm{sp}}\) is specified in Hz.

### Dispersive detection

For detuning \(|\Delta|\gg g_{\mathrm{sp}}\),

\[
\chi \approx \frac{g_{\mathrm{sp}}^2}{\Delta},
\]

so phonon occupation can shift the sensor frequency without requiring a full resonant swap.

A real detector must additionally include mechanical loss, sensor decoherence, phonon collection, thermal background, mode mismatch and readout infidelity.

---

## 4. Resonator figures of merit

For mechanical resonance frequency \(f_m\) and quality factor \(Q_m\),

\[
\Delta f_m = \frac{f_m}{Q_m}.
\]

Using the convention

\[
Q_m=\frac{\omega_m}{\kappa},
\]

the mechanical energy lifetime is

\[
\tau_m=\frac{1}{\kappa}=\frac{Q_m}{2\pi f_m}.
\]

The repository states this convention explicitly because amplitude lifetime, energy lifetime and linewidth conventions are easily mixed.

A useful detector requires a balance between high \(Q_m\), sufficient external coupling, strong sensor–mode coupling, long sensor coherence, low thermal occupation and high-fidelity electrical readout. Very high \(Q\) is not automatically optimal: an over-isolated cavity may collect incoming phonons poorly.

---

## 5. What “deployable” means here

The repository uses **deployable** in an engineering sense: a design that can progress toward a fabrication mask, cryogenic wiring plan and measurable protocol.

A credible prototype would require:

- a semiconductor heterostructure or nanomechanical chip;
- lithographically defined phononic structures;
- a localized GHz mechanical mode;
- a cryostat, likely in the dilution-refrigerator regime for very low phonon occupation;
- microwave/RF wiring;
- gates and/or charge-sensor readout;
- an acoustic excitation/calibration mechanism;
- spectrum, time-domain and background measurements.

QuantumSense is therefore a **simulation and experimental-design layer**, not a claim that a completed Ge single-phonon detector already exists.

---

## 6. Initial numerical design point

| Parameter | Initial value |
|---|---:|
| Mechanical frequency | 1.5 GHz |
| Mechanical \(Q\) | 10,000 |
| Bath temperature | 20 mK |
| Effective \(g_{\mathrm{sp}}/2\pi\)-style input | 1 MHz |
| Readout fidelity | 0.98 |
| Phonon collection efficiency | 0.20 |
| Acoustic velocity used for scale estimate | 5000 m/s |

These are editable design inputs, not measurements for a specific fabricated device.

The code reports:

- single-phonon energy;
- equivalent phonon temperature;
- Bose–Einstein thermal occupation;
- cavity linewidth;
- cavity energy lifetime;
- approximate Bragg period;
- ideal resonant swap time;
- simplified event-detection probability;
- repeated-shot probability-difference SNR.

---

## 7. Repository layout

```text
QuantumSense/
├── README.md
├── pyproject.toml
├── src/
│   └── quantumsense/
│       ├── __init__.py
│       ├── constants.py
│       ├── phonons.py
│       ├── resonator.py
│       ├── detector.py
│       └── signal.py
├── examples/
│   └── ghz_phonon_detector.py
├── tests/
│   └── test_physics.py
└── docs/
    ├── PHYSICS.md
    ├── DEVICE_CONCEPT.md
    └── EXPERIMENTAL_ROADMAP.md
```

---

## 8. Installation

Requires Python 3.10 or newer.

```bash
git clone https://github.com/premathul/QuantumSense.git
cd QuantumSense
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

For development:

```bash
pip install -e ".[dev]"
pytest
```

---

## 9. Quick start

```python
from quantumsense import PhononMode, PhononDetector

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
)

print(mode.summary())
print(detector.summary())
```

Or run

```bash
python examples/ghz_phonon_detector.py
```

---

## 10. Scientific confidence levels

QuantumSense deliberately separates three levels of confidence.

### Level A — standard analytical relations

Examples: \(E=hf\), Bose–Einstein occupation, \(f/Q\) linewidth and the stated \(Q/(2\pi f)\) lifetime convention.

### Level B — reduced-order physical models

The two-level-system/mechanical-mode interaction and efficiency chain are useful for feasibility calculations, but they omit device-specific multimode physics, spectral diffusion, nonlinearities, pulse imperfections and detailed open-system dynamics.

### Level C — device predictions

Absolute Ge/SiGe spin–phonon coupling, single-phonon collection efficiency, phononic band structure and fabrication yield require device-specific finite-element and/or multiband electronic-structure calculations plus experiment.

The repository should never convert an assumed input into an apparently measured or independently predicted result.

---

## 11. Path toward a real Ge/SiGe implementation

A Ge-oriented realization could combine:

1. a strained Ge quantum well;
2. a gate-defined hole quantum dot;
3. nearby charge sensing or RF gate reflectometry;
4. an etched nanobeam or membrane;
5. phononic-crystal mirrors around a defect cavity;
6. magnetic-field orientation selected for useful spin–strain coupling while preserving coherence;
7. calibrated GHz acoustic injection;
8. time-resolved spin or charge readout.

A sensible experimental sequence is:

**Milestone 1:** fabricate and identify a mechanical resonance.

**Milestone 2:** demonstrate that a quantum-dot observable shifts or relaxes when the mode is driven.

**Milestone 3:** extract coupling versus drive frequency and magnetic-field orientation.

**Milestone 4:** reduce drive power and temperature while calibrating occupation.

**Milestone 5:** demonstrate statistically resolved few-phonon sensitivity.

**Milestone 6:** pursue single-event or QND-style detection only if measured coupling, lifetime and readout performance support it.

---

## 12. Literature anchors

The design philosophy is motivated by experimentally demonstrated and proposed quantum-acoustic systems:

- C. Spinnler *et al.*, **A single-photon emitter coupled to a phononic-crystal resonator in the resolved-sideband regime**, *Nature Communications* **15**, 9509 (2024). DOI: https://doi.org/10.1038/s41467-024-53882-2
- D.-M. Mei *et al.*, **Phonon-Coupled Hole-Spin Qubits in High-Purity Germanium: Design and Modeling of a Scalable Architecture** (2025), arXiv:2504.12221.
- M. J. A. Schuetz *et al.*, **Universal Quantum Transducers Based on Surface Acoustic Waves**, *Physical Review X* **5**, 031031 (2015).

These references establish relevant ingredients; they do not validate the complete QuantumSense detector proposed here.

---

## 13. Planned extensions

Future versions should add:

- elastic band-structure calculations;
- COMSOL/FEniCS mode import;
- zero-point strain from FEM mode normalization;
- anisotropic elasticity for Si, Ge and SiGe;
- Bir–Pikus strain coupling;
- multiband hole-state response;
- \(T_1\)-based phonon spectroscopy;
- Ramsey/echo phase detection;
- arrival-time reconstruction;
- Bayesian event classification and matched filtering;
- realistic amplifier and charge-readout noise;
- multiple sensors for phonon localization;
- inverse design of the cavity;
- fabrication-tolerance Monte Carlo;
- GDS-compatible geometry generation.

---

## 14. Research objective

The eventual objective is a nanoscale instrument that closes the chain

\[
\boxed{
\text{phonon}
\rightarrow
\text{localized strain}
\rightarrow
\text{quantum-state change}
\rightarrow
\text{electrical signal}
}
\]

with every arrow quantitatively measured or independently modeled.

QuantumSense is the computational starting point for testing whether that chain can close before committing to a fabrication run.

---

## Author

**Athul Prem**  
Physics PhD researcher  
Research interests: Ge/SiGe hole-spin qubits, quantum sensing, phononics, nanofabrication and scientific computing.
