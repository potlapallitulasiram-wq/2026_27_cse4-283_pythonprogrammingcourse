# Multi-Criteria Library Resource Distribution

## Problem statement

A library system has several branches and a limited number of copies of each book. For each branch and book, the system receives:

- the number of copies currently available,
- the borrowing demand,
- a priority score,
- the number of copies to allocate.

Allocate copies according to the supplied priority rules: branches with higher priority receive copies first. Within each priority level, branches with greater unmet demand are considered first. Do not allocate more copies than are available or more than a branch needs.

Report each branch’s allocation and unmet demand. If priority and demand are tied, use the branch name alphabetically.

## Algorithm

1. Read the available copy count and the branch records.
2. For each branch, calculate its initial unmet demand: `max(0, demand - current_stock)`.
3. Sort branches by:
   - priority, highest first;
   - initial unmet demand, highest first;
   - branch name, alphabetical order.
4. For each branch in that order:
   - calculate copies needed after current stock;
   - allocate the smaller of the remaining copies and copies needed;
   - update the remaining copy count.
5. Calculate final unmet demand: `max(0, demand - current_stock - allocation)`.
6. Display each branch’s allocation and unmet demand, plus any copies left over.

## Flowchart

    flowchart TD
    A([Start]) --> B[/Read book title, available copies, and branch records/]
    B --> C[Calculate initial unmet demand for each branch]
    C --> D[Sort by priority descending, unmet demand descending, branch name ascending]
    D --> E[Set remaining copies to available copies]
    E --> F{More branches to process?}
    F -- No --> K[/Display allocation, unmet demand, and leftover copies/]
    K --> L([End])
    F -- Yes --> G[Calculate copies needed after current stock]
    G --> H[Allocate the smaller of needed copies and remaining copies]
    H --> I[Update remaining copies and calculate final unmet demand]
    I --> F

## Sample input

For this program, enter the following responses:

```text
Book title: Data Structures
Copies available for distribution: 12
Number of branches: 3

Branch 1
Name: Central
Current stock: 2
Borrowing demand: 10
Priority (higher number = higher priority): 3

Branch 2
Name: East
Current stock: 1
Borrowing demand: 8
Priority (higher number = higher priority): 2

Branch 3
Name: West
Current stock: 0
Borrowing demand: 6
Priority (higher number = higher priority): 2
```

## Sample output

```text
Distribution for: Data Structures
----------------------------------------------------------------------
Branch            Priority     Stock    Demand   Allocated     Unmet
----------------------------------------------------------------------
Central                   3         2        10           8         0
East                      2         1         8           4         3
West                      2         0         6           0         6
----------------------------------------------------------------------
Copies left undistributed: 0
```

## Mermaid flowchart code

Paste this into a Mermaid-compatible editor to render the flowchart:

```mermaid
flowchart TD
    A([Start]) --> B[/Read book title, available copies, and branch records/]
    B --> C[Calculate initial unmet demand for each branch]
    C --> D[Sort by priority descending, unmet demand descending, branch name ascending]
    D --> E[Set remaining copies to available copies]
    E --> F{More branches to process?}
    F -- No --> K[/Display allocation, unmet demand, and leftover copies/]
    K --> L([End])
    F -- Yes --> G[Calculate copies needed after current stock]
    G --> H[Allocate the smaller of needed copies and remaining copies]
    H --> I[Update remaining copies and calculate final unmet demand]
    I --> F
```
