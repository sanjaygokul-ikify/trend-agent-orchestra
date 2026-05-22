from typing import List, Dict

class TrendAgentError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class TrendAgentWarning(Warning):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

import logging

class TrendAgent:
    def __init__(self, config: Dict[str, str]):
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