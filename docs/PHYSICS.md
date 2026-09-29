# Physics model

## Scope

QuantumSense begins with a deliberately reduced model: one acoustic mode coupled to one quantum two-level system. This is the correct level for feasibility scans, parameter sensitivity and experimental planning, but it is not yet a substitute for a full elastic, electrostatic and multiband semiconductor calculation.

## Phonon energy and thermal occupation

For a mode of frequency (f_m),

[
E_m=h f_m,
qquad
ar n =
rac{1}{exp(hf_m/k_BT)-1}.
]

The relevant question for a quantum detector is not simply whether the bath is “cold,” but whether (k_B T) is small compared with (h f_m).

## Mechanical resonance

The code uses

[
Q_m=rac{omega_m}{kappa}
]

and therefore

[
	au_E=rac{1}{kappa}
=rac{Q_m}{2pi f_m}.
]

Here (	au_E) is an energy-decay lifetime under this convention. Experimental publications sometimes quote different amplitude/energy decay conventions, so imported values must be checked carefully.

## Spin–phonon / quantum-transducer coupling

The most important device-specific quantity is the strain sensitivity of the selected quantum transition.

A generic linearized Hamiltonian is

[
H =
rac{h f_q}{2}sigma_z +
h f_m a^dagger a +
h g(a+a^dagger)hat O_q .
]

The operator (hat O_q) depends on the physical transducer. For a hole-spin device it may emerge from strain-induced modulation of the valence-band Hamiltonian and spin-orbit-dependent (g)-tensor.

After moving to a resonant rotating-wave description, a Jaynes–Cummings-like term may result:

[
H_{mathrm{int}}
approx
h g(
a^daggersigma_-+
asigma_+
).
]

For the repository convention where (g) is in Hz,

[
P_{mathrm{swap}}(t)
=
sin^2(2pi g t).
]

The first ideal maximum occurs at

[
t_{mathrm{swap}}=rac{1}{4g}.
]

## What must eventually replace the reduced model

A quantitative Ge/SiGe prediction should obtain coupling from:

1. elastic eigenmodes of the complete fabricated geometry;
2. properly normalized zero-point displacement and strain;
3. heterostructure electrostatics;
4. valence-band states, ideally from a multiband (k\cdot p) Hamiltonian;
5. Bir–Pikus strain coupling;
6. spin-orbit interaction and magnetic-field orientation;
7. charge noise, hyperfine noise and gate-voltage noise;
8. finite-temperature mechanical damping.

The central rule is that a parameter imported from an assumed model must remain labeled as an assumption until independently validated.
