#!/usr/bin/env python3
"""Reproducible checks and plots for Quantum Mechanics Ch. 3.

Run: python chapter3/scripts/plots.py
Requires numpy, scipy, matplotlib. Figures appear in chapter3/figures.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import simpson
from scipy.special import erf

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(parents=True,exist_ok=True)

def verify(name, value, expected, tolerance=1e-8):
    assert np.isclose(value, expected, rtol=tolerance, atol=tolerance), (
        f"{name}: {value} != {expected}"
    )
    print(f"PASS {name}: {value:.10g}")

def ground_momentum():
    # Problem 3.11, oscillator units: hbar=m=omega=1
    verify("oscillator momentum tail", 1-erf(1), 0.15729920705028513)
    verify("oscillator momentum Gaussian norm",
           simpson(np.exp(-np.linspace(-10,10,40001)**2)/np.sqrt(np.pi),
                   x=np.linspace(-10,10,40001)),1)

def well_momentum(n, q):
    """Stable exact Fourier transform in a=hbar=1 units, q=pa/hbar."""
    k = n*np.pi
    # np.sinc(y/pi) = sin(y)/y, including the removable zeros.
    first = np.exp(0.5j*(k-q))*np.sinc((k-q)/(2*np.pi))
    second = np.exp(-0.5j*(k+q))*np.sinc((k+q)/(2*np.pi))
    return (first-second)/(2j*np.sqrt(np.pi))

def well_plots():
    # Problem 3.34. Fourier normalization of a sine eigenmode.
    q = np.linspace(-1000,1000,250001)
    fig, ax = plt.subplots(figsize=(9,5.3))
    for n in (1,2,5,10):
        density = np.abs(well_momentum(n,q))**2
        pnorm = simpson(density,x=q)
        verify(f"well n={n}: momentum normalization",pnorm,1,tolerance=1e-5)
        moment2 = simpson(q*q*density,x=q)
        target = (n*np.pi)**2
        assert abs(moment2-target)/target < 0.002, (
            "p^2 integral needs a larger cutoff: " + str((n,moment2,target))
        )
        print(f"PASS well n={n}: <(pa/hbar)^2> = {moment2:.5f} "
              f"(exact {target:.5f}, truncated at |q|<=1000)")
        qq = np.linspace(-36,36,3201)
        ax.plot(qq,np.abs(well_momentum(n,qq))**2,label=f"n={n}")
    ax.set(xlabel="Dimensionless momentum q = p a / ℏ",
           ylabel="Momentum probability density in q",
           title="Infinite square well: momentum representation (Problem 3.34)")
    ax.legend()
    ax.grid(alpha=.2)
    fig.tight_layout()
    fig.savefig(OUT/"momentum_well.pdf")
    fig.savefig(OUT/"momentum_well.png",dpi=180)
    plt.close(fig)

def coherent_plot():
    # Problem 3.42. m=omega=hbar=1; C=2.0 and phase=0.
    x=np.linspace(-8,8,1800)
    C=2.
    fig, ax=plt.subplots(figsize=(9,5.3))
    for theta in (0,np.pi/3,2*np.pi/3,np.pi):
        center=C*np.cos(theta)
        rho=np.exp(-(x-center)**2)/np.sqrt(np.pi)
        verify(f"coherent state norm t={theta:.2f}",simpson(rho,x=x),1,tolerance=1e-5)
        ax.plot(x,rho,label=f"ωt={theta/np.pi:.2g}π")
    ax.set(xlabel="Position x (oscillator length units)",
           ylabel="Probability density",
           title="Coherent state: translation with constant width")
    ax.legend()
    ax.grid(alpha=.2)
    fig.tight_layout()
    fig.savefig(OUT/"coherent.pdf")
    fig.savefig(OUT/"coherent.png",dpi=180)
    plt.close(fig)

def matrix_checks():
    # Problem 3.25.
    H=np.array([[1,1],[1,-1]],float)
    vals=np.linalg.eigvalsh(H)
    np.testing.assert_allclose(vals,[-np.sqrt(2),np.sqrt(2)])
    print("PASS two-level Hermitian eigenvalues ±√2")
    # Problem 3.26.
    a=np.array([1j,-2,-1j])
    b=np.array([1j,0,2])
    verify("Re <alpha|beta>",np.vdot(a,b).real,1)
    verify("Im <alpha|beta>",np.vdot(a,b).imag,2)
    np.testing.assert_allclose(np.outer(a,b.conj()),
        [[1,0,2j],[2j,0,-4],[-1,0,-2j]])
    print("PASS complex outer-product matrix")
    # Problem 3.33.
    verify("sequential measurement p(a1)",(9**2+16**2)/25**2,337/625)
    # Problem 3.44, time-unit hbar=1.
    H3=np.array([[3,0,1],[0,5,0],[1,0,3]],float)
    from scipy.linalg import expm
    t=.7
    u=expm(-1j*H3*t)
    expected=np.exp(-3j*t)*np.array([np.cos(t),0,-1j*np.sin(t)])
    np.testing.assert_allclose(u@np.array([1,0,0]),expected,atol=1e-12)
    print("PASS coupled three-level exact time evolution")
    # Problem 3.46: probabilities sum to unity for all three operators.
    rng=np.random.default_rng(2026)
    c=rng.normal(size=3)+1j*rng.normal(size=3)
    c=c/np.linalg.norm(c)
    for t in (0,.4,1.3):
        v=np.array([c[0]*np.exp(-1j*t),
          c[1]*np.exp(-2j*t), c[2]*np.exp(-2j*t)])
        pa=[abs((v[0]+v[1])/np.sqrt(2))**2,
            abs((v[0]-v[1])/np.sqrt(2))**2,
            abs(v[2])**2]
        pb=[abs(v[0])**2,
            abs((v[1]+v[2])/np.sqrt(2))**2,
            abs((v[1]-v[2])/np.sqrt(2))**2]
        verify(f"three-level A sum t={t}",sum(pa),1)
        verify(f"three-level B sum t={t}",sum(pb),1)

def uncertainty_checks():
    # Problem 3.36. sigma_x=a, sigma_p=hbar/(sqrt(2)*a)
    verify("Lorentzian uncertainty product / hbar",1/np.sqrt(2),0.7071067811865476)
    # Problem 3.20: check Mandelstam-Tamm bound for all sample times.
    pi=np.pi
    theta=np.linspace(0,2*pi,1000)
    sx2=1/12-5/(16*pi*pi)-256/(81*pi**4)*np.cos(theta)**2
    assert np.min(sx2)>0
    speed=16/(3*pi**2)*np.abs(np.sin(theta))  # units a*Omega
    sh=1.5 # units hbar*Omega
    bound=np.divide(sh*np.sqrt(sx2),speed,
      out=np.full_like(speed,np.inf),where=speed>1e-10)
    assert bound.min()>0.5
    print("PASS box superposition energy-time uncertainty")

def main():
    ground_momentum()
    well_plots()
    coherent_plot()
    matrix_checks()
    uncertainty_checks()
    print("ALL CHAPTER 3 NUMERICAL CHECKS PASSED")

if __name__ == "__main__":
    main()
