"""Pure task-list logic. No I/O — see architecture.md."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Task:
    """A single task with a title and completion state."""
    
    title: str
    done: bool = False


@dataclass
class TaskList:
    """An in-memory collection of tasks."""
    tasks: list[Task] = field(default_factory=list)

    def add(self, title: str) -> Task:
        """Add a new task and return it."""
        task = Task(title=title)
        self.tasks.append(task)
        return task

    def complete(self, index: int) -> Task:
        """Mark the task at `index` as done and return it."""
        task = self.tasks[index]
        task.done = True
        return task

    def all(self) -> list[Task]:
        """Return all tasks."""
        return list(self.tasks)
