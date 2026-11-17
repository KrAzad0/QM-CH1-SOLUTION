# The Wave Function — Interactive Chapter 1 Website

**Study the complete chapter online:** [Open the GitHub Pages website](https://krazad0.github.io/QM-CH1-SOLUTION/)

The website includes a responsive academic design, the six foundational concepts, a searchable and filterable index of **all 18 worked exercises**, links to the LaTeX derivations, a light/dark theme switch, and a **PDF manuscript that is rebuilt and published with the site**.

Website sources live in [docs/](docs/). The publishing workflow is [.github/workflows/pages.yml](.github/workflows/pages.yml). It uses GitHub Pages deployment via Actions and attempts to enable Pages automatically on the first run.

---

# Quantum Mechanics — Chapter 1 Complete Solutions

**An arXiv-inspired mathematical-physics study manuscript** with original step-by-step worked solutions to **Problems 1.1–1.18** in Chapter 1, *The Wave Function*, of Griffiths & Schroeter, *Introduction to Quantum Mechanics*, 3rd edition (Cambridge University Press, 2018).

> **Status:** Course solutions, not a published arXiv preprint or peer-reviewed research article. Problem summaries are independently paraphrased instead of reproducing the textbook verbatim.

## Read and build

The main LaTeX entry point is [main.tex](main.tex). The eighteen worked problems are arranged in the [tex/](tex/) directory, each with derivations and checks.

~~~text
QM-CH1-SOLUTION/
├── main.tex
├── tex/
│   ├── problems-01-06.tex
│   ├── problems-07-09.tex
│   ├── problems-10-13.tex
│   └── problems-14-18.tex
├── scripts/
│   └── problem_1_13.py
├── .github/workflows/latex.yml
└── README.md
~~~

Compile using a current TeX Live installation:

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The resulting PDF is main.pdf. The GitHub Actions **Build LaTeX PDF** workflow builds a downloadable PDF artifact for every push or pull request.

To generate the reproducible comparison plot for **Problem 1.13**, run:

~~~bash
python3 -m pip install numpy matplotlib
python3 scripts/problem_1_13.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

This creates figures/problem_1_13.pdf and figures/problem_1_13.png. When present, the figure is embedded in the LaTeX manuscript.

## Index of all 18 problems

| Problems | Topics |
|---|---|
| 1.1–1.3 | Discrete variance, falling-rock fluctuations, Gaussian statistics |
| 1.4–1.6 | Triangular and exponential wavefunctions, differentiation and integration |
| 1.7–1.9 | Ehrenfest theorem, potential shifts, Gaussian oscillator and uncertainty |
| 1.10–1.13 | Digits of pi, classical oscillator position and momentum, numerical simulation |
| 1.14–1.18 | Current conservation, overlap preservation, compact-support moments, decay models, thermal wavelengths |

## Reference and attribution

D. J. Griffiths and D. F. Schroeter, *Introduction to Quantum Mechanics*, 3rd ed., Cambridge University Press (2018), Chapter 1 (book pages 3–24). DOI: [10.1017/9781316995433](https://doi.org/10.1017/9781316995433).

This is an independently written solution companion, not an official or authorized textbook solutions manual. For exact questions, consult the book. Open GitHub issues for corrections or mathematical questions.

Maintained by [Kumar Azad](https://github.com/KrAzad0).
