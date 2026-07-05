import logging
from typing import List, Dict
from .types import Task, Agent
from .exceptions import TaskException


class Engine:
    def __init__(self, agents: List[Agent] = None):
        self.agents = agents if agents is not None else []
        self.tasks = {}
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def ingest_task(self, task: Task):
        self.logger.info(f'Ingesting task {task.id} with priority {task.priority}')
        self.tasks[task.id] = task
        try:
            self.allocate_task(task)
        except Exception as e:
            self.logger.error(f'Error allocating task {task.id}: {e}')
            raise TaskException(f'Task {task.id} cannot be allocated') from e

    def allocate_task(self, task: Task):
        agent = self.find_agent_for_task(task)
        if agent:
            self.logger.info(f'Allocating task {task.id} to agent {agent.id}')
            agent.tasks.append(task)
        else:
            self.logger.warning(f'No suitable agent found for task {task.id}')
            raise TaskException(f'Task {task.id} cannot be allocated')

    def execute_task(self, task: Task):
        agent = self.find_agent_for_task(task)
        if agent:
            try:
                self.logger.info(f'Executing task {task.id} on agent {agent.id}')
                task.status = 'executing'
                agent.execute_task(task)
                task.status = 'completed'
            except Exception as e:
                task.status = 'failed'
                self.logger.error(f'Task {task.id} failed with error {e}')
                raise TaskException(f'Task {task.id} failed with error {e}') from e
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

    def find_agent_for_task(self, task: Task) -> Agent:
        for agent in self.agents:
            if hasattr(agent.capabilities, 'contains') and callable(agent.capabilities.contains) and agent.capabilities.contains(task.requirements):
                return agent
        return None

    def create_task(self, id: str, priority: str, requirements: str, status: str = 'pending') -> Task:
        return Task(id, priority, requirements, status)

    def run(self):
        for task in self.tasks.values():
            try:
                self.execute_task(task)
            except TaskException as e:
                self.logger.error(f'Task {task.id} failed with error {e}')

    def add_agent(self, agent: Agent):
        self.agents.append(agent)
