# Experimental roadmap

## Phase 0 — numerical verification

Goal: establish a reproducible simulation baseline.

1. Verify analytical calculations in this repository.
2. Build an elastic finite-element unit cell.
3. Calculate the phononic band structure.
4. Introduce a defect and calculate the localized eigenmode.
5. Extract resonance frequency, mode volume, radiation loss and strain field.
6. Perform mesh convergence.
7. Export normalized strain at the intended quantum-dot position.

Deliverable: a device geometry with a numerically converged target mode.

## Phase 1 — passive phononic test chip

Fabricate the phononic structure without relying on quantum-dot operation.

Measurements:

- resonance frequencies;
- quality factor;
- device-to-device variation;
- temperature dependence;
- response versus lithographic dimensions.

This phase determines whether the phononic structure itself works.

## Phase 2 — integrated semiconductor device

Integrate the phononic structure with the active heterostructure and gates.

First verify:

- intact quantum well;
- acceptable leakage;
- stable charge transitions;
- functional charge sensor;
- no catastrophic degradation from release/etch steps.

Only then proceed to quantum-acoustic measurements.

## Phase 3 — driven coupling

Inject a calibrated coherent acoustic tone.

Measure:

- sensor response versus drive frequency;
- response versus drive amplitude;
- magnetic-field-angle dependence;
- detuning dependence;
- cavity ring-down if available.

Fit a physical model and extract coupling parameters with uncertainty.

## Phase 4 — low-occupation operation

Lower bath temperature and drive amplitude.

Calibrate thermal occupation using independently measurable quantities whenever possible. Avoid inferring “single phonons” solely from nominal generator power.

## Phase 5 — event detection

Define, before collecting the decisive dataset:

- detection window;
- threshold statistic;
- false-positive rate;
- detection efficiency;
- background model;
- number of trials;
- confidence interval.

A single-phonon detector claim requires event statistics and calibration, not merely a visible resonance.

## Fabrication-facing outputs to add

Future releases should generate:

- parameterized nanobeam geometry;
- taper tables;
- hole position/diameter tables;
- process-bias sweeps;
- GDS layers;
- alignment marks;
- proximity-correction metadata;
- fabrication tolerance Monte Carlo.

## Suggested experimental success ladder

1. Mechanical mode exists.
2. Mechanical mode is reproducible.
3. Quantum sensor operates after phononic fabrication.
4. Driven phonons measurably affect sensor.
5. Coupling model agrees with power/frequency/field dependence.
6. Few-phonon response is statistically resolved.
7. Single-event sensitivity is calibrated.

Each step should be treated as a separate scientific result.
