"""
GW Method Implementation for Qiskit

This package provides quantum computing implementations of the GW approximation
for many-body electronic structure calculations.
"""

__version__ = "0.1.0"

from .gw_calculator import GWCalculator
from .green_function import QuantumGreenFunction
from .screened_interaction import ScreenedInteraction
from .self_energy import SelfEnergy

__all__ = [
    "GWCalculator",
    "QuantumGreenFunction", 
    "ScreenedInteraction",
    "SelfEnergy",
]
