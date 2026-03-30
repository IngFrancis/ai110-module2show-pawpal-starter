from pawpal_system import Owner, Pet, Task, Scheduler

# 1️⃣ Create Owner and Pets
owner = Owner("Alice")
pet1 = Pet("Buddy", "Dog", 3)
pet2 = Pet("Mittens", "Cat", 2)

owner.add_pet(pet1)
owner.add_pet(pet2)

# 2️⃣ Add Tasks (including a recurring and conflicting task)
task1 = Task("Walk Buddy", 30, 3, "08:00", frequency="Daily")
task2 = Task("Feed Mittens", 10, 5, "07:30", frequency="Daily")
task3 = Task("Groom Buddy", 20, 2, "08:00")  # Intentional conflict

pet1.add_task(task1)
pet1.add_task(task3)
pet2.add_task(task2)

# 3️⃣ Scheduler
scheduler = Scheduler(available_time=60)
for task in owner.get_all_tasks():
    scheduler.add_task(task)

# 4️⃣ Generate and print schedule
schedule = scheduler.generate_schedule()
print("Today's Schedule:")
for t in schedule:
    print(f"- {t.title} ({t.duration} mins) [Priority: {t.priority}]")

# 5️⃣ Detect conflicts
conflicts = scheduler.detect_conflicts()
if conflicts:
    print("\n⚠️ Conflicts detected:")
    for c in conflicts:
        print(c)

# 6️⃣ Mark a task complete and create next recurring task
new_task = task1.mark_complete()
if new_task:
    print(f"\nRecurring Task Created: {new_task.title} at {new_task.time}")