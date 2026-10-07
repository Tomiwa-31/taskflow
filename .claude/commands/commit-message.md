---
description: Draft a conventional-commits style commit message for staged changes
---

Look at the staged git changes (`git diff --staged`) and draft a commit
message using the Conventional Commits format:

```
<type>(<scope>): <short summary>

<body: 1-3 bullet points on what changed and why>
```

Valid types: feat, fix, refactor, test, docs, chore. Keep the summary line
under 72 characters. Don't run `git commit` — just output the message.
