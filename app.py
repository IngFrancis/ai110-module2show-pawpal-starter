import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+.

This app lets you manage your pets and their tasks, and generates a daily schedule based on priorities, available time, and smart conflict detection.
"""
)

# -----------------------
# Step 0: Initialize Owner
# -----------------------
owner_name = st.text_input("Owner name", value="Jordan")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_name if owner_name else "Jordan")

owner = st.session_state.owner

# -----------------------
# Step 1: Add Pets
# -----------------------
st.subheader("Add a Pet")

with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name", value="Mochi")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    age = st.number_input("Age", min_value=0, max_value=50, value=2)
    submit_pet = st.form_submit_button("Add Pet")

if submit_pet:
    new_pet = Pet(pet_name, species, age)
    owner.add_pet(new_pet)
    st.success(f"{pet_name} added!")

# -----------------------
# Step 2: Add Tasks
# -----------------------
st.subheader("Add a Task")

pets_list = owner.list_pets()
pet_names = [pet.name for pet in pets_list]

if pet_names:
    selected_pet_name = st.selectbox("Select Pet", pet_names)

    with st.form("add_task_form"):
        task_title = st.text_input("Task title", value="Morning walk")
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
        priority = st.number_input("Priority (1=low, 5=high)", min_value=1, max_value=5, value=3)
        task_time = st.text_input("Time (e.g., 08:00)", value="08:00")
        frequency = st.selectbox("Frequency", ["None", "Daily", "Weekly"])
        submit_task = st.form_submit_button("Add Task")

    if submit_task:
        pet = next((p for p in pets_list if p.name == selected_pet_name), None)
        if pet:
            new_task = Task(task_title, duration, priority, task_time, frequency=frequency if frequency != "None" else None)
            pet.add_task(new_task)
            st.success(f"Task '{task_title}' added to {selected_pet_name}")
else:
    st.info("Add a pet first to assign tasks.")

# -----------------------
# Step 3: Display Current Tasks
# -----------------------
st.subheader("Current Tasks")
all_tasks = owner.get_all_tasks()

if all_tasks:
    task_data = [
        {"Pet": next(pet.name for pet in pets_list if task in pet.tasks),
         "Title": task.title,
         "Duration": task.duration,
         "Priority": task.priority,
         "Time": task.time,
         "Completed": task.completed,
         "Frequency": task.frequency if hasattr(task, "frequency") else "None"}
        for task in all_tasks
    ]
    st.table(task_data)
else:
    st.info("No tasks yet. Add one above.")

# -----------------------
# Step 4: Generate Schedule
# -----------------------
st.subheader("Today's Schedule")
available_time = st.number_input("Available time (minutes)", min_value=10, max_value=480, value=120)

if st.button("Generate Schedule"):
    scheduler = Scheduler(available_time=available_time)
    for task in all_tasks:
        scheduler.add_task(task)

    # Sort tasks
    sorted_tasks = scheduler.sort_by_time()
    schedule = scheduler.generate_schedule()

    # Display sorted schedule
    if schedule:
        st.markdown("### 🗓 Schedule (sorted by time)")
        for task in schedule:
            if task.completed:
                st.success(f"- {task.title} ({task.duration} mins) [Priority: {task.priority}]")
            else:
                st.write(f"- {task.title} ({task.duration} mins) [Priority: {task.priority}]")
    else:
        st.info("No tasks fit in the available time or no tasks added yet.")

    # Detect conflicts
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        st.markdown("### ⚠️ Conflicts Detected")
        for c in conflicts:
            st.warning(c)