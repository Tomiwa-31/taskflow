# Architecture

- `src/tasks.py` — pure data logic (add/complete/list tasks). No I/O here.
- `src/cli.py` — thin command-line wrapper around `tasks.py`. Handles argv
  parsing and printing only.
- `tests/` — mirrors `src/` one-to-one.

Keep logic and I/O separated so `tasks.py` stays easy to unit test.
