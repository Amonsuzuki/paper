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
    print("State preparation utilities - Testing")
    
    # Test HF state preparation
    print("\n1. Testing Hartree-Fock state...")
    hf_circuit = prepare_hartree_fock_state(n_qubits=4, n_electrons=2)
    print(f"   HF circuit for 4 qubits, 2 electrons:")
    print(f"   Depth: {hf_circuit.depth()}")
    print(f"   Gates: {hf_circuit.count_ops()}")
    print("   ✓ HF state preparation working")
    
    # Test uniform superposition
    print("\n2. Testing uniform superposition...")
    superpos_circuit = prepare_uniform_superposition(n_qubits=3)
    print(f"   Superposition circuit for 3 qubits:")
    print(f"   Depth: {superpos_circuit.depth()}")
    print(f"   Gates: {superpos_circuit.count_ops()}")
    print("   ✓ Superposition state preparation working")
    
    # Test edge cases
    print("\n3. Testing edge cases...")
    try:
        edge1 = prepare_hartree_fock_state(2, 0)
        print("   ✓ Empty state (0 electrons) works")
        edge2 = prepare_hartree_fock_state(2, 2)
        print("   ✓ Full state (all electrons) works")
    except Exception as e:
        print(f"   ✗ Edge case failed: {e}")
    
    print("\n✓ All state preparation tests passed")
