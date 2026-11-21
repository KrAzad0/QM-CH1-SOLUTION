# Chapter 6 — Symmetries & Conservation Laws

**37 independent worked solutions (Problems 6.1–6.37)** following Chapter 6 of D. J. Griffiths and D. F. Schroeter, *Introduction to Quantum Mechanics*, 3rd edition (Cambridge University Press, 2018).

- **Live chapter website:** https://krazad0.github.io/QM-CH1-SOLUTION/chapter6/
- **Published solutions PDF:** https://krazad0.github.io/QM-CH1-SOLUTION/chapter6/chapter-6-solutions.pdf
- **LaTeX manuscript:** [main.tex](main.tex)
- **Reproducible figures and checks:** [scripts/verify.py](scripts/verify.py)

## Numbered solutions

| Problems | LaTeX source | Subjects |
|---|---|---|
| 6.1–6.7 | [01-07.tex](tex/01-07.tex) | Parity, generators, translations, Bloch states, interacting-particle momentum |
| 6.8–6.17 | [08-17.tex](tex/08-17.tex) | Parity operators, hydrogen dipoles, SO(2) rotations, vector transformations |
| 6.18–6.25 | [18-25.tex](tex/18-25.tex) | Free-particle degeneracy, tensor operators, Clebsch–Gordan and Wigner–Eckart relations |
| 6.26–6.31 | [26-31.tex](tex/26-31.tex) | Heisenberg equations, free and oscillator propagators, Gaussian states, spectral translations |
| 6.32–6.34 | [32-34.tex](tex/32-34.tex) | SU(2) spin matrices, D4 square-well symmetry, quantum Runge–Lenz vector |
| 6.35–6.37 | [35-37.tex](tex/35-37.tex) | Galilean boosts, antiunitary time reversal, Kramers degeneracy |

## Reproduce the numerical calculations and PDF

From the repository root, with Python 3.12 and a TeX distribution:

~~~sh
python3 -m pip install numpy scipy matplotlib
python3 chapter6/scripts/verify.py
cd chapter6
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The script generates 3 PNG/PDF scientific plots under \`chapter6/figures/\` and independently checks:

- Periodic square-well Bloch band roots at five crystal momenta against exact transfer-matrix matching (Problem 6.6);
- Hermitian gauge-covariant finite-difference spectra at 240 and 480 grid points for convergence;
- Discrete D4 square-well reflection and quarter-turn identities plus normalization (Problem 6.33);
- Spin-half unitarity and the \`2π\` rotation sign, as well as antiunitary Kramers orthogonality (Problems 6.32, 6.37);
- The exact hydrogen \`2s–2p\` dipole overlap (Problem 6.13), Gaussian propagation (Problem 6.30), and Runge–Lenz termination (Problem 6.34).

GitHub Actions [Chapter 6 validation](../.github/workflows/chapter6-check.yml) checks all 37 numbered exercises, recomputes numerical results, compiles the manuscript and uploads the PDF. [Pages publishing](../.github/workflows/pages.yml) builds all six chapters and publishes the new website and downloadable manuscript without deleting existing chapter pages.

## Academic scope

This is an independently authored **educational solution companion**. The exercise prompts are paraphrased rather than copied; the reader must refer to the textbook for the authoritative problem statements and diagrams.

The symmetry derivations use the active translation/rotation conventions stated in the manuscript. Phase conventions may alter signs in Clebsch–Gordan coefficients or spinor matrices but not measured predictions. Physical systems with external magnetic fields or time-dependent Hamiltonians may not possess time-reversal or continuous time-translation symmetry. Some long exercises are presented as compact reproducible derivations instead of every intermediary algebraic line.

The document is **not** the publisher's solutions manual, an arXiv preprint, or a peer-reviewed paper.

**Reference:** Griffiths & Schroeter (2018), Chapter 6, [DOI 10.1017/9781316995433](https://doi.org/10.1017/9781316995433).

Maintained by [Kumar Azad](https://github.com/KrAzad0).