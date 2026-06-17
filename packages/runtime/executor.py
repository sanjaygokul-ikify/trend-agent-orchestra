import logging
from typing import List
from . import Executor
from packaging import version
from packages.core.engine import Engine

class Executor:
    def __init__(self, agents: List[Agent]):
        self.engine = Engine(agents)

    def execute_tasks(self, tasks: List[Task]):
        logging.basicConfig(level=logging.INFO)
        for task in tasks:
            try:
                self.engine.ingest_task(task)
            except Exception as e:
                logging.error(f'Task {task.id} cannot be allocated: {e}')
            finally:
                self.engine.update_task_status(task)

    def run(self):
        for task in self.engine.tasks.values():
            try:
                self.engine.execute_task(task)
            except TaskException as e:
                logging.error(f'Task {task.id} failed with error {e}')