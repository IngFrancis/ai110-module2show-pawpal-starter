# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Smarter Scheduling

PawPal+ now includes algorithmic intelligence:

- **Sort Tasks by Time** – Ensures tasks appear in chronological order.
- **Filter Tasks** – Easily filter by completion status or pet name.
- **Recurring Tasks** – Daily/weekly tasks automatically generate the next occurrence.
- **Conflict Detection** – Warns if two tasks are scheduled at the same time.

## Testing PawPal+

We have implemented an automated test suite for PawPal+ to verify core system behaviors:

- **Sorting Correctness:** Tasks are sorted chronologically by time.
- **Recurrence Logic:** Daily tasks generate a new task when completed.
- **Conflict Detection:** Scheduler identifies tasks scheduled at the same time.
- **Filtering:** Ability to filter tasks by completion status.
- **Edge Cases:** Scheduler handles situations where a pet has no tasks.

**Run tests with:**

```bash
python -m pytest


## 📸 System Architecture

<a href="/course_images/ai110/uml_final.png" target="_blank">
  <img src='/course_images/ai110/uml_final.png' title='PawPal+ UML Diagram' width='600' alt='PawPal+ UML Diagram' class='center-block' />
</a>

✅ Clicking the image opens the full-size UML diagram.
```

## ✨ Features

PawPal+ includes several intelligent features to help pet owners manage their pets efficiently:

- **Sort Tasks by Time:** Tasks are displayed in chronological order automatically.
- **Filter Tasks:** Quickly filter tasks by completion status or pet name.
- **Recurring Tasks:** Daily tasks automatically generate the next occurrence when completed.
- **Conflict Detection:** Warns if two tasks are scheduled at the same time.
- **Daily Schedule Generation:** Generates a schedule based on task priorities and available time.
- **Task Management:** Add, edit, and track tasks for multiple pets.
- **Edge Case Handling:** Handles pets with no tasks and ensures smooth UI experience.

## 📸 Demo

<a href="/course_images/ai110/pawpal_screenshot.png" target="_blank">
  <img src='/course_images/ai110/pawpal_screenshot.png' title='PawPal+ App' width='600' alt='PawPal+ App' class='center-block' />
</a>

✅ Clicking the image opens the full-size app screenshot.
