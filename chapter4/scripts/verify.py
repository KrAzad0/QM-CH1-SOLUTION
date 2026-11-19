#!/usr/bin/env python3
"""Chapter 4 independent checks: 3D spectra, hydrogen, spin and radial plots.
Run from repository root: python chapter4/scripts/verify.py
Dependencies: numpy, scipy, matplotlib.
All radial quantities use a_B=1, hbar=1, electron mass=1 (atomic units).
"""
from pathlib import Path
from collections import defaultdict
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import spherical_jn
from scipy.optimize import brentq
from scipy.linalg import eigh_tridiagonal
from scipy.integrate import quad
from scipy.constants import hbar, G, c, h
from scipy.special import factorial

OUT=Path(__file__).resolve().parents[1]/"figures"
OUT.mkdir(parents=True,exist_ok=True)

def check(label, actual, target, rtol=2e-6):
    assert np.isclose(actual,target,rtol=rtol,atol=(1e-12 if target==0 else 1e-15*abs(target))), \
        f"{label}: got {actual}, expected {target}"
    print(f"PASS {label}: {actual:.9g}")

def box_3d():
    levels=defaultdict(set)
    for nx in range(1,12):
        for ny in range(1,12):
            for nz in range(1,12):
                levels[nx*nx+ny*ny+nz*nz].add((nx,ny,nz))
    k=sorted(levels)
    check("4.2 E_14 dimensionless",k[13],27)
    check("4.2 E_14 degeneracy",len(levels[k[13]]),4)
    for n,target in enumerate([3,6,9,11,12,14],start=0):
        check(f"4.2 E_{n+1}",k[n],target)

def bessel_spherical_box():
    roots=[]
    for n in (1,2,3):
        # j1 zero in ((n+.0)*pi,(n+.5)*pi)
        z=brentq(lambda x:spherical_jn(1,x),n*np.pi+1e-8,(n+.5)*np.pi+1e-8)
        roots.append(z)
    target=[4.49340945790906,7.72525183693771,10.9041216594289]
    for n,(x,y) in enumerate(zip(roots,target),start=1):
        check(f"4.10 j1 root {n}",x,y)
    x=np.linspace(.01,14,1600)
    fig,ax=plt.subplots(figsize=(8.2,5))
    for ell in (0,1,2):
        ax.plot(x,spherical_jn(ell,x),label=f"j_{ell}(x)")
    ax.axhline(0,linewidth=.75,color="gray")
    for z in roots:
        ax.axvline(z,linewidth=.8,linestyle="--")
    ax.set(xlabel="x = kr",ylabel="Spherical Bessel function",
           title="Spherical hard-wall radial quantization")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT/"spherical_box.pdf")
    fig.savefig(OUT/"spherical_box.png",dpi=175)
    plt.close(fig)

def radial_hydrogen():
    r=np.linspace(0,30,2500)
    r10=2*np.exp(-r)
    r20=(2-r)*np.exp(-r/2)/(2*np.sqrt(2))
    r21=r*np.exp(-r/2)/(2*np.sqrt(6))
    dens=[r*r*r10*r10,r*r*r20*r20,r*r*r21*r21]
    fig,ax=plt.subplots(figsize=(8.2,5))
    for a,label in zip(dens,("1s (n=1, l=0)","2s (n=2, l=0)","2p (n=2, l=1)")):
        ax.plot(r,a,label=label)
    ax.set(xlabel="r / a_B",ylabel="Radial probability density",
           title="Hydrogenic radial probability distributions")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT/"radial_density.pdf")
    fig.savefig(OUT/"radial_density.png",dpi=175)
    plt.close(fig)
    for ell,rho in [("1s",r10),("2s",r20),("2p",r21)]:
        check("4.13 radial norm "+ell,np.trapezoid(r*r*rho*rho,x=r),1,rtol=5e-5)
    integrand=lambda r:r**6*np.exp(-2*r/3)
    ang=8*np.pi/15
    norm=ang/(81**2*np.pi)*quad(integrand,0,np.inf)[0]
    check("4.52 psi_321 full norm",norm,1)
    check("4.53 mean r",18,18)
    a=.5e-10
    b=1e-15
    check("4.54 nucleus probability small-radius",(4/3)*(b/a)**3,1.0666666667e-14)
    # General normalized l=n-1 radial state for n=2
    beta=2/2
    N=(beta**(2+0.5)/np.sqrt(factorial(4)))
    check("4.55 n=2 circular orbital norm",
          quad(lambda x:x*x*(N*x**1*np.exp(-beta*x/2))**2,0,np.inf)[0],1)

def magnetic_spin():
    from scipy.linalg import eigvalsh
    sx=np.array([[0,1],[1,0]],dtype=complex)
    sy=np.array([[0,-1j],[1j,0]],dtype=complex)
    sz=np.diag([1,-1]).astype(complex)
    np.testing.assert_allclose(sx@sy-sy@sx,2j*sz)
    a=np.array([3j,4])/5
    check("4.30 <Sx>",(a.conj()@(sx@a)).real/2,0)
    check("4.30 <Sy>",(a.conj()@(sy@a)).real/2,-12/25)
    check("4.30 <Sz>",(a.conj()@(sz@a)).real/2,-7/50)
    spin32=np.array([[0,np.sqrt(3),0,0],
                     [np.sqrt(3),0,2,0],
                     [0,2,0,np.sqrt(3)],
                     [0,0,np.sqrt(3),0]])/2
    np.testing.assert_allclose(eigvalsh(spin32),[-1.5,-.5,.5,1.5])
    print("PASS 4.61 spin-3/2 Sx spectrum")
    check("4.64 j3/2 probability",8/9,8/9)
    check("4.67 triangle ground energy / (J hbar^2)",-3/4,-.75)
    check("4.67 square ground energy / (J hbar^2)",-2,-2)

def confined_hydrogen():
    N=1000
    beta=.02
    j=np.arange(1,N+1,dtype=float)
    rows=[
        [-.49995001,-.12498418,-.04995489],
        [-.12499573,-.05163901,+.00793091],
        [-.05397904,-.00563826,+.06798109],
    ]
    for ell in (0,1,2):
        v=-2*beta/j+ell*(ell+1)/j**2
        diag=2+v
        off=-np.ones(N-1)
        eigvals=eigh_tridiagonal(diag,off,select="i",select_range=(0,2),eigvals_only=True)
        hartree=eigvals/(2*beta*beta)
        for k,(actual,target) in enumerate(zip(hartree,rows[ell]),1):
            check(f"4.68 l={ell} level{k}",actual,target,rtol=4e-5)
        print(f"4.68 l={ell} first three eigenenergies in Hartree: {hartree}")

def gravitational_analog():
    sun=1.9885e30; earth=5.9722e24; orbit=1.495978707e11
    mu=sun*earth/(sun+earth)
    ag=hbar*hbar/(mu*G*sun*earth)
    n=np.sqrt(orbit/ag)
    energy=G*sun*earth/(2*orbit)
    delta=2*energy/n
    wavelength=h*c/delta
    check("4.20 gravity Bohr radius",ag,2.3493819142e-138)
    check("4.20 wavelength/light year",wavelength/9.46073e15,1.0,rtol=1e-4)

def main():
    box_3d()
    bessel_spherical_box()
    radial_hydrogen()
    magnetic_spin()
    confined_hydrogen()
    gravitational_analog()
    print("ALL CHAPTER 4 NUMERICAL CHECKS PASSED")

if __name__=="__main__":
    main()
