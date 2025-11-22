# Quick Start Guide: GW and QMC Research

## Overview

This repository contains research on GW method and Quantum Monte Carlo for quantum computing, along with a Qiskit-based MVP implementation.

## What's Included

### 📚 Research Documentation

1. **GW_QMC_Research.md** - Comprehensive research document
   - Overview of GW method and Quantum Monte Carlo
   - Key algorithms and pseudocode
   - Implementation plan for Qiskit MVP
   - Target systems and benchmarks

2. **Paper_References.md** - Paper bibliography
   - Specific paper recommendations with arXiv IDs
   - Search strategies for finding papers
   - Classical reference papers
   - Online resources

3. **RESEARCH_SUMMARY.md** - Executive summary
   - Quick overview of findings
   - Implementation status
   - Next steps

### 💻 MVP Code Structure

Located in `qiskit_mvp/` directory:

```
qiskit_mvp/
├── gw_method/          # GW approximation implementation
├── qmc_method/         # Quantum Monte Carlo implementation  
├── utils/              # Utilities (Hamiltonians, visualization)
├── examples/           # Usage examples
└── requirements.txt    # Python dependencies
```

## Getting Started

### 1. Review the Research

Start by reading the research documents in order:

```bash
# Quick overview
cat RESEARCH_SUMMARY.md

# Detailed research
cat GW_QMC_Research.md

# Paper references
cat Paper_References.md
```

### 2. Understanding the Algorithms

**GW Method:**
- Calculates electronic structure using many-body perturbation theory
- Key components: Green's function (G), Screened interaction (W), Self-energy (Σ)
- Quantum implementation uses QPE and time evolution

**Quantum Monte Carlo:**
- Variational QMC uses parameterized quantum circuits
- Quantum amplitude estimation provides quadratic speedup
- Applications: ground state energy, electronic structure

### 3. Exploring the Code

```bash
cd qiskit_mvp

# View the main README
cat README.md

# Check example scripts
cat examples/example_gw_h2.py
cat examples/example_vqmc_h2.py

# View implemented utilities
cat utils/hamiltonians.py
```

### 4. Next Steps for Implementation

The code structure is ready. To implement:

1. **Install dependencies:**
   ```bash
   cd qiskit_mvp
   pip install -r requirements.txt
   ```

2. **Test Hamiltonian generation:**
   ```python
   from utils.hamiltonians import create_h2_hamiltonian, create_hubbard_hamiltonian
   
   # H2 molecule
   h2_ham, problem = create_h2_hamiltonian(distance=0.735)
   print(f"H2: {h2_ham.num_qubits} qubits, {len(h2_ham)} terms")
   
   # Hubbard model
   hubbard_ham = create_hubbard_hamiltonian(n_sites=2)
   print(f"Hubbard: {hubbard_ham.num_qubits} qubits")
   ```

3. **Implement core algorithms:**
   - Green's function calculation (time evolution)
   - VQMC optimization loop
   - Energy sampling and estimation

## Key Features

### ✅ Completed

- Comprehensive research documentation
- Paper bibliography with search strategies
- Complete MVP code structure
- Hamiltonian generation utilities (H₂, LiH, Hubbard)
- State preparation functions
- Visualization utilities
- Example scripts

### 🚧 To Be Implemented

- Green's function via time evolution
- Screened interaction calculation
- Self-energy and GW self-consistency
- VQMC optimization
- Quantum amplitude estimation
- Benchmarking suite

## Target Systems

### Phase 1: Simple Systems
- **H₂ molecule:** 2 electrons, 4 qubits, equilibrium geometry
- **2-site Hubbard model:** 4 qubits, exact solution available

### Phase 2: Larger Systems  
- **LiH molecule:** 4 electrons, 8-12 qubits
- **BeH₂ molecule:** 6 electrons, 12-16 qubits

## Expected Results

**GW Method:**
- Quasi-particle energies within 10% of classical GW
- HOMO-LUMO gap calculation
- Comparison with Hartree-Fock and FCI

**Quantum Monte Carlo:**
- Ground state energy within 1% of exact for H₂
- Statistical error analysis
- Convergence within 100 iterations

## Papers to Find

### High Priority

1. **GW on quantum computers** - Green's function via QPE
2. **Quantum Monte Carlo with quantum computing** - VQMC implementations  
3. **Quantum chemistry reviews** - State of the art

### Search Strategy

Use arXiv searches:
```
"GW approximation" AND ("quantum computer" OR "quantum algorithm")
"quantum Monte Carlo" AND ("quantum computer" OR "qubit")
"quantum chemistry" AND ("VQE" OR "QPE")
```

Categories: quant-ph, cond-mat.str-el, physics.chem-ph

## Resources

### Documentation
- **Main Research:** GW_QMC_Research.md
- **Papers:** Paper_References.md  
- **Summary:** RESEARCH_SUMMARY.md
- **MVP Guide:** qiskit_mvp/README.md

### External Links
- Qiskit Nature: https://qiskit.org/ecosystem/nature/
- PySCF (classical reference): https://pyscf.org/
- ArXiv quantum physics: https://arxiv.org/list/quant-ph/recent

## Contributing to Implementation

To contribute to the implementation:

1. Pick a module from the TODO list
2. Review the algorithm description in GW_QMC_Research.md
3. Implement following the existing code structure
4. Add tests in `tests/` directory
5. Update documentation

## Project Structure

```
paper/
├── GW_QMC_Research.md           # Main research document
├── Paper_References.md          # Paper bibliography
├── RESEARCH_SUMMARY.md          # Executive summary
├── QUICK_START.md              # This file
├── qiskit_mvp/                 # MVP implementation
│   ├── gw_method/              # GW modules
│   ├── qmc_method/             # QMC modules
│   ├── utils/                  # Utilities
│   ├── examples/               # Examples
│   └── requirements.txt        # Dependencies
├── pdf/                        # Paper PDFs
├── 60qa/                       # Paper analysis
└── latex/                      # LaTeX files
```

## FAQ

**Q: Where should I start?**  
A: Read RESEARCH_SUMMARY.md first, then dive into GW_QMC_Research.md for details.

**Q: Is the code ready to run?**  
A: The structure is complete, but core algorithms need implementation. Hamiltonian utilities are functional.

**Q: What papers should I download?**  
A: See Paper_References.md for specific search terms and arXiv categories.

**Q: Can I run this on real quantum hardware?**  
A: Initially designed for simulators. Real hardware requires error mitigation and circuit optimization.

**Q: How accurate will the results be?**  
A: Target: GW within 10%, VQMC within 1% of exact for small systems (H₂).

## Support

- Repository: https://github.com/Amonsuzuki/paper
- Issues: Use GitHub issues for bugs or questions
- Documentation: All markdown files in repository

---

**Last Updated:** 2025-11-22  
**Status:** Research complete, implementation ready to begin  
**Version:** 1.0
