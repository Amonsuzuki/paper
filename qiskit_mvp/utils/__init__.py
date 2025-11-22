"""
Utility functions for quantum chemistry calculations

This module provides helper functions for Hamiltonian generation,
state preparation, and visualization.
"""

__version__ = "0.1.0"

from .hamiltonians import (
    create_h2_hamiltonian,
    create_lih_hamiltonian,
    create_hubbard_hamiltonian,
)
from .state_preparation import (
    prepare_hartree_fock_state,
    prepare_uniform_superposition,
)
from .visualization import plot_energy_convergence, plot_wavefunction

__all__ = [
    "create_h2_hamiltonian",
    "create_lih_hamiltonian",
    "create_hubbard_hamiltonian",
    "prepare_hartree_fock_state",
    "prepare_uniform_superposition",
    "plot_energy_convergence",
    "plot_wavefunction",
]
