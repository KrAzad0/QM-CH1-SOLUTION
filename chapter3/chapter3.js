(() => {
  "use strict";
  const problems = [
    ["Square-integrable functions and inner products","HILBERT SPACE","Closure, complex scalar multiplication, positivity and normalization.","L²(a,b) is a Hilbert space"],
    ["Power-law integrability and derivative domains","FUNCTION SPACES","Check when x^ν and its derivative lie in L²(0,1).","ν > −1/2"],
    ["Two definitions of Hermitian operators","HERMITICITY","Polarization identity for quadratic-form symmetry.","⟨f|Qg⟩ = ⟨Qf|g⟩"],
    ["Sums, products and real potentials","OPERATOR ALGEBRA","When Hermitian operators remain symmetric under algebraic operations.","(AB)† = BA"],
    ["Adjoints and raising/lowering operators","ADJOINTS","Conjugates of x, i, derivatives and the ladder operators.","(a₊)† = a₋"],
    ["Angular second derivative and degeneracy","ANGULAR SPECTRUM","Periodic eigenfunctions of d²/dφ².","qₙ = −n²"],
    ["Linear combinations inside a degenerate eigenspace","EIGENFUNCTIONS","Build even/odd eigenfunctions from exp(±x).","cosh x ⟂ sinh x"],
    ["Angular eigenvalue orthogonality","ORTHOGONALITY","Real eigenvalues and Fourier-basis overlaps.","⟨uₘ|uₙ⟩ = δₘₙ"],
    ["Discrete, continuous and mixed spectra","SPECTRAL THEORY","Identify potentials with different kinds of energy spectrum.","Discrete / continuous / mixed"],
    ["Is the well ground state a momentum eigenstate?","MEASUREMENT","A sine standing wave is not a momentum eigenfunction.","p̂ψ₁ ≠ p ψ₁"],
    ["Oscillator ground state in momentum space","MOMENTUM SPACE","Gaussian Fourier transform and classically forbidden momentum.","Poutside ≈ 0.16"],
    ["Momentum conservation for a free wave packet","FOURIER TRANSFORM","Express Φ(p,t) in terms of φ(k) and show invariant density.","|Φ(p,t)|² = const. in time"],
    ["Position operator in momentum representation","REPRESENTATIONS","Derive the dual momentum-space position operator.","x̂ = iħ∂ₚ"],
    ["Commutator identities and functions","OPERATOR ALGEBRA","Prove product rules and [f(x),p] formula.","[f(x),p] = iħ f′(x)"],
    ["Position–energy uncertainty relation","UNCERTAINTY","Apply the generalized uncertainty principle to x and H.","σₓ σᴴ ≥ ħ|⟨p⟩|/(2m)"],
    ["Incompatible operators and common eigenstates","COMPATIBILITY","Nonzero commutators exclude a complete common eigenbasis.","[A,B] ≠ 0"],
    ["Minimum-uncertainty Gaussian states","WAVEFUNCTIONS","Solve the saturation differential equation.","σₓσₚ = ħ/2"],
    ["Ehrenfest equations from the general time derivative","TIME EVOLUTION","Evaluate the expectations for I, H, x and p.","d⟨p⟩/dt = −⟨V′⟩"],
    ["Classical trajectories of quantum means","EHRENFEST","Derive free translation and oscillator motion of ⟨x⟩.","⟨x⟩(t) ∝ cos ωt"],
    ["Energy–time inequality in a two-level box state","DYNAMICS","Compute σᴴ, σₓ and the changing position expectation.","σᴴ Δt ≥ ħ/2"],
    ["Energy–time inequality for a traveling Gaussian","GAUSSIAN PACKET","Evaluate energy variance and characteristic timescale.","σᴴ Δt ≥ ħ/2"],
    ["Relationship of two uncertainty principles","UNCERTAINTY","Reduce energy-time inequality to the position-energy bound.","Δt = σₓ / |d⟨x⟩/dt|"],
    ["Projection operators and their eigenvalues","DIRAC NOTATION","Prove idempotence and identify range/kernel.","P² = P; eigenvalues 0,1"],
    ["Hermitian matrices in any basis","MATRIX REPRESENTATION","Derive Qₘₙ = Qₙₘ* from self-adjointness.","Q = Q†"],
    ["Exact diagonalization of a two-level Hamiltonian","TWO-LEVEL SYSTEMS","Solve eigenvectors and ±√2 eigenvalues.","E± = ±√2 ε"],
    ["Complex bra-ket vectors and outer products","LINEAR ALGEBRA","Construct conjugate duals, inner products and a 3×3 matrix.","⟨α|β⟩ = 1 + 2i"],
    ["Spectral decompositions of observables","SPECTRAL THEOREM","Represent Q and exp(Q) with eigenprojectors.","Q = Σ qₙ |n⟩⟨n|"],
    ["Functions of the derivative operator","OPERATOR FUNCTIONS","Compute sin(D)x⁵ and a derivative-resolvent example.","sin(D)x⁵ = 5x⁴−10x²+1"],
    ["Baker–Campbell–Hausdorff identity","COMMUTATORS","Derive the exponential formula for a central commutator.","eᴬ⁺ᴮ = eᴬeᴮe⁻ᶜᐟ²"],
    ["Position basis to energy basis","BASIS CHANGES","Recover energy amplitudes by completeness.","cₙ = ∫ψₙ* Ψ dx"],
    ["Legendre polynomials by Gram–Schmidt","ORTHOGONAL POLYNOMIALS","Orthonormalize 1, x, x² and x³.","eₙ = √((2n+1)/2) Pₙ"],
    ["Anti-Hermitian operators","ADJOINTS","Prove imaginary spectra and decompose arbitrary operators.","Q† = −Q"],
    ["Sequential noncommuting measurements","MEASUREMENT THEORY","Track three projective measurements of A, B and A.","P(final a₁) = 337/625"],
    ["Momentum wavefunction of an infinite well","CONTINUOUS SPECTRA","Fourier transform well eigenstates and study momentum peaks.","⟨p²⟩ = (nπħ/a)²"],
    ["Finite plane-wave train and uncertainty","FOURIER ANALYSIS","Understand sinc momentum distributions and infinite variance.","wₓwₚ = 4πħ"],
    ["Lorentzian-amplitude wavefunction","EXPECTATION VALUES","Normalize, Fourier transform and verify uncertainty.","σₓσₚ = ħ/√2"],
    ["Virial theorem and the harmonic oscillator","CONSERVATION","Derive 2⟨T⟩ = ⟨xV′⟩ from Ehrenfest.","⟨T⟩ = ⟨V⟩"],
    ["Energy and orthogonalization time","QUANTUM SPEED LIMIT","Test the energy-time relation for two stationary states.","σᴴ τ/π = ħ/2"],
    ["Position and momentum oscillator matrices","MATRIX MECHANICS","Compute infinite tridiagonal matrices for x and p.","Hₙₙ = (n+½)ħω"],
    ["General oscillator expectation motion","EHRENFEST","Derive universal classical-frequency motion of ⟨x⟩.","⟨x⟩ = C cos(ωt−φ)"],
    ["Maximum momentum expectation of two levels","COHERENT SUPERPOSITION","Optimize relative phase for n=0 and n=1.","max ⟨p⟩ = √(mħω/2)"],
    ["Coherent states of a harmonic oscillator","COHERENT STATES","Derive expansion coefficients, moments and fixed widths.","a|α⟩ = α|α⟩"],
    ["Robertson–Schrödinger uncertainty bound","GENERALIZED UNCERTAINTY","Include covariance in the stronger uncertainty relation.","σ²ᴬσ²ᴮ ≥ (⟨C⟩²+⟨D⟩²)/4"],
    ["Dynamics of a coupled three-level matrix","FINITE-DIMENSIONAL QM","Exponentiate a 2×2 off-diagonal coupling inside a 3×3 Hamiltonian.","Population oscillation sin²(bt/ħ)"],
    ["Position acting on energy-basis coefficients","OPERATOR MATRIX","Show that position mixes adjacent oscillator levels.","x couples n ↔ n±1"],
    ["Spectra and measurements in a three-level system","QUANTUM COMPUTATION","Find eigenbases, expectations and measurement probabilities.","Three observable matrices"],
    ["Supersymmetric partner potentials","SUSY QUANTUM MECHANICS","Factorize Hamiltonians and derive delta-well partners.","V₂ = const + αδ(x)"],
    ["Self-adjoint momentum domains","FUNCTIONAL ANALYSIS","Distinguish symmetry and self-adjointness on finite/half lines.","|λ| = 1 on [0,a]"],
    ["Traveling Gaussian in momentum space","QUANTUM DYNAMICS","Solve free momentum evolution and compute mean energy.","⟨H⟩ = ⟨p⟩²/(2m)+⟨H⟩₀"]
  ];

  const groups=[
    [1,10,"01-10.tex"],
    [11,22,"11-22.tex"],
    [23,30,"23-30.tex"],
    [31,40,"31-40.tex"],
    [41,49,"41-49.tex"]
  ];
  const list=document.getElementById("problem-list");
  if(!list){return;}

  const el=(tag,cl,txt)=>{
    const node=document.createElement(tag);
    if(cl)node.className=cl;
    if(txt!==undefined)node.textContent=txt;
    return node;
  };

  problems.forEach(([title,topic,summary,result],i)=>{
    const number=i+1;
    const card=el("article","problem-card");
    card.id="problem-3-"+number;
    card.dataset.group=number<=30?"section":"further";
    card.dataset.terms=("3."+number+" "+title+" "+topic+" "+summary+" "+result).toLowerCase();
    const digit=el("div","problem-number",String(number).padStart(2,"0")+" / 49");
    const content=el("div","problem-content");
    content.append(
      el("span","problem-category",topic),
      el("h3","",title),
      el("p","",summary),
      el("div","result-line",result)
    );
    const file=groups.find(g=>number>=g[0]&&number<=g[1])[2];
    const a=el("a","problem-link","Full derivation ↗");
    a.href="https://github.com/KrAzad0/QM-CH1-SOLUTION/blob/main/chapter3/tex/"+file;
    a.target="_blank";
    a.rel="noopener noreferrer";
    a.setAttribute("aria-label","View LaTeX solution to Problem 3."+number);
    card.append(digit,content,a);
    list.appendChild(card);
  });

  document.querySelectorAll(".quick-nav a").forEach(link=>{
    link.addEventListener("click",()=>{
      const input=document.getElementById("problem-search");
      if(input){input.value="";input.dispatchEvent(new Event("input",{bubbles:true}));}
      const all=document.querySelector('[data-filter="all"]');
      if(all)all.click();
    });
  });
})();