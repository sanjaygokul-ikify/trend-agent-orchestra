import logging
from typing import List, Dict
from .types import Task, Agent
from .exceptions import TaskException


class Engine:
    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.tasks = {}
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def ingest_task(self, task: Task):
        self.logger.info(f'Ingesting task {task.id} with priority {task.priority}')
        self.tasks[task.id] = task
        self.allocate_task(task)

    def allocate_task(self, task: Task):
        agent = self.find_agent_for_task(task)
        if agent:
            self.logger.info(f'Allocating task {task.id} to agent {agent.id}')
            agent.tasks.append(task)
        else:
            self.logger.warning(f'No suitable agent found for task {task.id}')
            raise TaskException(f'Task {task.id} cannot be allocated')

    def find_agent_for_task(self, task: Task) -> Agent:
        for agent in self.agents:
            if hasattr(agent.capabilities, 'contains') and callable(agent.capabilities.contains) and agent.capabilities.contains(task.requirements):
                return agent
        return None

    def execute_task(self, task: Task):
        agent = self.find_agent_for_task(task)
        if agent:
            self.logger.info(f'Executing task {task.id} on agent {agent.id}')
            try:
                task.status = 'executing'
                agent.execute_task(task)
                task.status = 'completed'
            except Exception as e:
                task.status = 'failed'
                self.logger.error(f'Task {task.id} failed with error {e}')
                raise TaskException(f'Task {task.id} failed with error {e}')
        else:
            self.logger.warning(f'No suitable agent found for task {task.id}')
            raise TaskException(f'Task {task.id} cannot be executed')

    def cancel_task(self, task: Task):
        self.logger.info(f'Cancelling task {task.id}')
        task.status = 'cancelled'
        agent = self.find_agent_for_task(task)
        if agent:
            agent.cancel_task(task)
        else:
            self.logger.warning(f'No suitable agent found for task {task.id}')
            raise TaskException(f'Task {task.id} cannot be cancelled')

    def update_task_status(self, task: Task):
        self.logger.info(f'Updating task {task.id} status to {task.status}')
        self.tasks[task.id].status = task.status


class Agent:
    def __init__(self, id: str, capabilities: object):
        self.id = id
        self.capabilities = capabilities
        self.tasks = []

    def execute_task(self, task: Task):
        self.logger = logging.getLogger(__name__)
        self.logger.info(f'Executing task {task.id} on agent {self.id}')
        try:
            task.status = 'executing'
            # Simulate task execution
            import time
            time.sleep(2)
            task.status = 'completed'
        except Exception as e:
            task.status = 'failed'
            self.logger.error(f'Task {task.id} failed with error {e}')
            raise TaskException(f'Task {task.id} failed with error {e}')

    def cancel_task(self, task: Task):
        self.logger = logging.getLogger(__name__)
        self.logger.info(f'Cancelling task {task.id} on agent {self.id}')
        task.status = 'cancelled'
