# Chapter 4 — Quantum Mechanics in Three Dimensions

Independent, original, step-by-step worked solutions to all **76 numbered problems (4.1–4.76)** in Chapter 4 of D. J. Griffiths and D. F. Schroeter, *Introduction to Quantum Mechanics*, 3rd edition (Cambridge University Press, 2018).

**Live website:** https://krazad0.github.io/QM-CH1-SOLUTION/chapter4/

**Full PDF manuscript:** https://krazad0.github.io/QM-CH1-SOLUTION/chapter4/chapter-4-solutions.pdf

This is an independent educational coursework companion, **not an official textbook solutions manual, peer-reviewed paper, or an arXiv preprint**. Short problem descriptions have been paraphrased, not copied from the textbook. Consult the textbook itself for authoritative question wording and diagrams.

## Solution sections

| Exercise numbers | LaTeX source | Mathematical subjects |
|---|---|---|
| 4.1–4.11 | [01-11.tex](tex/01-11.tex) | 3D commutators, Cartesian well, spherical harmonics, radial Bessel wells |
| 4.12–4.20 | [12-20.tex](tex/12-20.tex) | Hydrogenic radial functions, expectation values, Bohr scaling, gravitational analogue |
| 4.21–4.34 | [21-34.tex](tex/21-34.tex) | Orbital angular momentum, commutators, rotor, spin matrices |
| 4.35–4.45 | [35-45.tex](tex/35-45.tex) | Spin dynamics, coupled spin, minimal coupling, gauge covariance and AB ring |
| 4.46–4.62 | [46-62.tex](tex/46-62.tex) | 3D harmonic oscillator, virial theorem, hydrogen momentum space, spin correlations |
| 4.63–4.76 | [63-76.tex](tex/63-76.tex) | Spherical harmonic normalization, 3-spin multiplets, confined hydrogen, spin measurements, Stern–Gerlach, magnetic flux |

## Reproduce the manuscript

From the repository root, with Python and TeX Live installed:

~~~bash
python3 -m pip install numpy scipy matplotlib
python3 chapter4/scripts/verify.py
cd chapter4
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The completed PDF appears at \`chapter4/main.pdf\` and the numerical figures at \`chapter4/figures/\`.

The independent [numerical script](scripts/verify.py) checks the special degeneracy of the 3D cubical well, spherical Bessel roots, radial hydrogen normalizations, spin matrices, gravitational analogy, and the three lowest confined-hydrogen eigenvalues in each of the \(\ell=0,1,2\) sectors. It plots radial hydrogen distributions and spherical Bessel modes.

GitHub Actions [Chapter 4 validation](../.github/workflows/chapter4-check.yml) compiles the PDF and checks that all 76 problem numbers occur in order. The [Pages publishing workflow](../.github/workflows/pages.yml) publishes Chapters 1–4 and their compiled PDFs in the same Pages site without replacing earlier chapters.

## Modelling and mathematical scope

- A spherical hydrogen atom confined to a hard-wall **volume** is distinct from a particle constrained to the surface of a sphere. Near-boundary and excited-level energies can differ markedly from free hydrogen.
- Physical spin-\(1/2\) is represented by a spinor rather than a spatial rotation of an extended charged sphere.
- Coulomb hydrogen calculations use the Bohr-radius convention stated in the manuscript; where nuclear recoil is ignored, \(m\) is the electron mass.
- Ideal gauge-phase results assume the electromagnetic vector potentials and boundary conditions specified by the textbook. For actual implementations additional experimental effects may matter.
- Numerical matrix spectra are finite-grid approximations. All displayed parameter choices and units are stated; comparisons with unconfined hydrogen require explicit finite-size convergence checks.

**Reference:** Griffiths & Schroeter (2018), Chapter 4, DOI [10.1017/9781316995433](https://doi.org/10.1017/9781316995433).

Maintained by [Kumar Azad](https://github.com/KrAzad0).