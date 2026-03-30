import pytest
from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler

# -------------------------
# Helper to convert string time to datetime
def time_to_datetime(time_str):
    return datetime.strptime(time_str, "%H:%M")

# -------------------------
# Test Sorting Correctness
def test_sort_by_time():
    scheduler = Scheduler(available_time=120)
    task1 = Task("Task A", 10, 3, "09:00")
    task2 = Task("Task B", 15, 2, "08:00")
    task3 = Task("Task C", 20, 1, "10:00")
    for t in [task1, task2, task3]:
        scheduler.add_task(t)

    sorted_tasks = scheduler.sort_by_time()
    times = [t.time for t in sorted_tasks]
    assert times == ["08:00", "09:00", "10:00"], "Tasks should be sorted chronologically"

# -------------------------
# Test Recurrence Logic
def test_daily_task_recurrence():
    pet = Pet("Buddy", "Dog", 3)
    task = Task("Walk", 30, 3, "08:00", frequency="Daily")
    pet.add_task(task)

    new_task = task.mark_complete()
    assert task.completed is True, "Original task should be marked complete"
    assert new_task is not None, "A new daily task should be created"
    assert new_task.time == task.time, "New task should have the same time"
    assert new_task.completed is False, "New task should not be completed yet"

# -------------------------
# Test Conflict Detection
def test_detect_conflicts():
    scheduler = Scheduler(available_time=120)
    task1 = Task("Task 1", 20, 3, "08:00")
    task2 = Task("Task 2", 15, 2, "08:00")  # Conflict time
    scheduler.add_task(task1)
    scheduler.add_task(task2)

    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) == 1, "Should detect one conflict"
    assert "08:00" in conflicts[0], "Conflict message should include the conflicting time"

# -------------------------
# Test Filtering Tasks by Completion
def test_filter_tasks():
    scheduler = Scheduler(available_time=60)
    task1 = Task("Task 1", 10, 3, "08:00")
    task2 = Task("Task 2", 15, 2, "09:00")
    task2.mark_complete()
    for t in [task1, task2]:
        scheduler.add_task(t)

    completed_tasks = scheduler.filter_tasks(completed=True)
    pending_tasks = scheduler.filter_tasks(completed=False)
    assert completed_tasks == [task2], "Completed filter should return only completed tasks"
    assert pending_tasks == [task1], "Pending filter should return only pending tasks"

# -------------------------
# Edge Case: No Tasks
def test_no_tasks():
    scheduler = Scheduler(available_time=60)
    assert scheduler.generate_schedule() == [], "Scheduler should return empty schedule when no tasks"