import pytest
from pawpal_system import Pet, Task

def test_task_completion():
    """Verify that calling mark_complete() changes the task's status."""
    task = Task("Feed", 10, 5, "07:00")
    assert not task.completed       # Initially False
    task.mark_complete()
    assert task.completed           # Should now be True

def test_pet_add_task():
    """Verify that adding a task to a Pet increases the task count."""
    pet = Pet("Buddy", "Dog", 3)
    task = Task("Walk", 30, 3, "08:00")
    assert len(pet.tasks) == 0      # Initially empty
    pet.add_task(task)
    assert len(pet.tasks) == 1      # Should now have 1 task