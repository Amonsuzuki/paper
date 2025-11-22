# Custom Agents Documentation

This directory contains custom agent configurations for GitHub Copilot. These agents help automate various tasks related to paper management and analysis.

## Agent Types

### Worker Agents
These agents perform specific tasks:

1. **60qa-respondant** - Answers questions about research papers based on the 60qa methodology
2. **latex_maker** - Converts PDF papers to LaTeX format
3. **question-respondant** - Answers general questions about papers

### Master Agents (Orchestrators)
These agents coordinate worker agents to complete complex workflows:

1. **master-60qa-respondant** - Orchestrates the complete 60qa process by invoking `60qa-respondant` three times (for questions 1-20, 21-40, and 41-60)
2. **master-latex-maker** - Coordinates conversion of multiple PDF files by invoking `latex_maker` for each unconverted PDF

## How Master Agents Invoke Other Agents

Master agents use the `custom-agent` tool to invoke worker agents. Here's the pattern:

### Configuration Requirements
1. The master agent must include `'custom-agent'` in its `tools` list
2. The agent prompt must include clear instructions on:
   - Which custom agent to invoke
   - What prompt/parameters to pass
   - The expected workflow

### Example Invocation Pattern

In the master agent's instructions:
```markdown
## How to Invoke Custom Agents

Use the `custom-agent` tool available to you. 

Invoke the `worker-agent-name` agent with a prompt like:
```
Detailed instructions for the worker agent including:
- What task to perform
- Input file locations
- Output file locations
- Any specific requirements
```

## Best Practices

### For Master Agents:
1. **Be Explicit**: Provide clear, step-by-step instructions for invoking child agents
2. **Include Examples**: Show example prompts for invoking worker agents
3. **Verify Results**: Check that each worker agent completed successfully before proceeding
4. **Don't Execute**: Master agents should coordinate, not perform the actual work
5. **Sequential Processing**: Process tasks one at a time to ensure quality

### For Worker Agents:
1. **Single Responsibility**: Each agent should have one clear purpose
2. **Clear Input/Output**: Specify expected input and output formats
3. **Self-Contained**: Include all necessary instructions within the agent definition
4. **Status Reporting**: Indicate completion or failure clearly

## Usage Examples

### Using master-60qa-respondant
```
@copilot Use the master-60qa-respondant agent to complete the 60qa analysis for "Paper Title"
```

The master agent will:
1. Invoke 60qa-respondant for questions 1-20
2. Wait for completion
3. Invoke 60qa-respondant for questions 21-40
4. Wait for completion
5. Invoke 60qa-respondant for questions 41-60
6. Report final status

### Using master-latex-maker
```
@copilot Use the master-latex-maker agent to convert all PDFs to LaTeX
```

The master agent will:
1. Scan the pdf/ directory
2. Identify unconverted PDFs
3. Invoke latex_maker for each PDF
4. Verify each conversion
5. Report summary of conversions

## Troubleshooting

### Master Agent Not Invoking Child Agents
- Verify `custom-agent` is in the tools list
- Check that instructions explicitly mention using the custom-agent tool
- Ensure the child agent name is spelled correctly

### Child Agent Not Found
- Verify the child agent file exists in `.github/agents/`
- Check that the agent name in the file matches the name used in invocation
- Ensure the agent file has been merged to the default branch

## File Structure

```
.github/agents/
├── README.md                           # This file
├── 60qa-respondant.agent.md           # Worker agent for 60qa questions
├── latex_maker.agent.md               # Worker agent for PDF to LaTeX conversion
├── question-respondant.agent.md       # Worker agent for general questions
├── master-60qa-respondant.agent.md    # Master agent for complete 60qa workflow
└── master-latex-maker.agent.md        # Master agent for batch PDF conversion
```

## Additional Resources

- [GitHub Custom Agents Documentation](https://gh.io/customagents/config)
- [Copilot CLI for Local Testing](https://gh.io/customagents/cli)
- [60qa Methodology Template](/60qa/template.md)
