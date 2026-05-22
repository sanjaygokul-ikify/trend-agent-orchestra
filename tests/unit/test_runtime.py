from unittest import TestCase
from packages.core.engine import Engine
from packages.core.types import Task


class TestRuntime(TestCase):
    def test_execute_task(self):
        engine = Engine()
        task = Task(id='task-1', priority='LOW', requirements='test-requirement')
        engine.ingest_task(task)
        engine.execute_task(task)
        self.assertEqual(task.status, 'COMPLETED')
