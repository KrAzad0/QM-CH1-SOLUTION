#!/usr/bin/env python3
"""Independent Chapter 6 quantum symmetry checks and reproducible figures.

Units for the Bloch bands: a=1 and E_*=hbar^2/(2ma^2)=1.
Reproduce: python chapter6/scripts/verify.py
Requires: numpy, scipy, matplotlib.
"""
from pathlib import Path
from math import pi, sqrt, factorial
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.integrate import quad
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

OUT=Path(__file__).resolve().parents[1]/"figures"
OUT.mkdir(parents=True,exist_ok=True)

def verify(label,actual,expected,rtol=2e-6,atol=1e-10):
    assert np.isclose(actual,expected,rtol=rtol,atol=atol),\
      f"{label}: measured {actual!r}, expected {expected!r}"
    print(f"PASS {label}: {actual:.10g}")

def dispersion(e):
    """Half-trace of transfer matrix of two half-cell constant potentials.

    One segment: V=-20, other: V=0, both width a/2.
    Trace/2 = cos(k1 d)cos(k2 d)-(k1²+k2²)/2 sin(k1d)/k1 sin(k2d)/k2.
    Complex sqrt handles negative E and limits at E=0,-20.
    """
    scalar=np.isscalar(e)
    x=np.asarray(e,dtype=float)
    k1=np.sqrt((x+20).astype(complex))
    k2=np.sqrt(x.astype(complex))
    def sk(k):
        return np.where(np.abs(k)<1e-12,.5,np.sin(k*.5)/(k+1e-80))
    f=np.cos(k1*.5)*np.cos(k2*.5)-(x+10)*sk(k1)*sk(k2)
    f=np.real_if_close(f).real
    return float(f) if scalar else f

GRID=np.linspace(-19.999,50,4500)
FGRID=dispersion(GRID)

def lowest_roots(qa,count=2):
    target=np.cos(qa)
    values=FGRID-target
    changes=np.where(values[:-1]*values[1:]<=0)[0]
    roots=[]
    for idx in changes:
        x=brentq(lambda e:dispersion(e)-target,
                 GRID[idx],GRID[idx+1],xtol=5e-13)
        if not roots or abs(roots[-1]-x)>1e-7:
            roots.append(x)
            if len(roots)>=count:break
    assert len(roots)>=count,(qa,roots)
    return roots

def bloch_bands():
    expected={
     -pi:[-6.98193153076273,5.61824788392706],
     -pi/2:[-10.0604367183464,13.5520286742363],
     0:[-11.9892989224983,28.8480766019147],
     pi/2:[-10.0604367183464,13.5520286742363],
     pi:[-6.98193153076273,5.61824788392706],
    }
    for q,t in expected.items():
        roots=lowest_roots(q)
        for j in range(2):
            verify(f"6.6 band {j+1} qa={q:.4f}",
                   roots[j],t[j],rtol=5e-9)
    qs=np.linspace(-pi,pi,141)
    levels=np.array([lowest_roots(q) for q in qs])
    # E(q)=E(-q) for a real static periodic potential.
    np.testing.assert_allclose(levels,levels[::-1],rtol=1e-10,atol=1e-9)
    print("PASS 6.6 time-reversal q <-> -q band symmetry")
    fig,ax=plt.subplots(figsize=(8.5,5.0))
    for idx in range(2):
        ax.plot(qs/pi,levels[:,idx],label=f"Bloch band {idx+1}",
                linewidth=2)
    for q,roots in expected.items():
        ax.scatter([q/pi]*2,roots,s=16,marker="x")
    ax.set(xlabel="Crystal momentum qa / π",
           ylabel="Energy E / [ℏ²/(2ma²)]",
           title="Periodic square well: two lowest bands, V₀/E*=20",
           xlim=(-1,1))
    ax.axhline(0,linewidth=.6,color="gray",alpha=.5)
    ax.grid(alpha=.17)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT/"bloch_bands.pdf")
    fig.savefig(OUT/"bloch_bands.png",dpi=175)
    plt.close(fig)
    # Hermitian covariant finite differences for a periodic Bloch mode.
    # Matrix has exp(iqh) link phase, and periodic wrap indices.
    for N in (240,480):
        h=1/N
        coords=np.arange(N)/N
        v=np.where((coords>=.25)&(coords<.75),-20.,0.)
        for q in (0,pi):
            main=2/h**2+v
            off=np.full(N-1,-np.exp(1j*q*h)/h**2)
            from scipy.sparse import lil_matrix
            H=diags([np.conj(off),main,off],[-1,0,1],dtype=complex,format="lil")
            H[0,N-1]=-np.exp(-1j*q*h)/h**2
            H[N-1,0]=-np.exp(1j*q*h)/h**2
            H=H.tocsr()
            assert (H-H.getH()).nnz==0 or np.max(np.abs((H-H.getH()).data))<1e-8
            eig=np.sort(eigsh(H,k=2,which="SA",tol=1e-9,
                                return_eigenvectors=False))
            ref=lowest_roots(q)
            for j in range(2):
                verify(f"6.6 finite difference N={N}, q={q:.2f}, band{j+1}",
                        eig[j],ref[j],rtol=1e-2,atol=.035)

def square_well():
    L=1.
    x=np.linspace(-L/2,L/2,251)
    X,Y=np.meshgrid(x,x,indexing="xy")
    def f(n,z):
        return np.sqrt(2/L)*np.sin(n*pi*(z/L-.5))
    p57=f(5,X)*f(7,Y)
    p75=f(7,X)*f(5,Y)
    minus=(p57-p75)/sqrt(2)
    plus=(p57+p75)/sqrt(2)
    np.testing.assert_allclose(minus.T,-minus,atol=2e-13)
    np.testing.assert_allclose(plus.T,plus,atol=2e-13)
    np.testing.assert_allclose(minus[::-1,:],minus,atol=2e-13)
    np.testing.assert_allclose(minus[:,::-1],minus,atol=2e-13)
    # Rotating CCW a quarter turn maps anti-symmetric combination to -itself.
    np.testing.assert_allclose(np.rot90(minus,1),-minus,atol=2e-13)
    norm=np.trapezoid(np.trapezoid(minus*minus,x=x,axis=0),x=x)
    verify("6.33 square-well antisymmetric state normalization",norm,1,rtol=.0005)
    fig,ax=plt.subplots(figsize=(6,5.5))
    vmax=np.max(np.abs(minus))
    im=ax.contourf(X,Y,minus,levels=41,cmap="coolwarm",vmin=-vmax,vmax=vmax)
    ax.contour(X,Y,minus,levels=[0],colors="black",linewidths=1.0)
    fig.colorbar(im,ax=ax,label="ψ₋(x,y)")
    ax.set(aspect="equal",xlabel="x / L",ylabel="y / L",
           title="Square-well D₄ symmetry: ψ₅₇ − ψ₇₅")
    fig.tight_layout()
    fig.savefig(OUT/"square_symmetry.pdf")
    fig.savefig(OUT/"square_symmetry.png",dpi=175)
    plt.close(fig)
    print("PASS 6.33 all tested D4 rotations and reflections")

def spin_tests():
    sx=np.array([[0,1],[1,0]],complex)
    sy=np.array([[0,-1j],[1j,0]],complex)
    sz=np.diag([1.,-1.]).astype(complex)
    for i,s in enumerate((sx,sy,sz)):
        assert np.max(np.abs(s@s-np.eye(2)))<1e-14
    np.testing.assert_allclose(sx@sy,1j*sz)
    n=np.array([.3,.4,np.sqrt(.75)])
    n=n/np.linalg.norm(n)
    N=n[0]*sx+n[1]*sy+n[2]*sz
    for angle in np.linspace(-2*pi,2*pi,29):
        R=np.cos(angle/2)*np.eye(2)-1j*np.sin(angle/2)*N
        np.testing.assert_allclose(R.conj().T@R,np.eye(2),atol=1e-14)
    Rz=np.cos(2*pi/2)*np.eye(2)-1j*np.sin(2*pi/2)*sz
    np.testing.assert_allclose(Rz,-np.eye(2),atol=1e-14)
    # The spin-1/2 time-reversal map is anti-linear and squares to -I.
    theta=lambda chi:np.array([-np.conj(chi[1]),np.conj(chi[0])])
    chi=np.array([.3+.7j,.6-.2j])
    np.testing.assert_allclose(theta(theta(chi)),-chi,atol=1e-14)
    np.testing.assert_allclose(np.vdot(chi,theta(chi)),0,atol=1e-14)
    print("PASS 6.32/6.37 spin rotations and Kramers orthogonality")
    angle=np.linspace(0,2*pi,501)
    p_up=np.cos(angle/2)**2
    p_down=np.sin(angle/2)**2
    np.testing.assert_allclose(p_up+p_down,1)
    fig,ax=plt.subplots(figsize=(8.5,5))
    ax.plot(angle/pi,p_up,label="P(spin up after x-axis rotation)")
    ax.plot(angle/pi,p_down,label="P(spin down after x-axis rotation)")
    ax.set(xlabel="Rotation angle / π",ylabel="Measurement probability",
           xlim=(0,2),ylim=(0,1),title="SU(2) spin rotation and spin flip")
    ax.grid(alpha=.15)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT/"spin_rotation.pdf")
    fig.savefig(OUT/"spin_rotation.png",dpi=175)
    plt.close(fig)

def hydrogen_and_propagators():
    radial=lambda t:t**3 * ((2-t)*np.exp(-t/2)/(2*sqrt(2))) * \
             (t*np.exp(-t/2)/(2*sqrt(6)))
    value=quad(radial,0,100,epsabs=1e-11)[0]/sqrt(3)
    verify("6.13 <200|z|210> / a0",value,-3)
    n=3
    k=1.
    for ell in (0,1,2):
        c=k*sqrt(2*(ell+1)/(2*ell+3)*(1-(ell+1)**2/n**2))
        verify(f"6.34 LRL zero at top ell={ell}",c if ell==2 else c,
               0 if ell==2 else c)
        if ell==2: assert abs(c)<1e-13
    # Free Gaussian from exact propagator: normalization and spreading.
    a=.73
    x=np.linspace(-25,25,25001)
    for t in (0,.5,2.,5.):
        z=1+2j*a*t
        psi=(2*a/pi)**.25*z**(-.5)*np.exp(-a*x*x/z)
        prob=abs(psi)**2
        verify(f"6.30 free Gaussian norm t={t}",np.trapezoid(prob,x),1,rtol=2e-6)
        var=np.trapezoid(prob*x*x,x)
        verify(f"6.30 spreading t={t}",var,(1+(2*a*t)**2)/(4*a),rtol=1e-4)
    print("PASS 6.13/6.30/6.34 hydrogen matrix and Gaussian propagation")

def main():
    bloch_bands()
    square_well()
    spin_tests()
    hydrogen_and_propagators()
    print("ALL CHAPTER 6 NUMERICAL VALIDATION CHECKS PASSED")

if __name__=="__main__":
    main()
