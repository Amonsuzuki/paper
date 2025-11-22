# Images Directory

This directory contains all images used in the repository's documentation and research notes.

## Directory Structure

```
/images/
├── figures/          # Paper figures and diagrams from research
├── equations/        # Screenshots or rendered images of complex equations
├── results/          # Experimental results, plots, and visualizations
└── diagrams/         # Architecture diagrams, flowcharts, and conceptual illustrations
```

## Subdirectories

### `/figures/`
Contains figures extracted from papers or created for research documentation:
- Model architectures
- Concept illustrations
- Workflow diagrams

### `/equations/`
Contains rendered mathematical equations saved as images:
- Complex derivations that are better shown as images
- Equation screenshots from papers
- LaTeX-rendered formulas for documentation

### `/results/`
Contains experimental results and visualizations:
- Performance plots
- Comparison charts
- Statistical visualizations
- Error analysis graphs

### `/diagrams/`
Contains technical diagrams and flowcharts:
- System architecture diagrams
- Algorithm flowcharts
- Network topology illustrations
- Process diagrams

## Image Guidelines

### Naming Conventions
- Use descriptive, lowercase names with hyphens
- Include subject/topic prefix
- Examples:
  - `dft-hamiltonian-architecture.png`
  - `energy-prediction-results.png`
  - `training-loss-comparison.png`

### File Formats
- **PNG**: Diagrams, screenshots, figures with transparency
- **JPEG**: Photographs, complex images without transparency
- **SVG**: Vector graphics (preferred for diagrams when possible)

### File Size
- Keep individual images under 1 MB when possible
- Compress large images before committing
- Consider using Git LFS for files larger than 1 MB

### Adding New Images

1. Save image to appropriate subdirectory
2. Use descriptive filename
3. Reference in markdown:
   ```markdown
   ![Description](images/subdirectory/filename.png)
   ```
4. Add caption and alt text for accessibility

### Example Usage

```markdown
<p align="center">
  <img src="images/figures/model-architecture.png" alt="Model Architecture" width="600">
  <br>
  <em>Figure 1: Overview of the proposed model architecture</em>
</p>
```

## Best Practices

1. ✅ Always add alt text for accessibility
2. ✅ Include captions explaining what the image shows
3. ✅ Optimize image size before committing
4. ✅ Use relative paths from markdown files
5. ✅ Keep source files (e.g., .drawio, .pptx) in a separate location
6. ✅ Credit sources for images from papers

## Tools for Creating Images

### Diagrams
- [Draw.io](https://www.drawio.com/) - Free online diagram tool
- [Lucidchart](https://www.lucidchart.com/) - Professional diagramming
- TikZ (LaTeX) - Programmatic diagram creation

### Plots and Visualizations
- Matplotlib (Python)
- ggplot2 (R)
- Plotly (Python/JavaScript)
- pgfplots (LaTeX)

### Image Optimization
- [TinyPNG](https://tinypng.com/) - PNG compression
- [ImageOptim](https://imageoptim.com/) - Mac image optimization
- pngquant - Command-line PNG compression

---

**Note:** This directory structure was created following the guidelines in `FORMATTING_GUIDE.md`. See that file for comprehensive documentation on using images and formulas in this repository.
