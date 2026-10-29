"""Small command-line task tracker used for the Week 7 Gitflow exercise."""

__version__ = "0.1.0"


def create_task(title: str, priority: str = "medium") -> dict:
    """Create a task after validating its title and priority."""
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Task title cannot be empty.")

    allowed_priorities = {"low", "medium", "high"}
    normalized_priority = priority.strip().lower()
    if normalized_priority not in allowed_priorities:
        raise ValueError("Priority must be low, medium, or high.")

    return {
        "title": title.strip(),
        "priority": normalized_priority,
        "completed": False,
    }


def complete_task(task: dict) -> dict:
    """Return a completed copy of a task."""
    if not isinstance(task, dict) or "title" not in task:
        raise ValueError("A valid task dictionary is required.")
    updated = task.copy()
    updated["completed"] = True
    return updated


def show_menu() -> None:
    print(f"Task Tracker v{__version__}")
    print("Example task:", create_task("Water greenhouse plants", "high"))
    print("Completed task:", complete_task(create_task("Check soil moisture")))


if __name__ == "__main__":
    show_menu()
