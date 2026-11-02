"""Command line interface for agent-task-graph."""
from .graph import TaskDAG

def main():
    dag = TaskDAG()
    dag.add_task("lint")
    dag.add_task("test")
    dag.add_task("build", depends_on=["lint", "test"])
    print("Execution waves:", dag.get_execution_order())

if __name__ == "__main__":
    main()
