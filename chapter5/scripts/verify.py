#!/usr/bin/env python3
"""Reproduce numerical and graphical checks for Chapter 5 - Identical Particles.

Run from repo root: python chapter5/scripts/verify.py
Requirements: numpy, scipy, matplotlib. Two PNG/PDF figures are generated.
The figures use dimensionless oscillator units or m=hbar=a=alpha=1.
"""
from pathlib import Path
from math import pi, sqrt, sin, cos
from math import comb, factorial
import numpy as np
from scipy import constants as C
from scipy.optimize import brentq
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parents[1]/"figures"
OUT.mkdir(parents=True,exist_ok=True)

def verify(label, result, expected, rtol=1e-4, atol=1e-12):
    if not np.isclose(result, expected, rtol=rtol, atol=atol):
        raise AssertionError(f"{label}: measured {result}, expected {expected}")
    print(f"PASS {label}: {result:.10g}")

def exchange():
    x=np.linspace(0,7,3000)
    g=np.exp(-x*x/2)/sqrt(2*pi)
    pdfs={
      "Distinguishable":2*0.5*(1+x*x)*g,
      "Bosons":2*g,
      "Fermions":2*x*x*g,
    }
    for label,pdf in pdfs.items():
        verify(f"5.7 {label} distance normalization",np.trapezoid(pdf,x),1,rtol=1e-6)
    for label,expected in (("Distinguishable",2),("Bosons",1),("Fermions",3)):
        verify(f"5.7 {label} mean r^2",np.trapezoid(x*x*pdfs[label],x),expected,rtol=1e-5)
    fig,ax=plt.subplots(figsize=(8.4,5.1))
    for label,pdf in pdfs.items():
        ax.plot(x,pdf,label=label,linewidth=2)
    ax.set(xlabel="Particle separation |x1-x2| / b",
           ylabel="Probability density",
           title="Exchange symmetry and particle separation")
    ax.set_xlim(0,5)
    ax.legend()
    ax.grid(alpha=.2)
    fig.tight_layout()
    for ext in ("png","pdf"):
        fig.savefig(OUT/f"exchange.{ext}",dpi=180)
    plt.close(fig)
    verify("5.29 distinguishable states",3**3,27)
    verify("5.29 bosonic states",comb(5,3),10)
    verify("5.29 fermionic states",comb(3,3),1)
    # Orthogonality of fermionic and symmetric states of two orbitals.
    xgrid=np.linspace(-5,5,5001)
    phi0=np.exp(-xgrid*xgrid/2)/pi**.25
    phi1=np.sqrt(2)*xgrid*phi0
    verify("oscillator phi0 normalization",np.trapezoid(phi0*phi0,xgrid),1)
    verify("oscillator phi1 normalization",np.trapezoid(phi1*phi1,xgrid),1)
    verify("oscillator phi0-phi1 overlap",np.trapezoid(phi0*phi1,xgrid),0)

def bands():
    beta=10
    f=lambda z:np.cos(z)+beta*np.sin(z)/z-1
    z0=brentq(f,2.0,np.pi-1e-8,xtol=1e-13)
    E=z0*z0/(2*beta)  # alpha/a = 1 eV
    verify("5.25 dimensionless band edge",z0,2.6276754329857925,rtol=1e-10)
    verify("5.25 energy in eV",E,0.3452339090558536,rtol=1e-10)
    # Plot first Brillouin zone for m=hbar=a=alpha=1.
    energy=np.linspace(1e-6,30,30000)
    k=np.sqrt(2*energy)
    f=np.cos(k)+np.sin(k)/k
    mask=(np.abs(f)<=1)
    q=np.arccos(f[mask])
    fig,ax=plt.subplots(figsize=(8.4,5.1))
    ax.scatter(q,energy[mask],s=0.23,label="Allowed +q",rasterized=True)
    ax.scatter(-q,energy[mask],s=0.23,label="Allowed -q",rasterized=True)
    ax.set(xlim=(-pi,pi),ylim=(0,30),
           xlabel="Bloch momentum qa (first Brillouin zone)",
           ylabel="E (hbar^2 / (m a^2) units)",
           title="Periodic repulsive delta comb: band structure")
    ax.grid(alpha=.14)
    fig.tight_layout()
    for ext in ("png","pdf"):
        fig.savefig(OUT/f"bands.{ext}",dpi=180)
    plt.close(fig)
    assert mask.any() and (~mask).any()
    print("PASS 5.28 forbidden gaps and allowed bands")
    # Density-of-states comparison: alpha=1.
    dfdK=(-np.sin(k)+np.cos(k)/k-np.sin(k)/k**2)
    dos=np.full_like(energy,np.nan)
    interior=np.abs(f)<0.99999
    dos[interior]=np.abs(dfdK[interior])/(pi*k[interior]*np.sqrt(1-f[interior]**2))
    free=1/(pi*np.sqrt(2*energy))
    fig,ax=plt.subplots(figsize=(8.4,5.1))
    ax.plot(energy,free,label="Free 1D electron, alpha=0")
    ax.plot(energy,dos,label="Delta-comb electron, alpha=1")
    ax.set(xlim=(.02,25),ylim=(0,1.8),
           xlabel="Energy (dimensionless)",
           ylabel="Density of states per length and energy",
           title="1D density of states and band-edge singularities")
    ax.legend()
    fig.tight_layout()
    for ext in ("png","pdf"):
        fig.savefig(OUT/f"dos.{ext}",dpi=180)
    plt.close(fig)

def helium_and_isotopes():
    # Two electrons in an uncorrelated helium 1s (Z=2):
    # <1/r12> = 5Z/(8a_B); in a_B units 5/4.
    Z=2
    b=2*Z
    inner=lambda r:quad(lambda s:s*s*np.exp(-b*s),0,r,epsabs=1e-12)[0]
    I=(b**6/2)*quad(lambda r:r*np.exp(-b*r)*inner(r),0,30,epsabs=1e-10)[0]
    verify("5.15 helium Coulomb integral a_B*I",I,1.25,rtol=1e-5)
    mu35=35/36
    mu37=37/38
    relative=sqrt(mu37/mu35)-1
    verify("5.3 HCl isotope fractional splitting",relative,7.516e-4,rtol=.01)
    verify("5.4 orthogonal exchange normalization",2*(1/sqrt(2))**2,1)

def fermi_gas():
    rho=8.96e3/0.0635*C.N_A
    ef=C.hbar**2/(2*C.m_e)*(3*pi*pi*rho)**(2/3)
    ef_ev=ef/C.e
    speed=sqrt(2*ef/C.m_e)
    tF=ef/C.k
    pressure=(2/5)*rho*ef
    bulk=(5/3)*pressure
    verify("5.21 copper Fermi energy eV",ef_ev,7.03,rtol=.006)
    verify("5.21 copper Fermi velocity",speed,1.57e6,rtol=.01)
    verify("5.21 copper Fermi temperature",tF,8.15e4,rtol=.01)
    verify("5.21 copper degeneracy pressure",pressure,3.83e10,rtol=.01)
    verify("5.23 copper bulk modulus",bulk,6.38e10,rtol=.01)
    mass3=3.01602932265*C.atomic_mass
    rho3=82/mass3
    t3=C.hbar**2*(3*pi*pi*rho3)**(2/3)/(2*mass3*C.k)
    verify("5.22 helium-3 free Fermi temperature K",t3,4.96,rtol=.02)
    alrho=18.1e22*1e6
    alEF=C.hbar**2*(3*pi*pi*alrho)**(2/3)/(2*C.m_e)
    muB=C.physical_constants["Bohr magneton"][0]
    chi=3*C.mu_0*alrho*muB*muB/(2*alEF)
    verify("5.33 aluminum Pauli susceptibility",chi,1.2e-5,rtol=.09)
    print("Aluminum theoretical chi:",chi)

def stars():
    # Same uniformly dense nonrelativistic toy model as the textbook.
    sun=1.9885e30
    nucleon=C.m_p
    N=sun/nucleon
    d=.5
    R=(9*pi/4)**(2/3)*C.hbar**2*d**(5/3)/(C.G*C.m_e*nucleon**2*N**(1/3))
    ne=d*N/(4*pi*R**3/3)
    ef=C.hbar**2/(2*C.m_e)*(3*pi*pi*ne)**(2/3)
    Nc=((5/4)*(9*pi/4)**(1/3)*C.hbar*C.c*d**(4/3)/(C.G*nucleon**2))**1.5
    verify("5.35 white dwarf radius km",R/1e3,7200,rtol=.10)
    verify("5.36 critical nucleon count",Nc,2.04e57,rtol=.06,atol=0)
    print("White dwarf radius km:",R/1e3,
          "Fermi energy keV:",ef/C.e/1e3,
          "critical stellar mass / Msun:",Nc*nucleon/sun)
    # neutron star: one neutron per nucleon
    Rn=(9*pi/4)**(2/3)*C.hbar**2/(C.G*C.m_n**3*N**(1/3))
    nn=N/(4*pi*Rn**3/3)
    efn=C.hbar**2/(2*C.m_n)*(3*pi*pi*nn)**(2/3)
    verify("5.36 neutron-star toy radius km",Rn/1e3,12,rtol=.18)
    print("Neutron-star Fermi energy MeV:",efn/C.e/1e6)

def phonons():
    N=12
    j=np.arange(1,N+1)
    for k in range(1,N):
        for kp in range(1,N):
            a=np.exp(2j*pi*j*(k-kp)/N).sum()/N
            b=np.exp(2j*pi*j*(k+kp)/N).sum()/N
            assert abs(a-(k==kp))<1e-12
            assert abs(b-(kp==N-k))<1e-12
    print("PASS 5.38 phonon DFT orthogonality for N=12")
    # 5.39: periodic block has 8 times hard-wall block volume.
    verify("5.39 periodic vs hard-wall k-block factor",(2*pi)**3/pi**3,8)

def main():
    exchange()
    bands()
    helium_and_isotopes()
    fermi_gas()
    stars()
    phonons()
    print("ALL CHAPTER 5 NUMERICAL CHECKS PASSED")
if __name__=="__main__":
    main()
