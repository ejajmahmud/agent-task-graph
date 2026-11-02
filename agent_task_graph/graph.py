"""Topological DAG scheduler."""
from typing import Dict, List, Set

class TaskDAG:
    def __init__(self):
        self.tasks: Set[str] = set()
        self.dependencies: Dict[str, Set[str]] = {}

    def add_task(self, task_name: str, depends_on: List[str] = None) -> None:
        self.tasks.add(task_name)
        self.dependencies[task_name] = set(depends_on or [])

    def get_execution_order(self) -> List[List[str]]:
        """Returns waves of tasks that can run in parallel."""
        remaining = set(self.tasks)
        completed = set()
        waves = []

        while remaining:
            ready = [t for t in remaining if self.dependencies[t].issubset(completed)]
            if not ready:
                raise ValueError("Cyclic dependency detected in task graph")
            waves.append(sorted(ready))
            completed.update(ready)
            remaining.difference_update(ready)

        return waves
