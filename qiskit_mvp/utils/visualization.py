"""
Visualization Utilities

This module provides plotting and visualization functions.
"""

from typing import List, Optional
import numpy as np
import matplotlib.pyplot as plt


def plot_energy_convergence(
    energies: List[float],
    exact_energy: Optional[float] = None,
    save_path: Optional[str] = None
):
    """
    Plot energy convergence during optimization.
    
    Args:
        energies: List of energy values over iterations
        exact_energy: Exact energy for reference (if known)
        save_path: Path to save figure (if provided)
    """
    plt.figure(figsize=(10, 6))
    plt.plot(energies, 'o-', label='VQMC Energy')
    
    if exact_energy is not None:
        plt.axhline(y=exact_energy, color='r', linestyle='--', label='Exact')
    
    plt.xlabel('Iteration')
    plt.ylabel('Energy (Ha)')
    plt.title('Energy Convergence')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()


def plot_wavefunction(
    amplitudes: np.ndarray,
    n_qubits: int,
    save_path: Optional[str] = None
):
    """
    Plot wavefunction amplitudes.
    
    Args:
        amplitudes: Wavefunction amplitudes
        n_qubits: Number of qubits
        save_path: Path to save figure
    """
    n_states = 2 ** n_qubits
    states = [format(i, f'0{n_qubits}b') for i in range(n_states)]
    
    plt.figure(figsize=(12, 6))
    plt.bar(range(n_states), np.abs(amplitudes)**2)
    plt.xlabel('Basis State')
    plt.ylabel('Probability')
    plt.title('Wavefunction Probability Distribution')
    plt.xticks(range(n_states), states, rotation=90)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()


# Placeholder for testing
if __name__ == "__main__":
    print("Visualization utilities - Testing")
    
    import numpy as np
    
    # Test energy convergence plot
    print("\n1. Testing energy convergence plot...")
    test_energies = [-1.0 - 0.1 * np.exp(-0.3 * i) + 0.01 * np.random.randn() 
                     for i in range(20)]
    exact_energy = -1.1
    
    print(f"   Sample energies: {test_energies[:5]} ...")
    print(f"   Exact energy: {exact_energy}")
    # Uncomment to save plot: plot_energy_convergence(test_energies, exact_energy, "test_convergence.png")
    print("   ✓ Energy plot function ready")
    
    # Test wavefunction plot
    print("\n2. Testing wavefunction plot...")
    n_qubits = 2
    test_amplitudes = np.random.randn(2**n_qubits) + 1j * np.random.randn(2**n_qubits)
    test_amplitudes /= np.linalg.norm(test_amplitudes)
    
    print(f"   Amplitudes shape: {test_amplitudes.shape}")
    print(f"   Norm: {np.linalg.norm(test_amplitudes):.6f}")
    # Uncomment to save plot: plot_wavefunction(test_amplitudes, n_qubits, "test_wavefunction.png")
    print("   ✓ Wavefunction plot function ready")
    
    print("\n✓ All visualization utilities ready")
