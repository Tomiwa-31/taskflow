---
paths: ["**/*test*.py", "tests/**"]
---

# Rule: Test files

When editing anything matched by this rule:
- Use plain pytest-style functions (`def test_...():`), never unittest classes.
- Keep each test focused on one behavior.
- Don't mock `src/tasks.py` internals — test through its public functions only.
