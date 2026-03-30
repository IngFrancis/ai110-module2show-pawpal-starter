from pawpal_system import Owner, Pet, Task, Scheduler

# 1️⃣ Create Owner and Pets
owner = Owner("Alice")
pet1 = Pet("Buddy", "Dog", 3)
pet2 = Pet("Mittens", "Cat", 2)

owner.add_pet(pet1)
owner.add_pet(pet2)

# 2️⃣ Add Tasks
task1 = Task("Walk Buddy", 30, 3, "08:00")
task2 = Task("Feed Mittens", 10, 5, "07:30")
task3 = Task("Groom Buddy", 20, 2, "09:00")

pet1.add_task(task1)
pet1.add_task(task3)
pet2.add_task(task2)

# 3️⃣ Scheduler
scheduler = Scheduler(available_time=40)
for task in owner.get_all_tasks():
    scheduler.add_task(task)

# 4️⃣ Generate and print schedule
schedule = scheduler.generate_schedule()
print("Today's Schedule:")
for t in schedule:
    print(f"- {t.title} ({t.duration} mins) [Priority: {t.priority}]")