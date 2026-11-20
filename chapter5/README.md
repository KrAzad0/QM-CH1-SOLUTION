# Chapter 5 — Identical Particles

**39 original worked solutions, numbered 5.1–5.39**, following D. J. Griffiths and D. F. Schroeter, *Introduction to Quantum Mechanics*, 3rd ed., Chapter 5.

- **Website:** https://krazad0.github.io/QM-CH1-SOLUTION/chapter5/
- **PDF:** https://krazad0.github.io/QM-CH1-SOLUTION/chapter5/chapter-5-solutions.pdf
- [Main LaTeX source](main.tex)
- [Numerical verification script](scripts/verify.py)

| Exercises | LaTeX source | Main topics |
|---|---|---|
| 5.1–5.8 | [01-08.tex](tex/01-08.tex) | Reduced mass, exchange, two-particle well and oscillator |
| 5.9–5.16 | [09-16.tex](tex/09-16.tex) | Spin, Slater determinants, Laughlin, helium, lithium |
| 5.17–5.23 | [17-23.tex](tex/17-23.tex) | Atomic terms, Hund rules, Fermi gas, copper |
| 5.24–5.28 | [24-28.tex](tex/24-28.tex) | Bloch bands and a delta-function comb |
| 5.29–5.34 | [29-34.tex](tex/29-34.tex) | Counting, 2D Fermi energy, paramagnetism, Stoner |
| 5.35–5.39 | [35-39.tex](tex/35-39.tex) | White dwarf, density of states, phonon modes, periodic Fermi gas |

## Reproduce

From the repository root (requires Python 3 and a TeX distribution):

~~~bash
python3 -m pip install numpy scipy matplotlib
python3 chapter5/scripts/verify.py
cd chapter5
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The script writes plots into \`chapter5/figures/\` and checks several analytic predictions numerically. The compiled manuscript is \`chapter5/main.pdf\`.

The [CI test workflow](../.github/workflows/chapter5-check.yml) verifies all 39 problem numbers, numerical checks, figures and LaTeX compilation. The [Pages publishing workflow](../.github/workflows/pages.yml) publishes Chapters 1–5 and PDFs together.

**Important:** These solutions are an independent educational companion with paraphrased problem descriptions, not the copyrighted textbook questions and not an official solutions manual. The arXiv-inspired academic style does **not** imply an arXiv submission or peer review. Some physical models are deliberately simplified, as the manuscript states.

Reference: Griffiths & Schroeter (2018), Chapter 5, [book DOI](https://doi.org/10.1017/9781316995433). Maintained by [Kumar Azad](https://github.com/KrAzad0).