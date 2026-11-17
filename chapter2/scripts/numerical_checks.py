#!/usr/bin/env python3
"""Numerical cross-checks and reusable plots for Griffiths chapter 2.

Outputs are not substitutes for the derivations in ../tex/.
Dependencies: numpy, scipy, matplotlib. Run from any directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal
from scipy.special import airy, ai_zeros
from scipy.optimize import brentq
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)


def check(name: str, actual: float, expected: float, tolerance: float = 1e-6):
    assert abs(actual - expected) <= tolerance * max(1, abs(expected)), (
        f"{name}: got {actual}, expected {expected}"
    )
    print(f"PASS {name}: {actual:.9g}")


def double_delta():
    print("\nProblem 2.27: double delta well")
    for t in (1.0, 0.25):
        even = brentq(lambda q: q - t * (1 + np.exp(-2 * q)), 1e-8, 2 * t + 1)
        print(f"kappa0*a={t:.2f}: even q={even:.9f}")
        if 2 * t > 1:
            odd = brentq(lambda q: q - t * (1 - np.exp(-2 * q)), 1e-8, 2 * t + 1)
            print(f" odd q={odd:.9f}")


def half_well():
    print("\nProblem 2.48: hard wall finite well")
    z0 = 8.0
    roots = []
    for lo, hi in (
        (np.pi / 2 + 1e-7, np.pi - 1e-7),
        (3 * np.pi / 2 + 1e-7, 2 * np.pi - 1e-7),
        (5 * np.pi / 2 + 1e-7, z0 - 1e-7),
    ):
        roots.append(brentq(lambda z: -z / np.tan(z) - np.sqrt(z0**2 - z**2), lo, hi))
    z = roots[-1]
    q = np.sqrt(z0**2 - z**2)
    inside = 0.5 - np.sin(2 * z) / (4 * z)
    outside = np.sin(z) ** 2 / (2 * q)
    check("highest state outside probability", outside / (inside + outside), 0.54204070360699)
    print("bound-state k*a =", np.array(roots))


def bouncing_ball():
    print("\nProblem 2.59: quantum bouncing ball")
    zeros = -ai_zeros(10)[0]
    lam1, lam10 = zeros[0], zeros[9]
    check("lambda1", lam1, 2.3381074104597674)
    check("lambda10", lam10, 12.828776752865757)
    z = np.linspace(0, 16, 800)
    fig, ax = plt.subplots(figsize=(8, 5))
    for lam, label in ((lam1, "n=1"), (lam10, "n=10")):
        airy_prime = abs(airy(-lam)[1])
        y = airy(z - lam)[0] / airy_prime
        ax.plot(z, y, label=label)
        sd_x = 2 * lam / np.sqrt(45)
        sd_p = np.sqrt(lam / 3)
        print(f"n={label}, norm={1/airy_prime:.7f}, sigma_x(z)={sd_x:.7f}, "
              f"sigma_p/(hbar*a)={sd_p:.7f}, product/hbar={sd_x*sd_p:.7f}")
    overlap, err = quad(
        lambda z: airy(z - lam1)[0] * airy(z - lam10)[0]
        / (abs(airy(-lam1)[1]) * abs(airy(-lam10)[1])),
        0, 55, epsabs=1e-12
    )
    check("ground/tenth overlap", overlap, 0, 1e-8)
    ax.set(xlabel="Dimensionless height z = a_g x",
           ylabel="Normalized wavefunction y(z)",
           title="Quantum bouncing ball: Airy bound states")
    ax.axhline(0, linewidth=.7, color="gray")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "bouncing_ball.pdf")
    fig.savefig(OUT / "bouncing_ball.png", dpi=180)
    plt.close(fig)


def finite_difference_box():
    print("\nProblem 2.61: finite-difference infinite well")
    for n in (1, 2, 3, 10, 100):
        d = np.full(n, 2 * (n + 1) ** 2, dtype=float)
        e = np.full(n - 1, -(n + 1) ** 2, dtype=float)
        vals = eigh_tridiagonal(d, e, eigvals_only=True)
        print(f"N={n}: first five (or fewer) E / E* = {vals[:5]}")
        analytic = 4 * (n + 1) ** 2 * np.sin(
            np.pi * np.arange(1, n + 1) / (2 * (n + 1))
        ) ** 2
        np.testing.assert_allclose(vals, analytic, rtol=1e-10, atol=1e-9)
    modes = np.arange(1, 6)
    fig, ax = plt.subplots(figsize=(8, 5))
    for n, marker in ((10, "o"), (100, "s")):
        vals = 4 * (n + 1) ** 2 * np.sin(np.pi * modes / (2 * (n + 1))) ** 2
        ax.plot(modes, vals, marker=marker, label=f"N={n} grid")
    ax.plot(modes, np.pi**2 * modes**2, "k--", label="Exact n²π²")
    ax.set(xlabel="Quantum number n", ylabel="Energy / E*",
           title="Finite-difference convergence of box energies")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "box_convergence.pdf")
    fig.savefig(OUT / "box_convergence.png", dpi=180)
    plt.close(fig)


def sinusoidal_well():
    print("\nProblem 2.62: sinusoidal well bottom (N=100)")
    n = 100
    j = np.arange(1, n + 1)
    x = j / (n + 1)
    v = 500 * np.sin(np.pi * x)
    d = 2 * (n + 1) ** 2 + v
    e = np.full(n - 1, -(n + 1) ** 2, dtype=float)
    vals, vecs = eigh_tridiagonal(d, e, select="i", select_range=(0, 2))
    target = (304.6595591, 304.80036733, 476.16269954)
    for idx, value in enumerate(vals):
        check(f"sinusoidal well E{idx+1} / E*", value, target[idx])
    dx = 1 / (n + 1)
    fig, ax = plt.subplots(figsize=(8, 5))
    for mode in range(3):
        psi = vecs[:, mode] / np.sqrt(dx)
        # Scale and offset each mode for visual comparison.
        ax.plot(x, psi + 3 * mode, label=f"mode {mode+1}, E={vals[mode]:.3f} E*")
    ax.set(xlabel="x/a", ylabel="Wavefunctions (vertically offset)",
           title="First three states in a sinusoidal-bottom square well")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT / "sinusoidal_well.pdf")
    fig.savefig(OUT / "sinusoidal_well.png", dpi=180)
    plt.close(fig)


def main():
    double_delta()
    half_well()
    bouncing_ball()
    finite_difference_box()
    sinusoidal_well()
    print("\nAll numerical checks passed.")


if __name__ == "__main__":
    main()
