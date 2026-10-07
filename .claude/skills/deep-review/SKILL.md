---
name: deep-review
description: >
  Runs a thorough, multi-file audit of the codebase for style, testing
  coverage, and architecture violations. Use for a deep pass across many
  files rather than a quick glance.
context: fork
allowed-tools: ["Read", "Grep", "Glob"]
---

# Deep Review Skill

This skill runs as a forked sub-agent (see `context: fork` above) so that
scanning every file in the project doesn't pollute or burn through the main
session's context window. It's also restricted to read-only tools via
`allowed-tools` — it can Read, Grep, and Glob, but cannot Edit, Write, or run
Bash. That's the Principle of Least Privilege in action: this skill's job is
to *find* problems, not fix them.

## Steps
1. Glob all `*.py` files under `src/` and `tests/`.
2. For each file in `src/`, check:
   - Type hints and docstrings present (per `.claude/docs/code-style.md`)
   - No I/O logic in `tasks.py`
   - A matching test exists in `tests/`
3. For each file in `tests/`, check it follows `.claude/docs/testing-conventions.md`.
4. Return a single structured report: file path → issues found. No edits.

## When to use this vs. the `/code-review` command
- `/code-review` (a slash command) is a quick, static, single-prompt pass —
  good for "check what I just changed."
- `deep-review` (this skill) is for "audit the whole project," runs in its
  own forked context, and can reason over many files without spending the
  main conversation's tokens.
