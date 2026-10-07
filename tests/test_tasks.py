import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from tasks import TaskList


def test_add_creates_task():
    tl = TaskList()
    task = tl.add("Write CLAUDE.md")
    assert task.title == "Write CLAUDE.md"
    assert task.done is False


def test_complete_marks_done():
    tl = TaskList()
    tl.add("Read the docs")
    completed = tl.complete(0)
    assert completed.done is True


def test_all_returns_every_task():
    tl = TaskList()
    tl.add("one")
    tl.add("two")
    assert len(tl.all()) == 2
