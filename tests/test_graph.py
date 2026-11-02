"""Unit tests for TaskDAG."""
import unittest
from agent_task_graph.graph import TaskDAG

class TestTaskDAG(unittest.TestCase):
    def test_waves(self):
        dag = TaskDAG()
        dag.add_task("A")
        dag.add_task("B", depends_on=["A"])
        dag.add_task("C", depends_on=["A"])
        dag.add_task("D", depends_on=["B", "C"])
        waves = dag.get_execution_order()
        self.assertEqual(waves, [["A"], ["B", "C"], ["D"]])

    def test_cycle(self):
        dag = TaskDAG()
        dag.add_task("A", depends_on=["B"])
        dag.add_task("B", depends_on=["A"])
        with self.assertRaises(ValueError):
            dag.get_execution_order()

if __name__ == "__main__":
    unittest.main()
