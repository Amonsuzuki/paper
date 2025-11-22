# Example: Before and After Formula Formatting

This document demonstrates the improvements made to formula visibility in this repository.

## ❌ Before: Hard to Read

```
i=1, the variation of the energy functional E[Φ]in Eq. (S15) with respect to each
orbital ϕiis required:
δE[Φ]
δϕi(r) =δPN
j=1(−1/2)⟨ϕj|∇2|ϕj⟩
δϕi(r) +ZδEeff[ρ[Φ]]
δρ(r′)δρ[Φ](r′)
δϕi(r)dr′
```

**Problems:**
- Symbols are unclear and hard to distinguish
- Structure is difficult to follow
- Copy-pasting from PDF creates formatting issues
- Subscripts and superscripts are not properly formatted
- Greek letters may not display correctly

---

## ✅ After: Clear and Readable

For $i=1$, the variation of the energy functional $E[\Phi]$ in Eq. (S15) with respect to each orbital $\phi_i$ is required:

$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} = \frac{\delta \sum_{j=1}^{N}\left(-\frac{1}{2}\right)\langle\phi_j|\nabla^2|\phi_j\rangle}{\delta \phi_i(r)} + \int \frac{\delta E_{eff}[\rho[\Phi]]}{\delta \rho(r')}\frac{\delta \rho[\Phi](r')}{\delta \phi_i(r)}dr'
$$

**Benefits:**
- ✅ Clear mathematical notation using LaTeX syntax
- ✅ Proper rendering on GitHub and in markdown viewers
- ✅ Easy to read and understand
- ✅ Professional appearance
- ✅ Copy-paste friendly for reuse
- ✅ Version control friendly (readable in diffs)

---

## Comparison Examples

### Example 1: Kinetic Energy Operator

**Before:**
```
T̂ = −(1/2)∇²
```

**After:**
$$
\hat{T} = -\frac{1}{2}\nabla^2
$$

### Example 2: Orthonormality Constraint

**Before:**
```
⟨ϕᵢ|ϕᵢ⟩ = 1
```

**After:**
$$
\langle\phi_i|\phi_i\rangle = 1
$$

### Example 3: Lagrange Multiplier Equation

**Before:**
```
δE[Φ]/δϕᵢ(r) - λᵢδ⟨ϕᵢ|ϕᵢ⟩/δϕᵢ(r) = 0
```

**After:**
$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} - \lambda_i\frac{\delta\langle\phi_i|\phi_i\rangle}{\delta \phi_i(r)} = 0
$$

### Example 4: Complex Multi-line Derivation

**Before:**
```
2T̂ϕᵢ(r) + 2Veff[ρ[Φ]](r)ϕᵢ(r) = λᵢ·2ϕᵢ(r)

Dividing both sides by 2:
T̂ϕᵢ(r) + Veff[ρ[Φ]](r)ϕᵢ(r) = λᵢϕᵢ(r)
```

**After:**

Starting from:
$$
2\hat{T}\phi_i(r) + 2V_{eff}[\rho[\Phi]](r)\phi_i(r) = \lambda_i \cdot 2\phi_i(r)
$$

Dividing both sides by 2:
$$
\hat{T}\phi_i(r) + V_{eff}[\rho[\Phi]](r)\phi_i(r) = \lambda_i\phi_i(r)
$$

---

## How to Write These Formulas

### Basic LaTeX Commands Used

| Display | LaTeX Code |
|---------|-----------|
| $\phi$ | `\phi` |
| $\nabla$ | `\nabla` |
| $\delta$ | `\delta` |
| $\lambda$ | `\lambda` |
| $\hat{T}$ | `\hat{T}` |
| $\frac{a}{b}$ | `\frac{a}{b}` |
| $\sum_{i=1}^{n}$ | `\sum_{i=1}^{n}` |
| $\int_{a}^{b}$ | `\int_{a}^{b}` |
| $\langle x \rangle$ | `\langle x \rangle` |
| $x_i$ | `x_i` |
| $x^2$ | `x^2` |

### Inline vs Display Math

**Inline math** (for text): Use single dollar signs
```markdown
The operator $\hat{T}$ is defined as $\hat{T} = -\frac{1}{2}\nabla^2$.
```
Renders as: The operator $\hat{T}$ is defined as $\hat{T} = -\frac{1}{2}\nabla^2$.

**Display math** (standalone): Use double dollar signs
```markdown
$$
\hat{F}[\rho[\Phi]]\phi_i = \varepsilon_i\phi_i
$$
```
Renders as:
$$
\hat{F}[\rho[\Phi]]\phi_i = \varepsilon_i\phi_i
$$

---

## Adding Images

You can also add images to illustrate concepts:

```markdown
<p align="center">
  <img src="images/figures/example-diagram.png" alt="Example Diagram" width="600">
  <br>
  <em>Figure 1: Illustration of the concept</em>
</p>
```

### Image Directory Structure

```
/images/
├── figures/      # Paper figures and diagrams
├── equations/    # Rendered equation images (use sparingly)
├── results/      # Experimental results and plots
└── diagrams/     # Architecture diagrams and flowcharts
```

---

## Best Practices Summary

1. ✅ **Use LaTeX syntax** in markdown for all mathematical formulas
2. ✅ **Use display math** (`$$...$$`) for important standalone equations
3. ✅ **Use inline math** (`$...$`) for formulas within text
4. ✅ **Break complex derivations** into multiple steps
5. ✅ **Add explanatory text** around equations
6. ✅ **Define symbols** before using them
7. ✅ **Use consistent notation** throughout the document
8. ✅ **Add images** to `/images/` directory with descriptive names
9. ✅ **Include alt text** for accessibility
10. ✅ **Reference equations** with labels like (S16), (S17), etc.

---

## Tools for Writing

- **VS Code** with Markdown Preview Enhanced extension
- **Typora** - WYSIWYG markdown editor with LaTeX support
- **Overleaf** - Online LaTeX editor (for .tex files)
- **GitHub** - Built-in markdown and LaTeX rendering

---

## Further Reading

- [FORMATTING_GUIDE.md](FORMATTING_GUIDE.md) - Complete formatting guide
- [README.md](README.md) - Repository overview
- [Question.md](Question.md) - Example of improved formatting

---

**Result:** Mathematical formulas are now clear, professional, and easy to read! 🎉
