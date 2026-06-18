from typing import Dict, List

Task = Dict[str, object]


def add_task(tasks: List[Task], title: str) -> List[Task]:
    tasks.append({"title": title, "done": False})
    return tasks


def complete_task(tasks: List[Task], title: str) -> List[Task]:
    for task in tasks:
        if task["title"] == title:
            task["done"] = True
            break
    return tasks


def list_all_tasks(tasks: List[Task]) -> List[Task]:
    return tasks
