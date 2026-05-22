class TaskException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self) -> str:
        return f'Task Exception: {self.message}'

class AgentException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self) -> str:
        return f'Agent Exception: {self.message}'
