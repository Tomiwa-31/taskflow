# TaskFlow — Project Instructions

This is the **project-level** CLAUDE.md. It lives in the repo root, is committed
to git, and is shared with every teammate who opens this project in Claude Code.
(Compare this to a *user-level* file at `~/.claude/CLAUDE.md`, which is private
to one machine and applies to ALL projects — see README.md for why mixing the
two up is the #1 cause of "Claude ignores our conventions" bugs.)

## What this project is
TaskFlow is a deliberately tiny Python CLI for managing a task list. The app
itself isn't the point — it exists to give Claude Code real files to apply
rules, commands, and skills against.

## Modular config via @import
Rather than cramming everything into this one file, the details are split into
topic-specific files and pulled in below. Claude Code should load all of them
when this file is read.

@.claude/docs/code-style.md
@.claude/docs/testing-conventions.md
@.claude/docs/architecture.md

## Quick facts
- Language: Python 3.11
- Entry point: `src/cli.py`
- Tests: `pytest`, located in `tests/`

## Common commands
- Run the app: `python src/cli.py list`
- Run tests: `pytest -q`

## Try this
Run `/memory` in Claude Code right now and confirm you see this file AND the
three imported docs listed as loaded context.
