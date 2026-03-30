from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    """Represents a single pet care activity (task) for a pet.

    Attributes:
        title (str): The name or description of the task.
        duration (int): Estimated duration of the task in minutes.
        priority (int): Priority level of the task (higher = more important).
        time (str): Suggested time for the task (e.g., "08:00").
        completed (bool): Whether the task has been completed.
    """
    title: str
    duration: int
    priority: int
    time: str
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

@dataclass
class Pet:
    """Stores pet details and manages a list of tasks.

    Attributes:
        name (str): Pet's name.
        species (str): Pet's species (e.g., "Dog", "Cat").
        age (int): Pet's age in years.
        tasks (List[Task]): List of tasks associated with this pet.
    """
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list.

        Args:
            task (Task): The task to add.
        """
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet.

        Returns:
            List[Task]: The list of tasks.
        """
        return self.tasks

class Owner:
    """Manages multiple pets and provides access to all their tasks.

    Attributes:
        name (str): Owner's name.
        pets (List[Pet]): List of pets owned.
    """
    def __init__(self, name: str) -> None:
        """Initialize an Owner with a name and an empty pet list."""
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list.

        Args:
            pet (Pet): The pet to add.
        """
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's list if present.

        Args:
            pet (Pet): The pet to remove.
        """
        if pet in self.pets:
            self.pets.remove(pet)

    def list_pets(self) -> List[Pet]:
        """Return all pets owned by this owner.

        Returns:
            List[Pet]: The list of pets.
        """
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from all pets owned.

        Returns:
            List[Task]: Flattened list of all tasks across pets.
        """
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks

class Scheduler:
    """Organizes and manages tasks across pets to fit within available time.

    Attributes:
        available_time (int): Total available time in minutes for tasks.
        tasks (List[Task]): Tasks added to the scheduler.
    """
    def __init__(self, available_time: int) -> None:
        """Initialize the Scheduler with a time budget."""
        self.available_time = available_time
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the scheduler.

        Args:
            task (Task): Task to add.
        """
        self.tasks.append(task)

    def sort_tasks_by_priority(self) -> List[Task]:
        """Return tasks sorted by descending priority.

        Returns:
            List[Task]: Tasks sorted from highest to lowest priority.
        """
        return sorted(self.tasks, key=lambda t: t.priority, reverse=True)

    def generate_schedule(self) -> List[Task]:
        """Generate a schedule fitting tasks into available_time by priority.

        Returns:
            List[Task]: Tasks selected for the schedule based on priority and time.
        """
        sorted_tasks = self.sort_tasks_by_priority()
        scheduled = []
        time_remaining = self.available_time

        for task in sorted_tasks:
            if task.duration <= time_remaining:
                scheduled.append(task)
                time_remaining -= task.duration

        return scheduled