## Problem statement

Given an answer key and the answers submitted by several students, compare each student’s answer with the key. For every question, calculate the percentage of students who answered correctly, count how many missed it, identify the question or questions missed most often, and classify performance.

**Assumptions:** Each answer is one token. A dash (`-`) represents a blank answer and counts as incorrect. Performance is **High** at 80% or above, **Moderate** from 50% to below 80%, and **Low** below 50%.

## Algorithm

1. Read the number of students and questions.
2. Read the answer key and each student’s answers.
3. For each question, count answers that match the key.
4. Calculate the success rate and missed count for each question.
5. Classify each question using the stated thresholds.
6. Find the largest missed count and report every question with that count.

## Flowchart
flowchart TD
    A([Start]) --> B[/Input number of students and questions/]
    B --> C[/Input answer key/]
    C --> D[/Input answers for each student/]
    D --> E[Initialize correct answer counts]
    E --> F{More student answers?}
    F -- Yes --> G[Compare answers with key]
    G --> H[Update correct counts]
    H --> F
    F -- No --> I[Calculate success rate and missed count per question]
    I --> J[Assign performance classification]
    J --> K[Find highest missed count and matching questions]
    K --> L[/Display results/]
    L --> M([End])

## Sample input

```text
Enter number of students and questions: 4 3
Enter the answer key: A B C
Enter answers for student 1: A B C
Enter answers for student 2: A C C
Enter answers for student 3: B B -
Enter answers for student 4: A A C
```

## Sample output

```text
Question-wise performance
Question | Correct | Missed | Success Rate | Classification
-----------------------------------------------------------------
Q1       | 3       | 1      |  75.00%       | Moderate
Q2       | 2       | 2      |  50.00%       | Moderate
Q3       | 3       | 1      |  75.00%       | Moderate

Most frequently missed: Q2 (2 students missed each).
```

## Mermaid flowchart code

```mermaid
flowchart TD
    A([Start]) --> B[/Input number of students and questions/]
    B --> C[/Input answer key/]
    C --> D[/Input answers for each student/]
    D --> E[Initialize correct answer counts]
    E --> F{More student answers?}
    F -- Yes --> G[Compare answers with key]
    G --> H[Update correct counts]
    H --> F
    F -- No --> I[Calculate success rate and missed count per question]
    I --> J[Assign performance classification]
    J --> K[Find highest missed count and matching questions]
    K --> L[/Display results/]
    L --> M([End])
```
