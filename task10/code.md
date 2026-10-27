# Comprehensive Smart Campus Management Simulation

## Problem statement

Develop a menu-driven Python program to simulate key campus operations. The program should manage student records, attendance, marks, event registrations, and resource allocation. It should also produce summary reports.

Use conditionals and loops to control the menu and validate choices; strings and lists to store data; nested lists for student records; and tuples with tuple unpacking for campus resources.

## Algorithm

1. Initialize empty lists for student records, events, and registrations. Store campus resources as tuples.
2. Display the main menu.
3. Read the user’s choice.
4. Use conditional statements to run the selected operation:
   - Add a student record.
   - Record attendance for a student.
   - Enter or update a student’s marks.
   - Register a student for an event.
   - Allocate a resource.
   - Display a summary report.
5. Use loops to find records, validate input, and display lists.
6. Repeat the menu until the user selects Exit.
7. Print a closing message.

## Flowchart
flowchart TD
    A([Start]) --> B[Initialize students, events, registrations, resources, and allocations]
    B --> C[Display menu]
    C --> D[/Read menu choice/]
    D --> E{Choice}

    E -->|1| F[Add student record]
    E -->|2| G[Record attendance]
    E -->|3| H[Enter or update marks]
    E -->|4| I[Register student for event]
    E -->|5| J[Allocate campus resource]
    E -->|6| K[Display summary report]
    E -->|7| L([Exit])
    E -->|Other| M[Display invalid choice message]

    F --> C
    G --> C
    H --> C
    I --> C
    J --> C
    K --> C
    M --> C
 
        



## Sample input

The following inputs show one possible session. Each line corresponds to a prompt in the program.

```text
1
ST101
Asha
2
ST101
3
ST101
Mathematics
92
4
ST101
Tech Fest
5
ST101
Projector
1
6
7
```

## Sample output

```text
===== SMART CAMPUS MANAGEMENT =====
1. Add student
2. Record attendance
3. Enter or update marks
4. Register for an event
5. Allocate a resource
6. Show summary report
7. Exit
Enter your choice (1-7): 1
Enter student ID: ST101
Enter student name: Asha
Student Asha added successfully.

===== SMART CAMPUS MANAGEMENT =====
...
Enter your choice (1-7): 2
Enter student ID: ST101
Attendance recorded for Asha.
Total attendance days: 1

===== SMART CAMPUS MANAGEMENT =====
...
Enter your choice (1-7): 3
Enter student ID: ST101
Enter subject name: Mathematics
Enter marks (0-100): 92
Marks recorded for Mathematics.

===== SMART CAMPUS MANAGEMENT =====
...
Enter your choice (1-7): 4
Enter student ID: ST101

Available events:
1. Tech Fest
2. Sports Meet
3. Cultural Night
Enter event name: Tech Fest
Asha registered for Tech Fest.

===== SMART CAMPUS MANAGEMENT =====
...
Enter your choice (1-7): 5
Enter student ID: ST101

Available resources:
1. Projector — 5 available
2. Laboratory — 3 available
3. Seminar Hall — 2 available
Enter resource name: Projector
Enter quantity to allocate: 1
1 unit(s) of Projector allocated to Asha.

===== SMART CAMPUS MANAGEMENT =====
...
Enter your choice (1-7): 6

========== CAMPUS SUMMARY ==========
Total students: 1
Total events: 3
Total event registrations: 1
Total resource allocations: 1

--- Student Records ---

ID: ST101 | Name: Asha
Attendance days: 1
Marks:
  Mathematics: 92

--- Event Registrations ---
Asha (ST101) — Tech Fest

--- Resource Allocations ---
Projector: 1 unit(s) for Asha
====================================

===== SMART CAMPUS MANAGEMENT =====
...
Enter your choice (1-7): 7
Thank you for using Smart Campus Management.
```

## Mermaid flowchart code

```mermaid
flowchart TD
    A([Start]) --> B[Initialize students, events, registrations, resources, and allocations]
    B --> C[Display menu]
    C --> D[/Read menu choice/]
    D --> E{Choice}

    E -->|1| F[Add student record]
    E -->|2| G[Record attendance]
    E -->|3| H[Enter or update marks]
    E -->|4| I[Register student for event]
    E -->|5| J[Allocate campus resource]
    E -->|6| K[Display summary report]
    E -->|7| L([Exit])
    E -->|Other| M[Display invalid choice message]

    F --> C
    G --> C
    H --> C
    I --> C
    J --> C
    K --> C
    M --> C
```
