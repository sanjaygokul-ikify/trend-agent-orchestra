import logging

logging.basicConfig(level=logging.INFO)

def setup_logging(level: str = 'INFO'):
    logging.basicConfig(level=level)
