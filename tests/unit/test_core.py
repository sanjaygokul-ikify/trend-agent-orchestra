from unittest import TestCase
from packages.core.engine import Engine
from packages.core.types import Task


class TestEngine(TestCase):
    def test_ingest_task(self):
        engine = Engine()
        task = Task(id='task-1', priority='LOW', requirements='test-requirement')
        engine.ingest_task(task)
        self.assertIn(task.id, engine.tasks)

    def test_allocate_task(self):
        engine = Engine()
        task = Task(id='task-1', priority='LOW', requirements='test-requirement')
        engine.ingest_task(task)
        self.assertIsNotNone(engine.find_agent_for_task(task))
