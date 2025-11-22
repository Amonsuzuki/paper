# Formatting Guide for Mathematical Formulas and Images

This guide explains how to properly format mathematical formulas and add images in this repository to improve readability and maintainability.

## Table of Contents
1. [Mathematical Formulas in Markdown](#mathematical-formulas-in-markdown)
2. [Adding Images](#adding-images)
3. [When to Use .md vs .tex Files](#when-to-use-md-vs-tex-files)
4. [Best Practices](#best-practices)
5. [Examples](#examples)

---

## Mathematical Formulas in Markdown

### Basic LaTeX Syntax in Markdown

Markdown supports LaTeX mathematical notation through two modes:

#### 1. **Inline Math** (for formulas within text)
Use single dollar signs: `$formula$`

**Example:**
```markdown
The kinetic energy operator is defined as $\hat{T} = -\frac{1}{2}\nabla^2$.
```

**Renders as:** The kinetic energy operator is defined as $\hat{T} = -\frac{1}{2}\nabla^2$.

#### 2. **Display Math** (for standalone formulas)
Use double dollar signs: `$$formula$$` or code blocks with math:

**Example:**
```markdown
$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} = \frac{\delta \sum_{j=1}^{N}(-\frac{1}{2})\langle\phi_j|\nabla^2|\phi_j\rangle}{\delta \phi_i(r)} + \int \frac{\delta E_{eff}[\rho[\Phi]]}{\delta \rho(r')}\frac{\delta \rho[\Phi](r')}{\delta \phi_i(r)}dr'
$$
```

**Renders as:**
$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} = \frac{\delta \sum_{j=1}^{N}(-\frac{1}{2})\langle\phi_j|\nabla^2|\phi_j\rangle}{\delta \phi_i(r)} + \int \frac{\delta E_{eff}[\rho[\Phi]]}{\delta \rho(r')}\frac{\delta \rho[\Phi](r')}{\delta \phi_i(r)}dr'
$$

### Common Mathematical Symbols

| Symbol | LaTeX Code | Description |
|--------|-----------|-------------|
| $\alpha, \beta, \gamma$ | `\alpha, \beta, \gamma` | Greek letters |
| $\nabla$ | `\nabla` | Nabla (gradient) |
| $\partial$ | `\partial` | Partial derivative |
| $\int$ | `\int` | Integral |
| $\sum$ | `\sum` | Summation |
| $\hat{T}$ | `\hat{T}` | Hat (operator) |
| $\langle \phi \rangle$ | `\langle \phi \rangle` | Angle brackets |
| $\frac{a}{b}$ | `\frac{a}{b}` | Fraction |
| $x^2$ | `x^2` | Superscript |
| $x_i$ | `x_i` | Subscript |
| $\mathbb{R}$ | `\mathbb{R}` | Blackboard bold |
| $\mathbf{x}$ | `\mathbf{x}` | Bold font |

### Multi-line Equations

For multi-line equations with alignment, use the `align` environment:

```markdown
$$
\begin{align}
\hat{F}[\rho[\Phi]]\phi_i &:= \hat{T}\phi_i + V_{eff}[\rho[\Phi]]\phi_i \\
&= \varepsilon_i\phi_i, \quad \forall i = 1, \ldots, N
\end{align}
$$
```

---

## Adding Images

### Image Directory Structure

Store images in organized directories:

```
/images/
  ├── figures/          # Paper figures and diagrams
  ├── equations/        # Screenshots of rendered equations
  ├── results/          # Experimental results and plots
  └── diagrams/         # Architecture diagrams and flowcharts
```

### Inserting Images in Markdown

#### Basic Image Syntax
```markdown
![Alt text](path/to/image.png)
```

#### Image with Caption and Sizing
```markdown
<p align="center">
  <img src="images/figures/model_architecture.png" alt="Model Architecture" width="600">
  <br>
  <em>Figure 1: Overview of the proposed model architecture</em>
</p>
```

#### Side-by-Side Images
```markdown
<p align="center">
  <img src="images/results/before.png" alt="Before" width="400">
  <img src="images/results/after.png" alt="After" width="400">
  <br>
  <em>Figure 2: Comparison of results (left: before, right: after)</em>
</p>
```

### Supported Image Formats

- **PNG** (.png) - Best for diagrams, screenshots, and figures with transparency
- **JPEG** (.jpg, .jpeg) - Best for photographs and complex images
- **SVG** (.svg) - Best for vector graphics (scalable, recommended for diagrams)
- **GIF** (.gif) - For animations (use sparingly)

### Best Practices for Images

1. **Use descriptive filenames**: `model_architecture.png` instead of `img1.png`
2. **Optimize file sizes**: Compress images to reduce repository size
3. **Add alt text**: Always include descriptive alt text for accessibility
4. **Use consistent sizing**: Maintain uniform dimensions across similar images
5. **Version control**: Don't commit large binary files; consider using Git LFS for large images

---

## When to Use .md vs .tex Files

### Use Markdown (.md) when:

- ✅ Writing documentation, README files, or guides
- ✅ Creating quick notes or summaries
- ✅ Equations are relatively simple
- ✅ Need quick preview on GitHub
- ✅ Writing 60QA responses or research notes
- ✅ Collaborating with non-LaTeX users

**Advantages:**
- Renders directly on GitHub
- Easier to learn and write
- Better for version control (readable diffs)
- Portable and platform-independent

### Use LaTeX (.tex) when:

- ✅ Writing formal research papers
- ✅ Complex mathematical derivations
- ✅ Need precise typesetting control
- ✅ Preparing for publication
- ✅ Multiple authors with LaTeX experience
- ✅ Need bibliography management (BibTeX)

**Advantages:**
- Superior mathematical typesetting
- Professional publication quality
- Fine-grained formatting control
- Extensive package ecosystem

### Hybrid Approach

For this repository, we use a **hybrid approach**:

1. **Original papers**: Store as `.tex` in `/latex/` directory
2. **Research notes and Q&A**: Use `.md` with LaTeX math syntax
3. **Documentation**: Use `.md` for better GitHub integration
4. **60QA responses**: Use `.md` format (convert from `.txt` if needed)

---

## Best Practices

### For Mathematical Formulas

1. **Use proper notation**:
   - Bad: `1(−1/2)⟨ϕj|∇2|ϕj⟩`
   - Good: `$(-\frac{1}{2})\langle\phi_j|\nabla^2|\phi_j\rangle$`

2. **Break complex equations into steps**:
   ```markdown
   First, we derive the functional derivative:
   $$
   \frac{\delta E[\Phi]}{\delta \phi_i(r)} = 2\hat{T}\phi_i(r) + 2V_{eff}[\rho[\Phi]](r)\phi_i(r)
   $$
   
   Then, applying the orthonormality constraint:
   $$
   \hat{T}\phi_i(r) + V_{eff}[\rho[\Phi]](r)\phi_i(r) = \varepsilon_i\phi_i(r)
   $$
   ```

3. **Add explanatory text**: Don't just dump equations; explain what they mean

4. **Use consistent notation**: Define symbols once and use them consistently

### For Images

1. **Create images directory** if it doesn't exist:
   ```bash
   mkdir -p images/{figures,equations,results,diagrams}
   ```

2. **Reference images relatively**: Use relative paths from the markdown file

3. **Add captions**: Always explain what the image shows

4. **Keep source files**: If you create diagrams, keep the source files (e.g., .drawio, .pptx) in a separate `/source/` directory

### For File Organization

```
/paper/
├── README.md                    # Main documentation
├── FORMATTING_GUIDE.md          # This guide
├── Question.md                  # Research questions (use LaTeX syntax)
├── idea.md                      # Research ideas
├── /60qa/                       # 60QA methodology files
│   ├── template.md             # Template with proper formatting
│   └── /ml-dft/                # Subject-specific 60QAs
├── /latex/                      # Original LaTeX papers
│   └── README.md               # LaTeX file descriptions
├── /pdf/                        # Original PDF papers
├── /images/                     # All images (NEW)
│   ├── /figures/
│   ├── /equations/
│   ├── /results/
│   └── /diagrams/
└── .gitignore                   # Ignore large binaries
```

---

## Examples

### Example 1: Converting Plain Text to LaTeX

**Before (hard to read):**
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

**After (clear and readable):**
```markdown
For $i=1$, the variation of the energy functional $E[\Phi]$ in Eq. (S15) with respect to each orbital $\phi_i$ is required:

$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} = \frac{\delta \sum_{j=1}^{N}(-\frac{1}{2})\langle\phi_j|\nabla^2|\phi_j\rangle}{\delta \phi_i(r)} + \int \frac{\delta E_{eff}[\rho[\Phi]]}{\delta \rho(r')}\frac{\delta \rho[\Phi](r')}{\delta \phi_i(r)}dr'
$$
```

### Example 2: Adding Images to Documentation

```markdown
## Model Architecture

Our proposed model consists of three main components:

<p align="center">
  <img src="images/diagrams/architecture_overview.png" alt="Architecture Overview" width="700">
  <br>
  <em>Figure 1: Overview of the proposed three-stage architecture for DFT Hamiltonian prediction</em>
</p>

The input features are processed through:
1. Feature extraction module
2. Graph neural network layers
3. Output projection layer

### Example Results

<p align="center">
  <img src="images/results/energy_prediction.png" alt="Energy Prediction" width="500">
  <br>
  <em>Figure 2: Comparison of predicted vs. actual energies (MAE = 0.023 eV)</em>
</p>
```

### Example 3: Mathematical Proof with Explanations

```markdown
## Proof: Why the coefficient 2 disappears

Starting from equation (S16):
$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} = 2\hat{T}\phi_i(r) + 2V_{eff}[\rho[\Phi]](r)\phi_i(r)
$$

We impose the orthonormality constraint $\langle\phi_i|\phi_i\rangle = 1$ using Lagrange multipliers $\lambda_i$:
$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} - \lambda_i\frac{\delta\langle\phi_i|\phi_i\rangle}{\delta \phi_i(r)} = 0
$$

This yields:
$$
2\hat{T}\phi_i(r) + 2V_{eff}[\rho[\Phi]](r)\phi_i(r) = \lambda_i \cdot 2\phi_i(r)
$$

Dividing both sides by 2:
$$
\hat{T}\phi_i(r) + V_{eff}[\rho[\Phi]](r)\phi_i(r) = \lambda_i\phi_i(r)
$$

By defining $\varepsilon_i = \lambda_i$, we obtain equation (S18):
$$
\hat{F}[\rho[\Phi]]\phi_i := \hat{T}\phi_i + V_{eff}[\rho[\Phi]]\phi_i = \varepsilon_i\phi_i
$$

Therefore, the coefficient 2 is absorbed into the Lagrange multiplier when enforcing the constraint. ∎
```

---

## Tools and Resources

### Online LaTeX Editors
- [Overleaf](https://www.overleaf.com/) - Online LaTeX editor
- [LaTeX equation editor](https://latex.codecogs.com/eqneditor/editor.php) - Generate LaTeX equations

### Markdown Preview Tools
- GitHub: Automatically renders markdown with LaTeX
- VS Code: Install "Markdown Preview Enhanced" extension
- Typora: WYSIWYG markdown editor with LaTeX support

### Image Creation Tools
- **Diagrams**: Draw.io, Lucidchart, TikZ (LaTeX)
- **Plots**: Matplotlib (Python), ggplot2 (R), pgfplots (LaTeX)
- **Screenshots**: macOS (Cmd+Shift+4), Windows (Snipping Tool)
- **Compression**: TinyPNG, ImageOptim, pngquant

### Git Large File Storage (LFS)
For large image files (>1 MB), consider using Git LFS:
```bash
# Install Git LFS
git lfs install

# Track large image files
git lfs track "*.png"
git lfs track "*.jpg"

# Add .gitattributes
git add .gitattributes
```

---

## Quick Reference Card

| Task | Markdown Syntax |
|------|-----------------|
| Inline math | `$E = mc^2$` |
| Display math | `$$E = mc^2$$` |
| Greek letter | `$\alpha, \beta, \gamma$` |
| Fraction | `$\frac{a}{b}$` |
| Superscript | `$x^{2}$` |
| Subscript | `$x_{i}$` |
| Sum | `$\sum_{i=1}^{n}$` |
| Integral | `$\int_{a}^{b}$` |
| Matrix | `$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$` |
| Image | `![alt](path/to/image.png)` |
| Sized image | `<img src="..." width="500">` |

---

## Summary

- ✅ Use **LaTeX syntax in markdown** (with `$` and `$$`) for mathematical formulas
- ✅ Store images in an **organized `/images/` directory**
- ✅ Use **.md files** for notes and documentation, **.tex files** for formal papers
- ✅ Always add **alt text** to images for accessibility
- ✅ **Explain equations** with surrounding text
- ✅ Keep **consistent notation** throughout the repository

For questions or suggestions, please open an issue or discussion on GitHub.

---

**Last updated:** 2025-11-22
