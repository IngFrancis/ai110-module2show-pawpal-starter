from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    title: str
    duration: int
    priority: int
    time: str
    completed: bool = False

    def mark_complete(self) -> None:
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass


class Owner:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass

    def list_pets(self) -> List[Pet]:
        pass


class Scheduler:
    def __init__(self, available_time: int) -> None:
        self.available_time = available_time
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        pass

    def sort_tasks_by_priority(self) -> List[Task]:
        pass

    def generate_schedule(self) -> List[Task]:
        pass