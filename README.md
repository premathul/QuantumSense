# QuantumSense

**A physics-first simulation and design toolkit for a cryogenic GHz phonon detector based on a nanomechanical/phononic resonator coupled to a semiconductor quantum sensor.**

QuantumSense is intended as a research repository for asking a concrete engineering question:

> Can a fabricated nanoscale device capture a short-duration acoustic-phonon excitation, confine it in a phononic resonator, convert the mechanical excitation into a measurable quantum-state change, and distinguish that event from thermal and readout noise?

The first target is **high-frequency acoustic phonons in the ~0.1–10 GHz range**, with a design point near **1–2 GHz**. The initial implementation is not presented as a completed experimental detector. It is a quantitative design and feasibility framework for a cryogenic prototype that could be fabricated using standard nanofabrication methods such as electron-beam lithography, dry etching, metal-gate deposition and suspended or partially released nanostructures.

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

A phonon with frequency (f) has energy

[
E_{mathrm{ph}} = h f.
]

Its corresponding temperature scale is

[
T_{mathrm{ph}} = rac{h f}{k_B}.
]

At 1 GHz,

[
rac{hf}{k_B} approx 48~mathrm{mK}.
]

This immediately shows why the lowest-occupation experiments require dilution-refrigerator temperatures. The thermal occupation of a mode is

[
ar n_{mathrm{th}} =
rac{1}{exp(hf/k_BT)-1}.
]

A 1 GHz resonator at tens of millikelvin can approach the few-phonon regime, whereas the same mode at kelvin temperatures contains many thermal phonons.

Higher frequencies reduce thermal occupation but impose tighter fabrication tolerances. For an acoustic velocity (v), a first-order Bragg period is approximately

[
a sim rac{v}{2f}.
]

For (v=5000~mathrm{m/s}) and (f=2~mathrm{GHz}), this gives (asim1.25~mumathrm{m}). Actual phononic-crystal dimensions depend on the full elastic eigenproblem, geometry, polarization and material stack; the relation above is only an initial scale estimate.

---

## 3. Detection mechanism

The most conservative architecture is **resonant strain transduction**.

A mechanical mode produces a strain field (epsilon(mathbf r,t)). A semiconductor quantum state responds through deformation-potential coupling, spin-orbit-mediated (g)-tensor modulation, or another strain-sensitive Hamiltonian term. At the effective level,

[
delta f_q =
rac{partial f_q}{partial epsilon},
deltaepsilon.
]

For a quantized mechanical mode,

[
epsilon =
epsilon_{mathrm{zpf}}
(a+a^dagger),
]

and an effective spin–phonon coupling may be parameterized as

[
g_{mathrm{sp}} =
left|
rac{partial f_q}{partialepsilon}
ight|
epsilon_{mathrm{zpf}}.
]

QuantumSense does **not** assume that a guessed value of (g_{mathrm{sp}}) is a prediction. The coupling is an explicit input until it is obtained from a validated microscopic or finite-element model.

Two measurement regimes are useful:

### Resonant detection

Tune the quantum transition near the mechanical resonance. A captured phonon can exchange energy with the sensor. In an ideal Jaynes–Cummings model,

[
P_{mathrm{swap}}(t)
=
sin^2(2pi g_{mathrm{sp}} t)
]

when (g_{mathrm{sp}}) is specified in Hz and the two systems are on resonance.

### Dispersive detection

For detuning (|Delta| gg g_{mathrm{sp}}),

[
chi approx rac{g_{mathrm{sp}}^2}{Delta},
]

so the phonon occupation changes the sensor frequency without requiring a full resonant swap.

The real detector will additionally depend on mechanical loss, sensor decoherence, phonon-collection efficiency, mode matching, thermal background and readout fidelity.

---

## 4. Resonator figures of merit

For resonance frequency (f_m) and mechanical quality factor (Q_m),

[
Delta f_m = rac{f_m}{Q_m},
]

and, under the convention (Q_m=omega_m/kappa), the mechanical energy lifetime is

[
	au_m = rac{Q_m}{2pi f_m}.
]

The repository calculates these values directly and warns against confusing amplitude lifetime, energy lifetime and linewidth conventions.

A useful detector requires a balance between:

- sufficiently high (Q_m) to retain the excitation;
- sufficient external coupling to allow phonons to enter the resonator;
- strong enough sensor–mode coupling;
- sensor coherence long enough for interrogation;
- low thermal occupation;
- efficient electrical readout.

Very high (Q) is not automatically optimal: an over-isolated cavity may collect incoming phonons poorly.

---

## 5. What “deployable” means here

The repository uses **deployable** in an engineering sense: a device concept that can be translated into a fabrication mask, a cryogenic wiring plan and a measurable protocol.

A credible first prototype would require:

- a fabricated semiconductor heterostructure or nanomechanical chip;
- lithographically defined phononic structures;
- a localized GHz mechanical mode;
- a cryostat, likely in the dilution-refrigerator regime for very low phonon occupation;
- microwave/RF lines;
- gates and/or charge-sensor readout;
- an acoustic excitation/calibration mechanism;
- spectrum, time-domain and background measurements.

The current repository is therefore a **simulation and experimental-design layer**, not a claim of a finished sensor.

---

## 6. Initial experimental target

The default demonstrator uses:

| Parameter | Initial design value |
|---|---:|
| Mechanical frequency | 1.5 GHz |
| Mechanical (Q) | 10,000 |
| Bath temperature | 20 mK |
| Effective spin–phonon coupling | 1 MHz |
| Readout fidelity | 0.98 |
| Phonon collection efficiency | 0.20 |
| Acoustic velocity for scale estimate | 5000 m/s |

These are editable design inputs, not measured values for a specific fabricated device.

The code reports:

- single-phonon energy;
- equivalent phonon temperature;
- thermal occupation;
- cavity linewidth;
- cavity energy lifetime;
- approximate Bragg period;
- ideal resonant swap time;
- effective event-detection probability;
- repeated-shot signal-to-noise estimates.

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

Or run:

```bash
python examples/ghz_phonon_detector.py
```

---

## 10. Scientific boundaries

QuantumSense deliberately distinguishes three levels of confidence.

### Level A — exact or standard analytical relations

Examples include (E=hf), Bose–Einstein thermal occupation, (f/Q) linewidth and the simple (Q/(2pi f)) energy-lifetime relation under the stated convention.

### Level B — reduced-order physical models

The resonant two-level-system/mechanical-mode interaction and simple detection-efficiency model are useful for feasibility calculations but neglect device-specific multimode physics, frequency noise, spectral diffusion, nonlinearities, pulse imperfections and non-Markovian effects.

### Level C — device predictions

Absolute Ge/SiGe spin–phonon coupling, single-phonon collection efficiency, phononic band structure and fabrication yield require device-specific finite-element and/or multiband electronic-structure calculations plus experiment. Values in the example are parameters, not validated predictions.

This distinction is intentional. The repository should never convert an assumed parameter into an apparently measured result.

---

## 11. Path toward a real Ge/SiGe implementation

A practical Ge-oriented extension would combine:

1. a strained Ge quantum well;
2. gate-defined hole quantum dot;
3. nearby charge sensor or RF gate reflectometry;
4. etched nanobeam or membrane;
5. phononic-crystal mirrors surrounding a defect cavity;
6. magnetic-field orientation chosen to obtain useful spin–strain coupling while preserving coherence;
7. calibrated GHz acoustic injection;
8. time-resolved spin or charge readout.

The first experimental milestone should **not** be “single phonon detected.” A sensible progression is:

**Milestone 1:** fabricate and identify a mechanical resonance.

**Milestone 2:** demonstrate that the quantum-dot observable shifts or relaxes when the mode is driven.

**Milestone 3:** extract the coupling strength versus drive frequency and magnetic-field orientation.

**Milestone 4:** reduce drive power and temperature, calibrating phonon occupation.

**Milestone 5:** demonstrate statistically resolved few-phonon sensitivity.

**Milestone 6:** pursue single-event or quantum-nondemolition-style detection only if the measured coupling, lifetime and readout support it.

---

## 12. Literature anchors

The design philosophy is motivated by experimentally demonstrated and proposed solid-state quantum-acoustic systems. In particular:

- C. Spinnler *et al.*, *A single-photon emitter coupled to a phononic-crystal resonator in the resolved-sideband regime*, Nature Communications **15**, 9509 (2024). DOI: https://doi.org/10.1038/s41467-024-53882-2
- D.-M. Mei *et al.*, *Phonon-Coupled Hole-Spin Qubits in High-Purity Germanium: Design and Modeling of a Scalable Architecture* (2025), arXiv:2504.12221.
- M. J. A. Schuetz *et al.*, *Universal Quantum Transducers Based on Surface Acoustic Waves*, Physical Review X **5**, 031031 (2015).

These references establish relevant ingredients. They do not by themselves validate the complete QuantumSense detector proposed here.

---

## 13. Planned extensions

Future versions should add:

- 1D transfer-matrix phononic filters;
- full elastic-band-structure import from COMSOL/QTCAD/FEniCS;
- zero-point strain from FEM mode normalization;
- anisotropic elasticity for Si, Ge and SiGe;
- Bir–Pikus strain coupling;
- multiband hole-state response;
- (T_1)-based phonon spectroscopy;
- Ramsey/echo phase detection;
- arrival-time reconstruction;
- Bayesian event detection;
- matched filtering;
- realistic amplifier and charge-readout noise;
- multiple sensors for phonon localization;
- inverse design of the phononic cavity;
- GDS-compatible geometry generation.

---

## 14. Research objective

The eventual objective is a nanoscale instrument that converts an otherwise difficult-to-observe acoustic excitation into a measurable quantum-state signal:

[
oxed{
	ext{phonon}
ightarrow
	ext{localized strain}
ightarrow
	ext{quantum-state change}
ightarrow
	ext{electrical signal}
}
]

QuantumSense is the computational starting point for testing whether that chain closes quantitatively before committing to a fabrication run.

---

## Author

**Athul Prem**  
Physics PhD researcher  
Research interests: Ge/SiGe hole-spin qubits, quantum sensing, phononics, nanofabrication and scientific computing.
