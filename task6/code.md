# Traffic Flow and Congestion Analysis

## Problem statement

Process vehicle counts for multiple roads over several time intervals. For each road and interval, classify congestion based on vehicle count, identify peak traffic periods, and flag roads whose maximum count exceeds their capacity.

This example uses fixed thresholds:

- **Low:** fewer than 50% of capacity
- **Moderate:** 50% to less than 80%
- **High:** 80% to 100%
- **Over capacity:** more than 100%

## Algorithm

1. Read the number of roads and time intervals.
2. For each road, read its name, capacity, and vehicle count for each interval.
3. For each count:
   - Calculate utilization as `count / capacity`.
   - Classify the congestion level using the thresholds above.
4. Find each road’s peak count and the corresponding interval.
5. Flag a road if its peak count is greater than its capacity.
6. Print the interval classifications, peak periods, and capacity alerts.

 

## Sample output

```text
TRAFFIC ANALYSIS
------------------------------------------------------------

Road: Main Street
  Interval 1: 40 vehicles — Low
  Interval 2: 85 vehicles — High
  Interval 3: 110 vehicles — Over capacity
  Peak traffic: 110 vehicles in interval 3
  Capacity alert: exceeds capacity (100 vehicles)

Road: Lake Road
  Interval 1: 30 vehicles — Low
  Interval 2: 55 vehicles — Moderate
  Interval 3: 70 vehicles — High
  Peak traffic: 70 vehicles in interval 3
  Capacity status: within capacity
```

## Mermaid flowchart code

```mermaid
flowchart TD
    A([Start]) --> B[/Input roads and time intervals/]
    B --> C[Read each road's name and capacity]
    C --> D[Read vehicle counts for all intervals]
    D --> E[Calculate utilization for each count]
    E --> F{Choose congestion level}
    F -->|Below 50%| G[Low]
    F -->|50% to under 80%| H[Moderate]
    F -->|80% to 100%| I[High]
    F -->|Above 100%| J[Over capacity]
    G --> K[Find peak count and interval]
    H --> K
    I --> K
    J --> K
    K --> L{Peak count greater than capacity?}
    L -->|Yes| M[Report capacity exceeded]
    L -->|No| N[Report within capacity]
    M --> O{More roads to process?}
    N --> O
    O -->|Yes| C
    O -->|No| P[/Display traffic analysis/]
    P --> Q([End])
```
