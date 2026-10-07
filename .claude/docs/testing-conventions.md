# Testing Conventions

- All tests live under `tests/` and are named `test_*.py`.
- Use plain `pytest` functions, not unittest classes.
- Every new function in `src/` needs at least one corresponding test.
- Tests should be independent — no shared mutable state between tests.
