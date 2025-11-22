# Quick Start Guide

This is a quick reference for the improvements made to address Issue #59.

## 🚀 TL;DR

1. **Formulas**: Use LaTeX syntax with `$...$` (inline) or `$$...$$` (display)
2. **File Type**: Keep using `.md` files (no change needed!)
3. **Images**: Save to `/images/` directory, reference in markdown

## ✨ Quick Examples

### Writing Mathematical Formulas

**Inline formula:**
```markdown
The kinetic energy operator is $\hat{T} = -\frac{1}{2}\nabla^2$.
```
Renders as: The kinetic energy operator is $\hat{T} = -\frac{1}{2}\nabla^2$.

**Display formula:**
```markdown
$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} = 2\hat{T}\phi_i(r) + 2V_{eff}[\rho[\Phi]](r)\phi_i(r)
$$
```
Renders as:
$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} = 2\hat{T}\phi_i(r) + 2V_{eff}[\rho[\Phi]](r)\phi_i(r)
$$

### Adding Images

**Step 1:** Save your image to the appropriate directory:
```bash
# Save figure to images/figures/
# Save result plot to images/results/
# Save diagram to images/diagrams/
```

**Step 2:** Reference in markdown:
```markdown
![Model Architecture](images/figures/model-architecture.png)
```

Or with caption and size:
```markdown
<p align="center">
  <img src="images/figures/model-architecture.png" alt="Model Architecture" width="600">
  <br>
  <em>Figure 1: Overview of the proposed model architecture</em>
</p>
```

## 📚 Common LaTeX Symbols

| What You Want | LaTeX Code | Example |
|---------------|-----------|---------|
| Greek letter phi | `\phi` | $\phi$ |
| Hat symbol | `\hat{T}` | $\hat{T}$ |
| Fraction | `\frac{a}{b}` | $\frac{a}{b}$ |
| Summation | `\sum_{i=1}^{n}` | $\sum_{i=1}^{n}$ |
| Integral | `\int_{a}^{b}` | $\int_{a}^{b}$ |
| Nabla | `\nabla` | $\nabla$ |
| Partial derivative | `\partial` | $\partial$ |
| Angle brackets | `\langle x \rangle` | $\langle x \rangle$ |
| Delta | `\delta` | $\delta$ |
| Lambda | `\lambda` | $\lambda$ |

## 📖 Full Documentation

- **FORMATTING_GUIDE.md** - Complete guide with all details
- **ISSUE_SUMMARY.md** - Direct answers to your questions
- **EXAMPLE_IMPROVEMENTS.md** - Before/after comparisons
- **README.md** - Repository overview

## 🎯 Where to Go Next

1. Check out **Question.md** to see the improved formulas in action
2. Read **FORMATTING_GUIDE.md** for comprehensive documentation
3. Look at **EXAMPLE_IMPROVEMENTS.md** for before/after comparisons
4. Start adding images to `/images/` directory

## ❓ Still Have Questions?

- **For formula syntax**: See FORMATTING_GUIDE.md, section "Mathematical Formulas in Markdown"
- **For image usage**: See FORMATTING_GUIDE.md, section "Adding Images"
- **For file types**: See FORMATTING_GUIDE.md, section "When to Use .md vs .tex Files"
- **For examples**: See EXAMPLE_IMPROVEMENTS.md

---

**That's it! You're ready to write beautiful mathematical documents! 🎉**
