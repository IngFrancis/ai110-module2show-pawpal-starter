from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime

# 1️⃣ Create Owner and Pets
owner = Owner("Alice")
pet1 = Pet("Buddy", "Dog", 3)
pet2 = Pet("Mittens", "Cat", 2)

owner.add_pet(pet1)
owner.add_pet(pet2)

# 2️⃣ Add Tasks (some intentionally out of order and recurring)
task1 = Task("Walk Buddy", 30, 3, "08:00", pet_name="Buddy", frequency="daily")
task2 = Task("Feed Mittens", 10, 5, "07:30", pet_name="Mittens")
task3 = Task("Groom Buddy", 20, 2, "09:00", pet_name="Buddy")
task4 = Task("Vet Call Mittens", 15, 4, "08:00", pet_name="Mittens")  # Conflict on time

pet1.add_task(task1)
pet1.add_task(task3)
pet2.add_task(task2)
pet2.add_task(task4)

# 3️⃣ Scheduler
scheduler = Scheduler(available_time=60)
for task in owner.get_all_tasks():
    scheduler.add_task(task)

# 4️⃣ Detect conflicts
conflicts = scheduler.detect_conflicts()
if conflicts:
    print("⚠️ Conflicts detected:")
    for c in conflicts:
        print(c)
else:
    print("No conflicts detected.")

# 5️⃣ Generate schedule
schedule = scheduler.generate_schedule()
print("\nToday's Schedule (by priority):")
for t in schedule:
    print(f"- {t.title} ({t.duration} mins) [Priority: {t.priority}] at {t.time} for {t.pet_name}")

# 6️⃣ Sort by time
time_sorted = scheduler.sort_by_time()
print("\nSchedule sorted by time:")
for t in time_sorted:
    print(f"- {t.title} at {t.time} for {t.pet_name}")

# 7️⃣ Filter tasks
completed_tasks = scheduler.filter_tasks(completed=True)
pending_tasks = scheduler.filter_tasks(completed=False)
print(f"\nCompleted tasks: {len(completed_tasks)}")
print(f"Pending tasks: {len(pending_tasks)}")

# 8️⃣ Mark a task as complete (demonstrating recurring task creation)
print("\nMarking 'Walk Buddy' as complete...")
new_task = task1.mark_complete()
if new_task:
    pet1.add_task(new_task)
    scheduler.add_task(new_task)
    print(f"New recurring task created for {new_task.time}")

# 9️⃣ Show updated schedule
updated_schedule = scheduler.generate_schedule()
print("\nUpdated Schedule after completing a task:")
for t in updated_schedule:
    print(f"- {t.title} ({t.duration} mins) [Priority: {t.priority}] at {t.time} for {t.pet_name}")