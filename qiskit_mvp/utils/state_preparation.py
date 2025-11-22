"""
State Preparation Utilities

This module provides utilities for preparing initial quantum states.
"""

from typing import Optional, List
import numpy as np
from qiskit import QuantumCircuit


def prepare_hartree_fock_state(
    n_qubits: int,
    n_electrons: int
) -> QuantumCircuit:
    """
    Prepare Hartree-Fock state (occupation number basis).
    
    For n_electrons=2, n_qubits=4, prepares |1100⟩ state.
    
    Args:
        n_qubits: Total number of qubits
        n_electrons: Number of electrons (qubits to flip to |1⟩)
        
    Returns:
        Quantum circuit preparing HF state
    """
    qc = QuantumCircuit(n_qubits)
    
    # Flip first n_electrons qubits to |1⟩
    for i in range(n_electrons):
        qc.x(i)
    
    return qc


def prepare_uniform_superposition(n_qubits: int) -> QuantumCircuit:
    """
    Prepare uniform superposition over all basis states.
    
    Args:
        n_qubits: Number of qubits
        
    Returns:
        Circuit preparing |+⟩⊗n state
    """
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))
    return qc


# Placeholder for testing
if __name__ == "__main__":
    print("State preparation utilities - Ready")
    
    # Test HF state
    hf_circuit = prepare_hartree_fock_state(4, 2)
    print(f"HF circuit depth: {hf_circuit.depth()}")
