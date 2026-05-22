import argparse
from packages.core.engine import Engine
from packages.core.types import Task


def main():
    parser = argparse.ArgumentParser(description='Multi-Agent Orchestration Framework')
    parser.add_argument('--task-id', help='Task ID', required=True)
    parser.add_argument('--priority', help='Task Priority', choices=['LOW', 'MEDIUM', 'HIGH'], required=True)
    parser.add_argument('--requirements', help='Task Requirements', required=True)
    args = parser.parse_args()
    
    task = Task(id=args.task_id, priority=args.priority, requirements=args.requirements)
    engine = Engine()
    engine.ingest_task(task)
    
if __name__ == '__main__':
    main()