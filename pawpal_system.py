from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime, timedelta


@dataclass
class Task:
    """Represents a single pet care activity."""
    title: str
    duration: int  # in minutes
    priority: int
    time: str  # "HH:MM" format
    pet_name: Optional[str] = None  # optional: associated pet
    completed: bool = False
    frequency: Optional[str] = None  # "daily" or "weekly"

    def mark_complete(self) -> Optional['Task']:
        """Mark the task as completed. If recurring, return a new Task for the next occurrence."""
        self.completed = True
        if self.frequency:
            new_time = datetime.strptime(self.time, "%H:%M")
            if self.frequency.lower() == "daily":
                new_time += timedelta(days=1)
            elif self.frequency.lower() == "weekly":
                new_time += timedelta(weeks=1)
            return Task(
                title=self.title,
                duration=self.duration,
                priority=self.priority,
                time=new_time.strftime("%H:%M"),
                pet_name=self.pet_name,
                frequency=self.frequency
            )
        return None


@dataclass
class Pet:
    """Stores pet details and a list of tasks."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        task.pet_name = self.name
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


class Owner:
    """Manages multiple pets and their tasks."""
    def __init__(self, name: str) -> None:
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's list."""
        if pet in self.pets:
            self.pets.remove(pet)

    def list_pets(self) -> List[Pet]:
        """Return all pets for the owner."""
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from all pets."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks


class Scheduler:
    """Organizes and manages tasks across pets."""
    def __init__(self, available_time: int) -> None:
        self.available_time = available_time
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the scheduler."""
        self.tasks.append(task)

    def sort_by_priority(self) -> List[Task]:
        """Return tasks sorted by priority, descending."""
        return sorted(self.tasks, key=lambda t: t.priority, reverse=True)

    def sort_by_time(self) -> List[Task]:
        """Return tasks sorted by time (HH:MM format)."""
        return sorted(self.tasks, key=lambda t: t.time)

    def filter_tasks(
        self, completed: Optional[bool] = None, pet_name: Optional[str] = None
    ) -> List[Task]:
        """Return tasks filtered by completion status or pet name."""
        filtered = self.tasks
        if completed is not None:
            filtered = [t for t in filtered if t.completed == completed]
        if pet_name is not None:
            filtered = [t for t in filtered if t.pet_name == pet_name]
        return filtered

    def detect_conflicts(self) -> List[str]:
        """Return warnings if two tasks share the same time."""
        warnings = []
        seen_times = {}
        for task in self.tasks:
            key = (task.time, task.pet_name)
            if key in seen_times:
                warnings.append(
                    f"Conflict: '{task.title}' overlaps with '{seen_times[key]}' at {task.time} for pet {task.pet_name}"
                )
            else:
                seen_times[key] = task.title
        return warnings

    def generate_schedule(self) -> List[Task]:
        """
        Generate a schedule that fits within available_time.
        Tasks are chosen by priority until time runs out.
        """
        sorted_tasks = self.sort_by_priority()
        scheduled = []
        time_remaining = self.available_time

        for task in sorted_tasks:
            if task.duration <= time_remaining:
                scheduled.append(task)
                time_remaining -= task.duration

        return scheduled