# Qiskit MVP: GW Method and Quantum Monte Carlo

This directory contains the MVP (Minimum Viable Product) implementation of GW method and Quantum Monte Carlo algorithms using Qiskit.

## Project Structure

```
qiskit_mvp/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
├── gw_method/               # GW approximation implementation
│   ├── __init__.py
│   ├── green_function.py    # Green's function calculations
│   ├── screened_interaction.py  # W calculation
│   ├── self_energy.py       # Self-energy Σ calculation
│   └── gw_calculator.py     # Main GW interface
├── qmc_method/              # Quantum Monte Carlo implementation
│   ├── __init__.py
│   ├── variational_wavefunction.py  # Ansatz definitions
│   ├── quantum_sampler.py   # Sampling routines
│   ├── amplitude_estimation.py  # QAE for integrals
│   └── vqmc_engine.py       # Main VQMC interface
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── hamiltonians.py      # Hamiltonian generation
│   ├── state_preparation.py # State prep utilities
│   └── visualization.py     # Plotting and analysis
├── examples/                # Usage examples
│   ├── example_gw_h2.py
│   ├── example_vqmc_h2.py
│   ├── example_hubbard.py
│   └── notebooks/
│       ├── 01_introduction.ipynb
│       ├── 02_gw_tutorial.ipynb
│       └── 03_vqmc_tutorial.ipynb
└── tests/                   # Unit tests
    ├── test_green_function.py
    ├── test_vqmc.py
    └── test_hamiltonians.py
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone or navigate to this directory:
```bash
cd qiskit_mvp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Install in development mode:
```bash
pip install -e .
```

## Quick Start

### Example 1: GW Approximation for H₂

```python
from qiskit_nature.second_q.drivers import PySCFDriver
from gw_method import GWCalculator

# Define H2 molecule
driver = PySCFDriver(atom="H 0 0 0; H 0 0 0.735", basis="sto-3g")
qmol = driver.run()

# Run GW calculation
gw = GWCalculator(qmol, backend='aer_simulator')
gw.run_self_consistent_gw(max_iter=5)

# Get results
qp_energies = gw.get_qp_energies()
print(f"Quasi-particle gap: {qp_energies[1] - qp_energies[0]:.4f} Ha")
```

### Example 2: Variational QMC for H₂

```python
from qiskit_nature.second_q.drivers import PySCFDriver
from qmc_method import VQMCEngine

# Define H2 molecule
driver = PySCFDriver(atom="H 0 0 0; H 0 0 0.735", basis="sto-3g")
qmol = driver.run()

# Run VQMC
vqmc = VQMCEngine(qmol, ansatz='UCCSD', backend='aer_simulator')
result = vqmc.run_vqmc(n_samples=1000, max_iter=100)

# Get results
print(f"Ground state energy: {result.energy:.6f} Ha")
print(f"Standard deviation: {result.std:.6f} Ha")
```

## Features

### Implemented
- [x] Basic Hamiltonian generation (H₂, LiH)
- [x] Classical reference calculations (PySCF integration)
- [ ] Green's function via time evolution
- [ ] Variational ansatz (UCCSD, hardware-efficient)
- [ ] Energy sampling and estimation
- [ ] Basic visualization utilities

### In Progress
- [ ] GW self-consistency loop
- [ ] Screened interaction calculation
- [ ] Quantum amplitude estimation
- [ ] Advanced error mitigation

### Planned
- [ ] Larger molecules (LiH, BeH₂)
- [ ] Hubbard model implementation
- [ ] Resource estimation tools
- [ ] Benchmarking suite
- [ ] Comprehensive documentation

## Testing

Run all tests:
```bash
pytest tests/
```

Run specific test:
```bash
pytest tests/test_green_function.py -v
```

## Examples and Tutorials

### Python Examples
See the `examples/` directory for standalone Python scripts:
- `example_gw_h2.py`: GW calculation for hydrogen molecule
- `example_vqmc_h2.py`: VQMC calculation for hydrogen molecule
- `example_hubbard.py`: Hubbard model examples

### Jupyter Notebooks
Interactive tutorials are available in `examples/notebooks/`:
- `01_introduction.ipynb`: Overview and setup
- `02_gw_tutorial.ipynb`: Step-by-step GW calculation
- `03_vqmc_tutorial.ipynb`: Step-by-step VQMC calculation

## Development

### Code Style
We follow PEP 8 style guidelines. Format code with:
```bash
black qiskit_mvp/
isort qiskit_mvp/
```

### Contributing
1. Create a feature branch
2. Make changes with tests
3. Ensure all tests pass
4. Submit pull request

## Benchmarks

### H₂ Molecule (bond length = 0.735 Å, STO-3G basis)

| Method | Energy (Ha) | Error vs Exact | Circuit Depth | Time (s) |
|--------|-------------|----------------|---------------|----------|
| Exact (FCI) | -1.137270 | - | - | <0.1 |
| HF | -1.117349 | 0.019921 | - | <0.1 |
| Classical GW | -1.128xxx | ~0.009 | - | ~1 |
| Quantum GW (this work) | TBD | TBD | TBD | TBD |
| Classical VMC | -1.135xxx | ~0.002 | - | ~10 |
| VQMC (this work) | TBD | TBD | TBD | TBD |

*TBD: To be determined after implementation*

## Performance Considerations

### Simulators
- **Aer Simulator**: Best for debugging and development
- **Statevector**: Fast for small systems (<12 qubits)
- **Qasm**: For shot-based simulations

### Real Hardware (Future)
- Circuit optimization needed for depth reduction
- Error mitigation essential
- Expected fidelity considerations

## Limitations

### Current Implementation
- Limited to small molecules (≤4 qubits)
- Simulator only (no hardware noise)
- Simplified GW (no full self-consistency yet)
- Basic ansatz options

### Theoretical
- GW approximation validity (weakly correlated systems)
- Fixed node approximation in DMC
- Statistical error in sampling
- NISQ hardware limitations

## Resources

### Documentation
- [Qiskit Nature Documentation](https://qiskit.org/ecosystem/nature/)
- [PySCF Documentation](https://pyscf.org/)
- [Main Project Documentation](../GW_QMC_Research.md)

### Papers
See [Paper_References.md](../Paper_References.md) for detailed bibliography.

### Support
- GitHub Issues: [Report bugs or request features]
- Questions: [Contact information]

## License

[To be determined - suggest MIT or Apache 2.0]

## Citation

If you use this code in your research, please cite:

```bibtex
@software{qiskit_gw_qmc_mvp,
  title = {Qiskit MVP: GW Method and Quantum Monte Carlo},
  author = {[Your Name]},
  year = {2025},
  url = {https://github.com/Amonsuzuki/paper}
}
```

## Acknowledgments

- Qiskit team for the quantum computing framework
- PySCF developers for classical reference implementations
- Research papers cited in Paper_References.md

## Changelog

### Version 0.1.0 (2025-11-22)
- Initial project structure
- Basic README and documentation
- Planned feature roadmap

---

**Status:** Under Development  
**Last Updated:** 2025-11-22  
**Version:** 0.1.0-alpha
