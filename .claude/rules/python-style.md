---
paths: ["**/*.py"]
---

# Rule: Python files

When editing any `.py` file in this repo:
- Enforce the style rules in `.claude/docs/code-style.md`.
- Add/adjust type hints if you touch a function signature.
- If you rename or add a function in `src/`, remind the user a matching test
  is expected (see the testing rule).
