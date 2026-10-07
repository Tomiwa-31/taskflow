"""Thin CLI wrapper. Handles argv and printing only — see architecture.md."""
from __future__ import annotations

import sys

from tasks import TaskList

_LIST = TaskList()


def main(argv: list[str]) -> None:
    """Entry point: dispatch on the first CLI argument."""
    if not argv:
        print("Usage: cli.py [add <title> | done <index> | list]")
        return

    command = argv[0]
    if command == "add" and len(argv) > 1:
        task = _LIST.add(" ".join(argv[1:]))
        print(f"Added: {task.title}")
    elif command == "done" and len(argv) > 1:
        task = _LIST.complete(int(argv[1]))
        print(f"Completed: {task.title}")
    elif command == "list":
        for i, task in enumerate(_LIST.all()):
            mark = "x" if task.done else " "
            print(f"[{mark}] {i}: {task.title}")
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main(sys.argv[1:])
