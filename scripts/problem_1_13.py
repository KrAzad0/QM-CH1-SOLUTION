#!/usr/bin/env python3
"""Reproduce the classical harmonic-oscillator histogram in Problem 1.13."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

def main() -> None:
    rng = np.random.default_rng(20261117)
    n = 10_000
    phases = rng.uniform(0.0, 2.0 * np.pi, n)
    positions = np.cos(phases)
    x = np.linspace(-0.995, 0.995, 1200)
    exact_pdf = 1.0 / (np.pi * np.sqrt(1.0 - x**2))
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.hist(positions, bins=100, range=(-1, 1), density=True,
            alpha=0.65, label="10,000 random snapshots")
    ax.plot(x, exact_pdf, linewidth=2, label=r"$1/(\pi\sqrt{1-x^2})$")
    ax.set(xlim=(-1, 1), xlabel="Position $x/A$", ylabel="Probability density")
    ax.legend()
    fig.tight_layout()
    out = Path(__file__).resolve().parent.parent / "figures"
    out.mkdir(exist_ok=True)
    fig.savefig(out / "problem_1_13.pdf")
    fig.savefig(out / "problem_1_13.png", dpi=180)
    plt.close(fig)
    print(f"N={n}; mean={positions.mean():.6f}; "
          f"sample sd={positions.std(ddof=1):.6f}; "
          f"exact mean=0; exact sd={1/np.sqrt(2):.6f}")

if __name__ == "__main__":
    main()
