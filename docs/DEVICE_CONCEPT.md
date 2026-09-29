# Device concept: a cryogenic GHz phonon event sensor

## Objective

Build a chip-scale structure that receives a high-frequency acoustic excitation, spectrally selects a target band, localizes the mechanical energy and converts that energy into an electrically readable change of a quantum sensor.

## Proposed stack

A Ge/SiGe-oriented realization may use a strained Ge quantum well containing a gate-defined hole quantum dot. The dot is positioned near the strain antinode of a defect mode in a suspended or semi-suspended nanobeam/membrane. Periodic holes, slots or width modulation create phononic mirrors around the defect.

The device therefore combines a **phononic subsystem** and an **electronic subsystem**.

### Phononic subsystem

- acoustic collection pad or waveguide;
- impedance-matching section;
- periodic phononic lattice;
- central defect cavity;
- optional output port for transmission characterization.

### Electronic subsystem

- accumulation/depletion gates;
- quantum-dot confinement region;
- reservoir and ohmic connection where required;
- charge sensor or RF resonator;
- magnetic field for spin-state definition.

## Recommended first prototype

Do not begin with a geometry optimized only for an assumed single-phonon interaction. Fabricate a structure that is easy to characterize classically.

A first mask should permit:

- several cavity lengths;
- several lattice constants;
- several hole/slot dimensions;
- at least one unpatterned control beam;
- electrical continuity and gate tests;
- acoustic drive and readout structures;
- SEM metrology after fabrication.

A target around 1–2 GHz is attractive because nanoscale feature sizes remain accessible to EBL while (hf/k_B) reaches the ~50–100 mK scale.

## Experimental observables

Before claiming phonon detection, demonstrate a reproducible resonance through at least one classical observable:

- driven displacement;
- RF transmission/reflection;
- sideband response;
- charge-sensor response;
- qubit relaxation rate versus drive frequency;
- qubit frequency shift versus acoustic drive.

Then show that the response:

1. is frequency selective;
2. follows the expected cavity resonance;
3. changes with drive power;
4. disappears or shifts in a control geometry;
5. obeys temperature dependence consistent with the mode.

## Detection modes

### Mode A — relaxation spectroscopy

Tune the spin splitting through the mechanical resonance and measure a change in (T_1). This may be experimentally simpler than attempting coherent phonon swaps.

### Mode B — coherent resonant exchange

When (g) is sufficiently large relative to mechanical and spin decoherence, pulse the systems into resonance for a controlled interval and search for state exchange.

### Mode C — dispersive sensing

Keep the sensor detuned and measure a phonon-number-dependent frequency or phase shift. This is attractive for reduced back-action but requires sufficient dispersive shift relative to linewidth and frequency noise.

## Key engineering risks

The largest risks are not hidden in the simple analytical equations:

- etch damage degrading the semiconductor;
- insufficient mechanical (Q);
- poor coupling between incoming phonons and the defect mode;
- charge noise created by nearby etched surfaces;
- imperfect overlap between the quantum dot and strain antinode;
- mode crowding;
- uncertainty in the microscopic spin–strain matrix element;
- heating from the acoustic drive;
- readout bandwidth slower than the event dynamics.

QuantumSense should be used to expose these tradeoffs rather than hide them.
