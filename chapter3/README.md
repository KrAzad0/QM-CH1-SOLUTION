# Chapter 3 — Formalism (Griffiths & Schroeter)

**49 original, mathematically worked textbook exercises, numbered 3.1–3.49**, from Chapter 3 of David J. Griffiths and Darrell F. Schroeter, *Introduction to Quantum Mechanics*, third edition (Cambridge University Press, 2018).

- **Website:** https://krazad0.github.io/QM-CH1-SOLUTION/chapter3/
- **Manuscript PDF:** https://krazad0.github.io/QM-CH1-SOLUTION/chapter3/chapter-3-solutions.pdf
- **Main LaTeX entry point:** [main.tex](main.tex)
- **Reproducibility checks and plots:** [scripts/plots.py](scripts/plots.py)

This is an independent coursework solutions companion in a research-style manuscript layout. **It is not a published arXiv preprint, not peer reviewed, and not an official solutions manual.** Problem descriptions have been paraphrased rather than reproducing the copyrighted textbook questions; consult the book for exact wording.

## Chapters and detailed source groups

| Problems | LaTeX source | Concepts |
|---|---|---|
| 3.1–3.10 | [01-10.tex](tex/01-10.tex) | Hilbert space, Hermitian operators, eigenfunctions, spectra |
| 3.11–3.22 | [11-22.tex](tex/11-22.tex) | Momentum representation, uncertainty, Ehrenfest |
| 3.23–3.30 | [23-30.tex](tex/23-30.tex) | Projection operators, Dirac notation, matrices, BCH |
| 3.31–3.40 | [31-40.tex](tex/31-40.tex) | Gram–Schmidt, momentum of well, virial theorem, oscillator |
| 3.41–3.49 | [41-49.tex](tex/41-49.tex) | Coherent states, three-level systems, SUSY, self-adjoint domains |

## Reproduce the manuscript and calculations

With an up-to-date TeX Live installation:

~~~bash
cd chapter3
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

To run independent numerical checks and build figures from the repository root:

~~~bash
python3 -m pip install numpy scipy matplotlib
python3 chapter3/scripts/plots.py
cd chapter3
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The plots visualize momentum densities of stationary infinite-well states and translation of a harmonic-oscillator coherent state. Automated checks include two- and three-level matrices, normalization, uncertainty and Gaussian Fourier transforms.

## Mathematical cautions

- Hermitian symmetry on a dense domain does **not** imply self-adjointness. The one-dimensional momentum operator on finite and semi-infinite domains requires domain analysis, as explored in Problem 3.48.
- Ideal momentum eigenfunctions are generalized states, not normalizable functions in \(L^2(\mathbb R)\).
- Commutator formulas for unbounded operators should be interpreted on common invariant domains.
- Gaussian and other analytic formulas assume the real, positive parameters and normalizations stated in their sections.

**Reference:** Griffiths & Schroeter, third ed., Chapter 3, printed pages 91–130. DOI [10.1017/9781316995433](https://doi.org/10.1017/9781316995433).

Maintained by [Kumar Azad](https://github.com/KrAzad0).
