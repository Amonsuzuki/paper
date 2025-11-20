# LaTeX Conversion - Machine Learning for DFT Accuracy

This directory contains the LaTeX conversion of the paper "Machine learning for accuracy in density functional approximations" by Johannes Voss.

## Files

- `ml-dft-accuracy.tex` - Main LaTeX source file
- `ml-dft-accuracy.pdf` - Compiled PDF output (9 pages)

## Original Source

Converted from: `/pdf/ml-dft/2311.00196v2.pdf`

## Paper Information

**Title:** Machine learning for accuracy in density functional approximations

**Author:** Johannes Voss (SUNCAT Center for Interface Science and Catalysis, SLAC National Accelerator Laboratory)

**Date:** October 2, 2025

**Abstract:** Machine learning techniques have found their way into computational chemistry as indispensable tools to accelerate atomistic simulations and materials design. In addition, machine learning approaches hold the potential to boost the predictive power of computationally efficient electronic structure methods, such as density functional theory, to chemical accuracy and to correct for fundamental errors in density functional approaches. This review covers recent progress in applying machine learning to improve the accuracy of density functional and related approximations.

## Compilation

To compile the LaTeX document:

```bash
pdflatex ml-dft-accuracy.tex
```

You may need to run it twice to resolve all references.

## Structure

The document includes the following sections:

1. Introduction
2. Shortcomings of Density Functional Approximations
3. Ground Truth for DFA ML Models
   - Thermochemistry, thermochemical kinetics, and molecular interactions
   - Atomic structures
   - Transition-metal surface chemistry
4. ML XC Functionals
   - Semi-empirical DFAs with explicit functional forms
   - Neural network DFAs
5. Δ-ML Corrections to DFT
6. Atomic Structure-Dependent XC Corrections
7. ML KS Hamiltonian Substitutions
8. Challenges and Opportunities
9. Summary
10. Methods
11. Bibliography (70+ references)

## Notes

This LaTeX version has been manually created from the PDF source to maintain proper document structure, mathematical equations, and citations. The conversion includes:

- Properly formatted mathematical equations
- Complete bibliography with proper citation formatting
- Section and subsection hierarchy
- All key content from the original paper

## License

This is a peer-reviewed version of the article published in J. Comput. Chem. 45, 1829–1845 (2024). See the original paper for full copyright and usage terms.
