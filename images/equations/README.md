# Equations Directory

Store rendered mathematical equation images here when you need to include complex equations as images rather than LaTeX code.

## When to Use

Use this directory when:
- You need to include equations in contexts where LaTeX rendering is not available
- You want to include screenshots of equations from papers
- You need to show how equations render in different tools

## Best Practices

1. Name files descriptively: `dft-functional-derivative.png`
2. Include the LaTeX source in a comment or separate file
3. Use high resolution (300 DPI minimum)
4. Keep background transparent when possible

## Creating Equation Images

### From LaTeX

Use online tools or command-line:
```bash
# Using LaTeX with standalone class
pdflatex equation.tex
convert -density 300 equation.pdf equation.png
```

### From Online Tools
- [LaTeX Equation Editor](https://latex.codecogs.com/eqneditor/editor.php)
- [Overleaf](https://www.overleaf.com/)
- Take screenshots with proper DPI

## Note

**Prefer LaTeX syntax in markdown** (`$...$` or `$$...$$`) over images when possible, as it's more maintainable and searchable. Use images only when necessary.
