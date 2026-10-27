## Problem statement

Simulate a water tank over several intervals. For each interval, the tank receives an inflow and has an outflow. Update the water level, record any overflow or shortage, and find the first interval whose **ending** water level is at least a specified threshold.

Assume the tank starts between 0 and its capacity. Water level is capped at capacity, and cannot go below 0. Overflow and shortage are reported as amounts.

## Algorithm

1. Read the number of intervals, tank capacity, initial level, target threshold, and each interval’s inflow and outflow.
2. For each interval, calculate the proposed level: `current level + inflow - outflow`.
3. If the proposed level exceeds capacity, record the excess as overflow and set the level to capacity.
4. If the proposed level is below zero, record the deficit as shortage and set the level to zero.
5. Record the ending level. If it is at least the threshold and no earlier interval reached it, save this interval number.
6. Report the results for every interval and the first interval that reached the threshold, if any.

## Flowchart
flowchart TD
    A([Start]) --> B[/Read capacity, initial level, threshold, and interval data/]
    B --> C[Set level to initial level]
    C --> D{More intervals?}
    D -- Yes --> E[Read inflow and outflow for interval]
    E --> F[Calculate proposed level = level + inflow - outflow]
    F --> G{Proposed level greater than capacity?}
    G -- Yes --> H[Record overflow; set level to capacity]
    G -- No --> I{Proposed level below zero?}
    I -- Yes --> J[Record shortage; set level to zero]
    I -- No --> K[Set level to proposed level]
    H --> L[Record ending level]
    J --> L
    K --> L
    L --> M{Threshold reached for the first time?}
    M -- Yes --> N[Save current interval number]
    M -- No --> D
    N --> D
    D -- No --> O[/Print interval results and first threshold interval/]
    O --> P([End])




## Sample input

```text
5
100
60
80
30 20
40 10
10 35
50 10
20 70
```

## Sample output

```text
Interval | Inflow | Outflow | Ending level | Overflow | Shortage
       1 |     30 |      20 |           70 |        0 |        0
       2 |     40 |      10 |          100 |        0 |        0
       3 |     10 |      35 |           75 |        0 |        0
       4 |     50 |      10 |          100 |       15 |        0
       5 |     20 |      70 |           50 |        0 |        0

The threshold was first reached in interval 2.
```

## Mermaid flowchart code

```mermaid
flowchart TD
    A([Start]) --> B[/Read capacity, initial level, threshold, and interval data/]
    B --> C[Set level to initial level]
    C --> D{More intervals?}
    D -- Yes --> E[Read inflow and outflow for interval]
    E --> F[Calculate proposed level = level + inflow - outflow]
    F --> G{Proposed level greater than capacity?}
    G -- Yes --> H[Record overflow; set level to capacity]
    G -- No --> I{Proposed level below zero?}
    I -- Yes --> J[Record shortage; set level to zero]
    I -- No --> K[Set level to proposed level]
    H --> L[Record ending level]
    J --> L
    K --> L
    L --> M{Threshold reached for the first time?}
    M -- Yes --> N[Save current interval number]
    M -- No --> D
    N --> D
    D -- No --> O[/Print interval results and first threshold interval/]
    O --> P([End])
```
