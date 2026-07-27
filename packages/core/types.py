from typing import List, Dict

class TrendAgentError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class TrendAgentWarning(Warning):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class TrendAgent:
    def __init__(self, config: Dict[str, str]) -> None:
        self.config = config
        self.logger = logging.getLogger(__name__)
    
    def start(self) -> None:
        self.logger.info('Starting trend agent')
        # implement trend agent start logic here
        self.logger.info('Trend agent started')

    def stop(self) -> None:
        self.logger.info('Stopping trend agent')
        # implement trend agent stop logic here
        self.logger.info('Trend agent stopped')

class Task:
    def __init__(self, id: str, priority: str, requirements: str, status: str = 'pending'):
        self.id = id
        self.priority = priority
        self.requirements = requirements
        self.status = status


class Agent:
    def __init__(self, id: str, capabilities: object, execute_task: callable = None, cancel_task: callable = None) -> None:
        self.id = id
        self.capabilities = capabilities
        self.tasks: List[Task] = []
        self.execute_task = execute_task
        self.cancel_task = cancel_task
