# Comprehensive Smart Campus Management Simulation

# Each student is stored as a nested list:
# [student_id, name, attendance_count, marks]
students = []

# Events are stored as strings.
events = ["Tech Fest", "Sports Meet", "Cultural Night"]

# Registrations are stored as [student_id, event_name] pairs.
registrations = []

# Resources are stored as tuples: (resource_name, total_available)
resources = [
    ("Projector", 5),
    ("Laboratory", 3),
    ("Seminar Hall", 2),
]

# Allocations are stored as [student_id, resource_name, quantity].
allocations = []


def find_student(student_id):
    """Return a student record if the ID exists; otherwise return None."""
    for student in students:
        if student[0] == student_id:
            return student
    return None


def add_student():
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student(student_id) is not None:
        print("A student with that ID already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    # Nested list record: [ID, name, attendance, marks]
    students.append([student_id, name, 0, []])
    print(f"Student {name} added successfully.")


def record_attendance():
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    student[2] += 1
    print(f"Attendance recorded for {student[1]}.")
    print(f"Total attendance days: {student[2]}")


def enter_marks():
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    subject = input("Enter subject name: ").strip()

    if not subject:
        print("Subject name cannot be empty.")
        return

    try:
        score = float(input("Enter marks (0-100): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if score < 0 or score > 100:
        print("Marks must be between 0 and 100.")
        return

    # Store each subject and score as a nested list.
    # Update the score if the subject already exists.
    for mark in student[3]:
        if mark[0].lower() == subject.lower():
            mark[1] = score
            print(f"Marks updated for {subject}.")
            return

    student[3].append([subject, score])
    print(f"Marks recorded for {subject}.")


def register_for_event():
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found. Add the student first.")
        return

    print("\nAvailable events:")
    for number, event in enumerate(events, start=1):
        print(f"{number}. {event}")

    event_name = input("Enter event name: ").strip()

    if event_name not in events:
        print("That event is not available.")
        return

    registration = [student_id, event_name]

    if registration in registrations:
        print("This student is already registered for that event.")
        return

    registrations.append(registration)
    print(f"{student[1]} registered for {event_name}.")


def allocate_resource():
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nAvailable resources:")
    for index, (resource_name, total) in enumerate(resources, start=1):
        used = 0
        for allocation in allocations:
            if allocation[1] == resource_name:
                used += allocation[2]

        print(f"{index}. {resource_name} — {total - used} available")

    resource_name = input("Enter resource name: ").strip()

    # Tuple unpacking is used to find the selected resource.
    resource_found = False
    total_available = 0

    for name, total in resources:
        if name.lower() == resource_name.lower():
            resource_name = name
            total_available = total
            resource_found = True
            break

    if not resource_found:
        print("Resource not found.")
        return

    try:
        quantity = int(input("Enter quantity to allocate: "))
    except ValueError:
        print("Quantity must be a whole number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    already_allocated = 0
    for allocation in allocations:
        if allocation[1] == resource_name:
            already_allocated += allocation[2]

    if already_allocated + quantity > total_available:
        print("Not enough units of that resource are available.")
        return

    allocations.append([student_id, resource_name, quantity])
    print(f"{quantity} unit(s) of {resource_name} allocated to {student[1]}.")


def show_summary():
    print("\n========== CAMPUS SUMMARY ==========")
    print(f"Total students: {len(students)}")
    print(f"Total events: {len(events)}")
    print(f"Total event registrations: {len(registrations)}")
    print(f"Total resource allocations: {len(allocations)}")

    print("\n--- Student Records ---")
    if not students:
        print("No student records available.")
    else:
        for student_id, name, attendance, marks in students:
            print(f"\nID: {student_id} | Name: {name}")
            print(f"Attendance days: {attendance}")

            if marks:
                print("Marks:")
                for subject, score in marks:
                    print(f"  {subject}: {score:g}")
            else:
                print("Marks: No marks entered")

    print("\n--- Event Registrations ---")
    if not registrations:
        print("No event registrations.")
    else:
        for student_id, event_name in registrations:
            student = find_student(student_id)
            student_name = student[1] if student else "Unknown student"
            print(f"{student_name} ({student_id}) — {event_name}")

    print("\n--- Resource Allocations ---")
    if not allocations:
        print("No resources allocated.")
    else:
        for student_id, resource_name, quantity in allocations:
            student = find_student(student_id)
            student_name = student[1] if student else "Unknown student"
            print(f"{resource_name}: {quantity} unit(s) for {student_name}")

    print("====================================")


def display_menu():
    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Add student")
    print("2. Record attendance")
    print("3. Enter or update marks")
    print("4. Register for an event")
    print("5. Allocate a resource")
    print("6. Show summary report")
    print("7. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            record_attendance()
        elif choice == "3":
            enter_marks()
        elif choice == "4":
            register_for_event()
        elif choice == "5":
            allocate_resource()
        elif choice == "6":
            show_summary()
        elif choice == "7":
            print("Thank you for using Smart Campus Management.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
