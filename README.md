# Research Paper Repository

This repository contains research papers, analysis documents, and notes related to machine learning and density functional theory (DFT).

## 📚 Repository Structure

```
/paper/
├── README.md                    # This file
├── FORMATTING_GUIDE.md          # Guide for writing formulas and adding images
├── Question.md                  # Research questions with answers
├── idea.md                      # Research ideas and task tracking
├── /60qa/                       # 60QA methodology for paper analysis
│   ├── template.md             # Template for 60QA analysis
│   ├── /ml-dft/                # DFT-related paper analyses
│   └── /security/              # Security-related paper analyses
├── /latex/                      # LaTeX source files of papers
│   ├── README.md               # Description of LaTeX files
│   └── /ml-dft/                # DFT paper LaTeX files
├── /pdf/                        # Original PDF papers
│   ├── /ml-dft/                # Machine learning for DFT
│   ├── /security/              # Security papers
│   └── /ai4research/           # AI for research papers
└── /images/                     # Images, figures, and diagrams
    ├── README.md               # Image guidelines
    ├── /figures/               # Paper figures and diagrams
    ├── /equations/             # Rendered equation images
    ├── /results/               # Experimental results
    └── /diagrams/              # Architecture diagrams
```

## 🎯 Key Features

### 1. **60QA Methodology**
A structured approach to analyzing research papers by answering ~60 questions organized into 7 sections:
- Introduction (10 questions)
- Related Work (5 questions)
- Problem Statement (8 questions)
- Method (11 questions)
- Experimental Setup (11 questions)
- Experimental Results (14 questions)
- Conclusions (3 questions)

See [`60qa/template.md`](60qa/template.md) for the complete template.

### 2. **Multi-Format Support**
- **PDF**: Original papers in `/pdf/` directory
- **LaTeX**: Converted LaTeX sources in `/latex/` directory
- **Markdown**: Analysis and notes with proper mathematical notation

### 3. **Mathematical Formula Support**
This repository uses LaTeX syntax within markdown files for mathematical formulas:

**Inline math:** `$E = mc^2$` → $E = mc^2$

**Display math:**
```markdown
$$
\hat{F}[\rho[\Phi]]\phi_i = \varepsilon_i\phi_i
$$
```

See [`FORMATTING_GUIDE.md`](FORMATTING_GUIDE.md) for comprehensive documentation on formatting.

### 4. **Image Support**
Images are organized in the `/images/` directory with subdirectories for different types:
- Figures from papers
- Rendered equations
- Experimental results
- Architecture diagrams

## 📖 How to Use This Repository

### For Reading and Understanding Papers

1. **Start with PDF papers** in `/pdf/` directory
2. **Read 60QA analysis** in `/60qa/` for structured understanding
3. **Check LaTeX source** in `/latex/` for detailed equations
4. **Review research questions** in `Question.md` for specific topics

### For Writing Mathematical Content

1. **Read the formatting guide**: [`FORMATTING_GUIDE.md`](FORMATTING_GUIDE.md)
2. **Use LaTeX syntax** for mathematical formulas in markdown files
3. **Add images** to `/images/` directory with proper organization
4. **Follow naming conventions** for files and images

### For Contributing

1. Use markdown (`.md`) for:
   - Documentation and guides
   - Research notes and questions
   - 60QA responses
   - Quick summaries

2. Use LaTeX (`.tex`) for:
   - Formal paper drafts
   - Complex mathematical derivations
   - Publication-ready documents

3. Store images in `/images/` with descriptive names

4. Update relevant README files when adding new content

## 🔬 Research Topics

### Machine Learning for Density Functional Theory (ML-DFT)

Papers exploring the application of machine learning to improve DFT calculations:

- **Orbital-Free DFT**: Deep learning approaches to overcome traditional barriers
- **Hamiltonian Prediction**: Self-consistency training and adaptive sparsity
- **DFT Approximations**: Machine learning for accuracy improvements

### Security and Distributed Learning

Papers on decentralized learning and Byzantine-resilient algorithms:

- Decentralized learning with fault tolerance
- Byzantine attack defense mechanisms

### AI for Research

Papers on using AI to accelerate research processes.

## 🛠️ Tools and Resources

### Recommended Tools

- **LaTeX Editors**: [Overleaf](https://www.overleaf.com/), VS Code with LaTeX Workshop
- **Markdown Editors**: VS Code, Typora, GitHub
- **Diagram Tools**: Draw.io, Lucidchart, TikZ
- **Plot Tools**: Matplotlib, ggplot2, Plotly

### Useful Resources

- [FORMATTING_GUIDE.md](FORMATTING_GUIDE.md) - Comprehensive guide for formulas and images
- [LaTeX Math Symbols](https://www.ctan.org/pkg/comprehensive) - Comprehensive symbol list
- [Markdown Guide](https://www.markdownguide.org/) - Markdown syntax reference

## 📝 File Format Guidelines

### When to Use Different Formats

| Format | Use Case | Advantages |
|--------|----------|------------|
| **Markdown (.md)** | Documentation, notes, 60QA | GitHub preview, easy collaboration |
| **LaTeX (.tex)** | Formal papers, complex math | Publication quality, precise control |
| **PDF (.pdf)** | Final papers, references | Universal format, preserves layout |

### Mathematical Notation

Always use proper LaTeX syntax for mathematical formulas in markdown:

❌ **Bad:** `1(−1/2)⟨ϕj|∇2|ϕj⟩`

✅ **Good:** `$(-\frac{1}{2})\langle\phi_j|\nabla^2|\phi_j\rangle$`

See examples in `Question.md` for properly formatted mathematical content.

## 🤝 Collaboration Guidelines

### For Questions and Answers

1. Add questions to `Question.md` with proper LaTeX formatting
2. Number questions for easy reference
3. Include references to source papers
4. Provide detailed explanations with step-by-step derivations

### For Paper Analysis (60QA)

1. Use the template in `60qa/template.md`
2. Save analysis in appropriate subdirectory (e.g., `/60qa/ml-dft/`)
3. Use `.md` format for better version control
4. Include both Japanese and English section headers if applicable

### For Adding Papers

1. Add PDF to `/pdf/` in appropriate subdirectory
2. Add LaTeX source (if available) to `/latex/`
3. Create 60QA analysis in `/60qa/`
4. Update relevant README files

## 📊 Current Status

### Completed 60QA Analyses

- ✅ Machine learning for accuracy in density functional approximations
- ✅ Overcoming the Barrier of Orbital-Free Density Functional Theory
- ✅ Decentralized Learning (masuda-ICCE-2025)

### Papers with LaTeX Sources

- 8 papers in `/latex/ml-dft/` with full LaTeX sources
- See [`latex/README.md`](latex/README.md) for details

### Research Questions

- 3 active questions in `Question.md` with detailed answers
- Topics: DFT functional derivatives, Lagrange multipliers, GitHub containers

## 🔗 Related Resources

- [60QA Methodology](60qa/template.md) - Paper analysis framework
- [LaTeX Papers](latex/README.md) - Converted paper sources
- [Image Guidelines](images/README.md) - Image organization and usage

## 💡 Tips for Better Readability

1. **Use display math for complex equations**: Makes formulas stand out
2. **Break long derivations into steps**: Easier to follow logic
3. **Add explanatory text**: Don't let equations stand alone
4. **Include references**: Link back to source papers
5. **Use consistent notation**: Define symbols once, use everywhere

## 📧 Questions or Suggestions?

- Open an issue on GitHub
- See `idea.md` for research ideas and ongoing tasks
- Check `Question.md` for answered research questions

---

**Last Updated:** 2025-11-22

**Maintained by:** Research team using GitHub Copilot for collaboration
