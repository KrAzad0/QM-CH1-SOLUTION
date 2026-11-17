# Quantum Mechanics — Chapter 2: Time-Independent Schrödinger Equation

**Independent mathematical-physics solutions to all 64 numbered problems (2.1–2.64)** from Chapter 2 of Griffiths & Schroeter, *Introduction to Quantum Mechanics*, third edition (Cambridge University Press, 2018).

**Interactive Chapter 2 website:** https://krazad0.github.io/QM-CH1-SOLUTION/chapter2/

**Full PDF manuscript:** https://krazad0.github.io/QM-CH1-SOLUTION/chapter2/chapter-2-solutions.pdf

> These are original coursework companion notes with paraphrased problem descriptions, not a reproduction of the textbook, an official solutions manual, a research paper, or an arXiv publication.

## Contents

| Problem range | Source | Main subjects |
|---|---|---|
| 2.1–2.9 | [01-09.tex](tex/01-09.tex) | Stationary states, infinite wells, normalizations, measurement and superpositions |
| 2.10–2.16 | [10-16.tex](tex/10-16.tex) | Harmonic oscillator, ladder algebra, Hermite polynomials |
| 2.17–2.21 | [17-21.tex](tex/17-21.tex) | Free particles, Fourier transforms and Gaussian wave packets |
| 2.22–2.28 | [22-28.tex](tex/22-28.tex) | Dirac deltas, bound states, double-delta transmission |
| 2.29–2.35 | [29-35.tex](tex/29-35.tex) | Finite wells, barriers, step potentials, tunneling |
| 2.36–2.45 | [36-45.tex](tex/36-45.tex) | Centered wells, revivals, cusps, parity and nodal theory |
| 2.46–2.54 | [46-54.tex](tex/46-54.tex) | Ring, double well, coherent motion, reflectionless wells, scattering and transfer matrices |
| 2.55–2.64 | [55-64.tex](tex/55-64.tex) | Numerical spectra, Airy functions, inverse-square potential, finite differences, Einstein heat capacity, Legendre polynomials |

## Compile the manuscript

From the repository root:

~~~bash
cd chapter2
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

This creates chapter2/main.pdf.

To verify the numerical sections and create the figures:

~~~bash
python3 -m pip install numpy scipy matplotlib
python3 chapter2/scripts/numerical_checks.py
cd chapter2
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The [numerical script](scripts/numerical_checks.py) checks double delta roots (2.27), the hard-wall finite well (2.48), the Airy quantization (2.59), finite-difference spectral convergence (2.61), and the sinusoidal well (2.62). It produces Airy, convergence, and eigenfunction plots in figures/.

The GitHub [Chapter 2 validation workflow](../.github/workflows/chapter2-check.yml) builds the PDF and uploads its artifact. The [Pages deployment workflow](../.github/workflows/pages.yml) rebuilds both chapters and publishes them without overwriting the Chapter 1 website.

## Mathematical notes and limitations

Some late-chapter problems require solving transcendental equations or numerical eigenvalue problems. Their equations, computational procedures, and output parameters are provided explicitly. The treatment of the attractive inverse-square singularity includes the self-adjoint boundary-condition caveat; a square-integrable formal solution is not sufficient to define a unique Hamiltonian. Treat numerical matrix spectra as grid-dependent estimates, not exact continuum levels.

**Reference:** D. J. Griffiths and D. F. Schroeter (2018), *Introduction to Quantum Mechanics*, third edition, Chapter 2, pp. 25–90. DOI [10.1017/9781316995433](https://doi.org/10.1017/9781316995433). Consult the textbook for the original questions.

Maintained by [Kumar Azad](https://github.com/KrAzad0).
