# Physics model

## Scope

QuantumSense begins with a deliberately reduced model: one acoustic mode coupled to one quantum two-level system. This is useful for feasibility scans, parameter sensitivity and experimental planning, but it is not a substitute for a full elastic, electrostatic and multiband semiconductor calculation.

## Phonon energy and thermal occupation

For a mode of frequency \(f_m\),

\[
E_m = h f_m,
\qquad
\bar n =
\frac{1}{\exp(hf_m/k_BT)-1}.
\]

The important comparison for a quantum detector is \(k_BT\) versus \(hf_m\), not temperature alone.

## Mechanical resonance

The code uses the convention

\[
Q_m=\frac{\omega_m}{\kappa},
\]

so

\[
\tau_E=\frac{1}{\kappa}
=\frac{Q_m}{2\pi f_m}.
\]

Here \(\tau_E\) is the mechanical energy-decay lifetime under this convention. Imported experimental values must be checked because publications can use different amplitude/energy decay definitions.

## Quantum-transducer coupling

The most important device-specific quantity is the strain sensitivity of the selected quantum transition.

A generic linearized Hamiltonian can be written

\[
H =
\frac{h f_q}{2}\sigma_z
+
h f_m a^\dagger a
+
h g(a+a^\dagger)\hat O_q .
\]

The operator \(\hat O_q\) depends on the transducer. In a hole-spin device it can emerge from strain-induced modification of the valence-band Hamiltonian combined with spin-orbit coupling and the magnetic-field orientation.

After transformation to an appropriate resonant rotating-wave model, a Jaynes–Cummings-like interaction may result,

\[
H_{\mathrm{int}}
\approx
h g
\left(
a^\dagger\sigma_-+
a\sigma_+
\right).
\]

For the repository convention in which \(g\) is in Hz,

\[
P_{\mathrm{swap}}(t)
=
\sin^2(2\pi g t),
\]

and the first ideal maximum occurs at

\[
t_{\mathrm{swap}}=\frac{1}{4g}.
\]

This ideal equation does not include detuning, dephasing, mechanical decay or thermal occupation.

## Dispersive limit

For a sensor detuned from the cavity by \(\Delta\), a reduced dispersive frequency scale is

\[
\chi \sim \frac{g^2}{\Delta}
\]

when all three quantities are expressed with a consistent frequency convention. A quantitative treatment must keep track of whether angular frequencies or ordinary frequencies are being used.

## What must eventually replace the reduced model

A quantitative Ge/SiGe prediction should obtain the coupling from:

1. elastic eigenmodes of the complete fabricated geometry;
2. properly normalized zero-point displacement and strain;
3. heterostructure electrostatics;
4. valence-band states, ideally from a multiband \(k\cdot p\) Hamiltonian;
5. Bir–Pikus strain coupling;
6. spin-orbit interaction and magnetic-field orientation;
7. charge noise, hyperfine noise and gate-voltage noise;
8. finite-temperature mechanical damping.

The central modeling rule is that a parameter imported from an assumed model remains labeled as an assumption until independently validated.
