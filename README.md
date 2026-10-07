# TaskFlow — a Claude Code config sandbox

A tiny Python task-list CLI, built specifically to let you practice Claude
Code's configuration system: CLAUDE.md hierarchy, `@import`, `.claude/rules`,
slash commands, and skills.

## Setup
1. Unzip this folder and `cd` into it.
2. (Optional) `git init && git add . && git commit -m "init"` — several of
   the exercises below assume this is a real git repo.
3. Open the folder in Claude Code.

## Exercises, mapped to the two videos

### 1. CLAUDE.md hierarchy (video 1)
- Run `/memory` right away. You should see `CLAUDE.md` plus the three files
  it imports from `.claude/docs/`.
- **Reproduce the common pitfall**: create `~/.claude/CLAUDE.md` (user-level)
  with some instruction, e.g. "Always answer in French." Start a fresh
  session in this project and notice it applies everywhere — then imagine a
  teammate who *doesn't* have that file: they won't see it, because it's
  private to your machine, not the repo. That mismatch is exactly the
  "ignores our conventions" bug from the video. Delete it when you're done
  experimenting.
- Try a directory-level file: add `src/CLAUDE.md` with a note like "Files in
  this folder must not perform I/O." Ask Claude to edit `src/tasks.py` and
  see whether it respects the extra, more specific instruction.

### 2. @import (video 1)
- Open `.claude/docs/code-style.md` and change one rule. Ask Claude to add a
  new function to `src/tasks.py` and check whether it follows the change —
  confirms the import is actually being read, not cached.

### 3. Rules with glob paths (video 1)
- `.claude/rules/python-style.md` targets `**/*.py`.
- `.claude/rules/testing.md` targets `**/*test*.py` and `tests/**`.
- Ask Claude to edit `tests/test_tasks.py` vs. `src/cli.py` in two separate
  requests and compare which rule's instructions show up in its reasoning —
  this confirms path-based conditional loading.

### 4. Slash commands (video 2)
- Run `/code-review` — it should walk the static checklist in
  `.claude/commands/code-review.md` against `src/`.
- Stage a change (`git add`) and run `/commit-message` to see the
  conventional-commit draft.

### 5. Skills + context fork + allowed-tools (video 2)
- Run the `deep-review` skill (e.g. "use the deep-review skill to audit the
  project"). Notice it runs as a forked sub-agent and reports back a summary
  rather than filling your main session with every file it reads.
- Try asking it to *fix* something it finds — it shouldn't be able to, since
  `allowed-tools` only grants `Read`, `Grep`, and `Glob`, not `Edit` or
  `Write`. That's the least-privilege principle from the video made concrete.

### 6. Put it together
- Add a new feature (e.g. `delete` command in `cli.py` + `TaskList.delete`).
- Notice: the python-style rule should push you toward type hints/docstrings,
  CLAUDE.md's imported testing conventions should prompt a new test, and you
  can finish with `/code-review` then `/commit-message`.

## Project layout
```
taskflow/
├── CLAUDE.md                        # project-level, committed, @imports below
├── .claude/
│   ├── docs/                        # topic files pulled in via @import
│   │   ├── code-style.md
│   │   ├── testing-conventions.md
│   │   └── architecture.md
│   ├── rules/                       # glob-scoped conditional instructions
│   │   ├── python-style.md
│   │   └── testing.md
│   ├── commands/                    # slash commands (static prompts)
│   │   ├── code-review.md
│   │   └── commit-message.md
│   └── skills/
│       └── deep-review/
│           └── SKILL.md             # context: fork + allowed-tools
├── src/
│   ├── tasks.py
│   └── cli.py
└── tests/
    └── test_tasks.py
```
