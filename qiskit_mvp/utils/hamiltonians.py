"""
Hamiltonian generation utilities for quantum chemistry

This module provides functions to generate Hamiltonians for various
molecular systems and model Hamiltonians.
"""

from typing import Tuple, Optional
import numpy as np
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper, ParityMapper
from qiskit_nature.second_q.problems import ElectronicStructureProblem
from qiskit.quantum_info import SparsePauliOp


def create_h2_hamiltonian(
    distance: float = 0.735,
    basis: str = "sto-3g",
    mapper: str = "jordan_wigner"
) -> Tuple[SparsePauliOp, ElectronicStructureProblem]:
    """
    Create Hamiltonian for H2 molecule.
    
    Args:
        distance: Bond length in Angstroms (default: 0.735)
        basis: Basis set (default: "sto-3g")
        mapper: Fermion-to-qubit mapping ("jordan_wigner" or "parity")
        
    Returns:
        Tuple of (qubit_operator, problem) where:
        - qubit_operator: Hamiltonian as Pauli operator
        - problem: ElectronicStructureProblem object
        
    Example:
        >>> hamiltonian, problem = create_h2_hamiltonian(distance=0.735)
        >>> print(f"Number of qubits: {hamiltonian.num_qubits}")
    """
    # Define H2 molecule geometry
    atom_string = f"H 0 0 0; H 0 0 {distance}"
    
    # Create driver
    driver = PySCFDriver(
        atom=atom_string,
        basis=basis,
        charge=0,
        spin=0
    )
    
    # Run driver to get problem
    problem = driver.run()
    
    # Choose mapper
    if mapper == "jordan_wigner":
        fermion_mapper = JordanWignerMapper()
    elif mapper == "parity":
        fermion_mapper = ParityMapper()
    else:
        raise ValueError(f"Unknown mapper: {mapper}")
    
    # Map to qubits
    hamiltonian = fermion_mapper.map(problem.hamiltonian.second_q_op())
    
    return hamiltonian, problem


def create_lih_hamiltonian(
    distance: float = 1.6,
    basis: str = "sto-3g",
    mapper: str = "jordan_wigner"
) -> Tuple[SparsePauliOp, ElectronicStructureProblem]:
    """
    Create Hamiltonian for LiH molecule.
    
    Args:
        distance: Bond length in Angstroms (default: 1.6)
        basis: Basis set (default: "sto-3g")
        mapper: Fermion-to-qubit mapping
        
    Returns:
        Tuple of (qubit_operator, problem)
    """
    atom_string = f"Li 0 0 0; H 0 0 {distance}"
    
    driver = PySCFDriver(
        atom=atom_string,
        basis=basis,
        charge=0,
        spin=0
    )
    
    problem = driver.run()
    
    if mapper == "jordan_wigner":
        fermion_mapper = JordanWignerMapper()
    elif mapper == "parity":
        fermion_mapper = ParityMapper()
    else:
        raise ValueError(f"Unknown mapper: {mapper}")
    
    hamiltonian = fermion_mapper.map(problem.hamiltonian.second_q_op())
    
    return hamiltonian, problem


def create_hubbard_hamiltonian(
    n_sites: int = 2,
    tunneling: float = 1.0,
    interaction: float = 2.0,
    periodic: bool = False
) -> SparsePauliOp:
    """
    Create Hubbard model Hamiltonian.
    
    The Hubbard Hamiltonian is:
    H = -t Σ_<i,j>,σ (c†_iσ c_jσ + h.c.) + U Σ_i n_i↑ n_i↓
    
    Args:
        n_sites: Number of sites in the chain
        tunneling: Hopping parameter t (default: 1.0)
        interaction: On-site interaction U (default: 2.0)
        periodic: Use periodic boundary conditions (default: False)
        
    Returns:
        SparsePauliOp representing the Hubbard Hamiltonian
        
    Example:
        >>> # 2-site Hubbard model
        >>> H = create_hubbard_hamiltonian(n_sites=2, tunneling=1.0, interaction=2.0)
    """
    n_qubits = 2 * n_sites  # Factor of 2 for spin up and down
    
    # Build Hamiltonian as list of Pauli terms
    pauli_list = []
    coeffs = []
    
    # Hopping terms: -t Σ_<i,j>,σ (c†_iσ c_jσ + h.c.)
    # Using Jordan-Wigner transformation
    for i in range(n_sites - 1):
        for spin in [0, 1]:  # spin up, spin down
            idx1 = 2 * i + spin
            idx2 = 2 * (i + 1) + spin
            
            # Hopping: c†_i c_j term
            # JW: c†_i c_j = (X_i - iY_i)/2 * Z_i+1...Z_j-1 * (X_j + iY_j)/2
            # Simplified for nearest neighbors
            pauli_str1 = ['I'] * n_qubits
            pauli_str1[idx1] = 'X'
            pauli_str1[idx2] = 'X'
            pauli_list.append(''.join(pauli_str1))
            coeffs.append(-tunneling / 2)
            
            pauli_str2 = ['I'] * n_qubits
            pauli_str2[idx1] = 'Y'
            pauli_str2[idx2] = 'Y'
            pauli_list.append(''.join(pauli_str2))
            coeffs.append(-tunneling / 2)
    
    # Periodic boundary condition
    if periodic and n_sites > 2:
        for spin in [0, 1]:
            idx1 = 2 * (n_sites - 1) + spin
            idx2 = spin
            
            pauli_str1 = ['I'] * n_qubits
            pauli_str1[idx1] = 'X'
            pauli_str1[idx2] = 'X'
            pauli_list.append(''.join(pauli_str1))
            coeffs.append(-tunneling / 2)
            
            pauli_str2 = ['I'] * n_qubits
            pauli_str2[idx1] = 'Y'
            pauli_str2[idx2] = 'Y'
            pauli_list.append(''.join(pauli_str2))
            coeffs.append(-tunneling / 2)
    
    # Interaction terms: U Σ_i n_i↑ n_i↓
    # JW: n = (I - Z)/2
    for i in range(n_sites):
        idx_up = 2 * i
        idx_down = 2 * i + 1
        
        # n_i↑ n_i↓ = (I - Z_i↑)/2 * (I - Z_i↓)/2
        # = 1/4 (I - Z_i↑ - Z_i↓ + Z_i↑ Z_i↓)
        
        # Constant term
        pauli_list.append('I' * n_qubits)
        coeffs.append(interaction / 4)
        
        # -Z_i↑ term
        pauli_str = ['I'] * n_qubits
        pauli_str[idx_up] = 'Z'
        pauli_list.append(''.join(pauli_str))
        coeffs.append(-interaction / 4)
        
        # -Z_i↓ term
        pauli_str = ['I'] * n_qubits
        pauli_str[idx_down] = 'Z'
        pauli_list.append(''.join(pauli_str))
        coeffs.append(-interaction / 4)
        
        # Z_i↑ Z_i↓ term
        pauli_str = ['I'] * n_qubits
        pauli_str[idx_up] = 'Z'
        pauli_str[idx_down] = 'Z'
        pauli_list.append(''.join(pauli_str))
        coeffs.append(interaction / 4)
    
    # Create SparsePauliOp
    hamiltonian = SparsePauliOp.from_list(list(zip(pauli_list, coeffs)))
    
    # Simplify by combining like terms
    hamiltonian = hamiltonian.simplify()
    
    return hamiltonian


def get_reference_energy(
    problem: ElectronicStructureProblem,
    method: str = "fci"
) -> float:
    """
    Get reference energy from classical calculation.
    
    This function will use PySCF to compute reference energies for comparison.
    
    Args:
        problem: ElectronicStructureProblem object from Qiskit Nature
        method: Method to use for calculation
            - "hf": Hartree-Fock (mean-field)
            - "fci": Full Configuration Interaction (exact for small systems)
            - "ccsd": Coupled Cluster Singles and Doubles
            - "ccsd(t)": CCSD with perturbative triples
        
    Returns:
        Reference energy in Hartree
        
    Example:
        >>> from qiskit_nature.second_q.drivers import PySCFDriver
        >>> driver = PySCFDriver(atom="H 0 0 0; H 0 0 0.735", basis="sto-3g")
        >>> problem = driver.run()
        >>> fci_energy = get_reference_energy(problem, method="fci")
        >>> print(f"FCI energy: {fci_energy:.6f} Ha")
    
    TODO: Implement using PySCF's built-in methods:
        - HF: problem.get_hartree_fock_energy() or use pyscf.scf.RHF
        - FCI: Use pyscf.fci.FCI
        - CCSD: Use pyscf.cc.CCSD
    """
    # This would use PySCF to get reference energies
    # Placeholder for now
    raise NotImplementedError("Reference energy calculation not yet implemented")


if __name__ == "__main__":
    # Test Hamiltonian generation
    print("Testing H2 Hamiltonian generation...")
    h2_ham, h2_prob = create_h2_hamiltonian()
    print(f"H2 Hamiltonian: {h2_ham.num_qubits} qubits")
    print(f"Number of terms: {len(h2_ham)}")
    
    print("\nTesting Hubbard model...")
    hubbard_ham = create_hubbard_hamiltonian(n_sites=2)
    print(f"Hubbard Hamiltonian: {hubbard_ham.num_qubits} qubits")
    print(f"Number of terms: {len(hubbard_ham)}")
