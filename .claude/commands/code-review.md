---
description: Run a quick static review checklist on the current changes
---

Review the currently changed files (or, if none are changed, review `src/`)
against this checklist and report findings as a short bullet list:

1. Do all functions have type hints and docstrings?
2. Is any I/O logic leaking into `src/tasks.py`?
3. Are there functions in `src/` with no corresponding test in `tests/`?
4. Any bare `except:` clauses?
5. Any function over ~25 lines that should be split up?

Do not make edits — just report what you find.


###think of this as a saved prompt and instead of typing it out to claude you just say /code-review