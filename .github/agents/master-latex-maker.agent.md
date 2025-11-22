---
# Fill in the fields below to create a basic custom agent for your repository.
# The Copilot CLI can be used for local testing: https://gh.io/customagents/cli
# To make this agent available, merge this file into the default repository branch.
# For format details, see: https://gh.io/customagents/config

name: master latex maker
description: convert all unconverted pdf files to latex files by calling latex-maker agent each times.
tools: ['shell', 'read', 'edit', 'search', 'custom-agent', 'web', 'todo']
---

# My Agent
