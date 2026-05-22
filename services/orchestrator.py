from packages.core.engine import Engine
from packages.core.exceptions import TaskException


class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine
    
    def execute(self, task_id: str):
        try:
            self.engine.execute_task(task_id)
        except TaskException as e:
            print(f'Error executing task {task_id}: {e}')
