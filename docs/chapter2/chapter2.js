(() => {
'use strict';
const topics = [
 ["Reality and parity of stationary states","FORMALISM","Establish reality of energy, real spatial bases and parity eigenstates.","Real E; parity ±"],
 ["Lower bound on bound-state energies","ENERGY SPECTRUM","Use positivity of kinetic energy to bound E above min V.","E > min V"],
 ["Why E ≤ 0 fails inside a box","BOUNDARY CONDITIONS","Exclude zero and negative energies directly from the ODE.","E_n > 0"],
 ["Expectation values in the infinite well","EXPECTATION VALUES","Evaluate x, x², p, p² and both uncertainties.","σx σp > ℏ/2"],
 ["Two-state superposition dynamics","TIME EVOLUTION","Track density, position, momentum and energy measurements.","Oscillation frequency 3Ω"],
 ["Relative phase and quantum motion","COHERENCE","Show that a phase difference shifts observable oscillations.","cos(3Ωt − φ)"],
 ["Triangular initial state","FOURIER SERIES","Normalize the cusp and expand into stationary eigenstates.","Only odd Fourier modes"],
 ["Half-box initial wavefunction","MEASUREMENT","Project a localized initial state onto the ground level.","P(E₁) = 4/π²"],
 ["Direct Hamiltonian expectation","ENERGY EXPECTATION","Verify the spectral-sum energy by direct integration.","⟨H⟩ = 5ℏ²/(ma²)"],
 ["Second excited harmonic oscillator","LADDER ALGEBRA","Construct ψ₂ and verify orthogonality from Gaussian moments.","ψ₂ ∝ (2q² − 1)e⁻q²ᐟ²"],
 ["Oscillator moments for n=0,1","QUANTUM OSCILLATOR","Evaluate Gaussian position and momentum integrals.","σxσp = ℏ/2, 3ℏ/2"],
 ["General oscillator uncertainties","CREATION / ANNIHILATION","Use ladder operators for the nth state.","σxσp = (n+½)ℏ"],
 ["Dynamics of a 3:4 superposition","EHRENFEST THEOREM","Compute coherent motion and test the force law.","⟨x⟩ ∝ cos(ωt)"],
 ["Ground-state tunneling tail","CLASSICAL LIMIT","Integrate the Gaussian beyond classical turning points.","Pout ≈ 0.157"],
 ["Fifth and sixth Hermite polynomials","SPECIAL FUNCTIONS","Generate H₅ and H₆ by recursion.","H₅, H₆ explicit"],
 ["Hermite polynomial identities","SPECIAL FUNCTIONS","Prove formulas using Rodrigues and generating functions.","H′ₙ = 2n Hₙ₋₁"],
 ["Traveling and standing wave bases","FREE PARTICLE","Transform between exponentials and sines/cosines.","C = A + B"],
 ["Probability current of free waves","CURRENT DENSITY","Separate left- and right-moving flux.","J ∝ |A|² − |B|²"],
 ["Complex Fourier series to transform","FOURIER ANALYSIS","Take the large-box limit of exponential series.","Fourier transform pair"],
 ["Exponential packet in free space","WAVE PACKETS","Normalize, transform and propagate an exponential cusp.","φ(k) ∝ 1/(a²+k²)"],
 ["Spreading Gaussian wave packet","UNCERTAINTY","Derive exact evolution, variances and minimum uncertainty.","σx(t) increases"],
 ["Three delta-function integrals","DISTRIBUTIONS","Apply the delta sifting property and support tests.","−25, 1, 0"],
 ["Delta scaling and Heaviside step","DISTRIBUTIONS","Derive δ(cx) and the derivative of a step.","θ′ = δ"],
 ["Delta-bound-state uncertainty","SINGULAR POTENTIAL","Treat the cusp with a distributional second derivative.","σxσp = ℏ/√2"],
 ["Bound/scattering orthogonality","SPECTRAL THEORY","Use the Wronskian and matching conditions.","Overlap = 0"],
 ["Fourier representation of δ(x)","FOURIER ANALYSIS","Interpret an oscillatory Fourier integral as a distribution.","δ(x) = ∫eⁱᵏˣdk/(2π)"],
 ["Two attractive delta centers","BOUND STATES","Solve even and odd transcendental equations.","κ± = κ₀(1 ± e⁻²κa)"],
 ["Transmission through two deltas","SCATTERING","Compose the matching conditions using transfer matrices.","T = 1/|M₂₂|²"],
 ["Odd bound states of a finite well","FINITE SQUARE WELL","Derive odd-parity energies and count allowed levels.","−z cot z = √(z₀² − z²)"],
 ["Normalize an even finite-well state","NORMALIZATION","Match decaying exterior and cosine interior amplitudes.","D and F from norm"],
 ["The delta potential as a limit","LIMITING CASES","Shrink a finite well while fixing its integrated strength.","E = −mα²/(2ℏ²)"],
 ["Finite square-well transmission","SCATTERING","Match waves across both interfaces and find T.","Resonances T = 1"],
 ["Transmission through a barrier","QUANTUM TUNNELING","Treat E below, equal and above the barrier height.","T ∝ sinh⁻²(κL) at low E"],
 ["Reflection at an upward step","POTENTIAL STEPS","Derive flux-weighted R, T and continuity checks.","R + T = 1"],
 ["Quantum reflection at a cliff","POTENTIAL DROPS","Compare step reflection to a neutron entering a nucleus.","R = 1/9"],
 ["Centered infinite square well","PARITY","Solve on (−a,a) and classify even/odd eigenstates.","Eₙ = n²π²ℏ²/(8ma²)"],
 ["Cubic-sine initial wavefunction","SUPERPOSITION","Reduce sin³ to two eigenstates and find energy.","⟨x⟩ = a/2"],
 ["Quantum revival in a box","REVIVAL TIMES","Show exact recurrence and compare classical motion.","Tq = 4ma²/(πℏ)"],
 ["Delta derivatives of a cusp state","DISTRIBUTIONAL DERIVATIVES","Use θ′ = δ for a piecewise linear initial state.","⟨H⟩ = 6ℏ²/(ma²)"],
 ["Polynomial-Gaussian oscillator state","OSCILLATOR EXPANSIONS","Find coefficients, measurement outcomes and revival time.","T = π/ω"],
 ["Half harmonic oscillator","BOUNDARY CONDITIONS","Retain only odd full-line oscillator states.","Eⱼ = (2j+3/2)ℏω"],
 ["Traveling Gaussian packet","WAVE-PACKET DYNAMICS","Distinguish envelope and carrier phase velocities.","vg = 2vp"],
 ["Well with a central delta barrier","SINGULAR BARRIER","Compare even-state shifts with unaffected odd states.","−ka cot ka = mαa/ℏ²"],
 ["Nondegeneracy of 1D bound states","WRONSKIAN","Prove that equal-energy bound solutions are proportional.","No 1D bound degeneracy"],
 ["Interlacing of eigenstate nodes","STURM THEORY","Use the Wronskian derivative to compare node counts.","Higher energy → more nodes"],
 ["Free particle on a ring","PERIODIC BOUNDARIES","Derive angular modes and ±n degeneracy.","kₙ = 2πn/L"],
 ["Qualitative double square well","MOLECULAR BONDING","Discuss symmetric/antisymmetric splitting and separation.","Splitting → 0 as gap grows"],
 ["Wall-adjacent finite well","NUMERICAL ROOTS","Find three bound levels and the outer probability.","Poutside ≈ 0.542"],
 ["Exact coherent oscillator packet","COHERENT STATES","Verify a nonspreading oscillating Gaussian.","⟨x⟩ = x₀ cosωt"],
 ["Moving delta-function well","GALILEAN BOOST","Transform an attractive bound state into a moving well.","⟨H⟩ = E₀+mv²/2"],
 ["Gaussian packet in free fall","GRAVITATIONAL POTENTIAL","Apply a coordinate shift and a time-dependent phase.","⟨x⟩ = −gt²/2"],
 ["Reflectionless sech² potential","EXACT SOLVABILITY","Check bound and scattering states of a smooth well.","R = 0, T = 1"],
 ["Scattering matrix of symmetric wells","S-MATRIX","Construct two-channel scattering and check unitarity.","S†S = I"],
 ["Transfer matrices and two deltas","TRANSFER MATRIX","Compose potentials and recover T from M₂₂.","Mtotal = M₂M₁"],
 ["Oscillator ground energy by shooting","NUMERICAL ODE","Vary K until a decaying solution is selected.","K₀ = 1"],
 ["Excited oscillator energies by shooting","NUMERICAL ODE","Use parity conditions and count nodes.","K = 3, 5, 7"],
 ["Numerical infinite-square-well spectrum","SHOOTING METHOD","Solve the Dirichlet problem with numerical roots.","εₙ = n²π²"],
 ["Simple metallic cohesion model","SOLID STATE","Estimate energy lowering due to delocalization.","≈1.57 eV / atom"],
 ["Quantum bouncing ball","AIRY FUNCTIONS","Airy zeros, normalization, variances and classical comparison.","λ₁ = 2.338107"],
 ["Attractive inverse-square potential","SCALE INVARIANCE","Modified Bessel states and singular-boundary subtleties.","ψ ∝ √x Kᵢg(κx)"],
 ["Finite-difference Hamiltonian","MATRIX SPECTRA","Construct tridiagonal box matrices and compare convergence.","Eigenvalues converge ∝ Δx²"],
 ["Sinusoidal-bottom square well","NUMERICAL DIAGONALIZATION","Obtain and plot three low-lying energy eigenvectors.","ε₁ ≈ 304.660"],
 ["Boltzmann oscillator heat capacity","STATISTICAL MECHANICS","Derive Einstein's partition function and heat capacity.","C → 3kB at high T"],
 ["Legendre polynomial recurrence","SPECIAL FUNCTIONS","Use power series and regularity to find P₀ through P₃.","P₂ = (3x²−1)/2"]
];

const groups = [
 [1, 9, "01-09.tex"],
 [10, 16, "10-16.tex"],
 [17, 21, "17-21.tex"],
 [22, 28, "22-28.tex"],
 [29, 35, "29-35.tex"],
 [36, 45, "36-45.tex"],
 [46, 54, "46-54.tex"],
 [55, 64, "55-64.tex"]
];

function findGroup(number) {
 return groups.find(g => number >= g[0] && number <= g[1]);
}
function tag(tagName, className, content) {
 const el = document.createElement(tagName);
 if (className) el.className = className;
 if (content != null) el.textContent = content;
 return el;
}
const root = document.getElementById("problem-list");
topics.forEach((item, index) => {
 const n = index + 1;
 const article = tag("article", "problem-card");
 article.id = "problem-2-" + n;
 article.dataset.group = n <= 35 ? "section" : "further";
 article.dataset.terms = ("2." + n + " " + item.join(" ")).toLowerCase();
 const number = tag("div", "problem-number");
 number.textContent = String(n).padStart(2, "0") + " / 64";
 const body = tag("div", "problem-content");
 body.appendChild(tag("span", "problem-category", item[1]));
 body.appendChild(tag("h3", "", item[0]));
 body.appendChild(tag("p", "", item[2]));
 body.appendChild(tag("div", "result-line", item[3]));
 const group = findGroup(n);
 const url = "https://github.com/KrAzad0/QM-CH1-SOLUTION/blob/main/chapter2/tex/" + group[2];
 const link = tag("a", "problem-link", "LaTeX solution ↗");
 link.href = url;
 link.target = "_blank";
 link.rel = "noopener noreferrer";
 link.setAttribute("aria-label", "Open detailed solution to Problem 2." + n);
 article.append(number, body, link);
 root.appendChild(article);
});

document.querySelectorAll("[data-group-link]").forEach(link => {
 link.addEventListener("click", evt => {
   evt.preventDefault();
   const group = groups[Number(link.dataset.groupLink)];
   const destination = document.getElementById("problem-2-" + group[0]);
   const search = document.getElementById("problem-search");
   if (search) {
     search.value = "";
     search.dispatchEvent(new Event("input", { bubbles: true }));
   }
   const all = document.querySelector('[data-filter="all"]');
   if (all) all.click();
   if (destination) destination.scrollIntoView({ behavior: "smooth", block: "start" });
 });
});
})();
