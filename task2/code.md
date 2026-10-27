## Problem statement

Write a Python program to calculate the production cost and profitability of a manufactured product. The program accepts the number of units produced, material cost per unit, labor hours and hourly wage, wastage percentage, machine hours and hourly machine rate, selling price per unit, and target profit percentage.

Calculate material cost, labor cost, wastage cost, machine cost, total production cost, revenue, profit, profit margin, and profit per unit. Report whether the production meets the specified profit target.

**Assumption:** Wastage is calculated as a percentage of material cost. The profit target is a percentage of total production cost.

## Algorithm

1. Read the production and rate inputs.
2. Calculate base material cost: `units × material cost per unit`.
3. Calculate wastage cost: `base material cost × wastage percentage ÷ 100`.
4. Calculate labor cost: `labor hours × hourly wage`.
5. Calculate machine cost: `machine hours × machine rate`.
6. Add material, wastage, labor, and machine costs to get total production cost.
7. Calculate revenue: `units × selling price per unit`.
8. Calculate profit: `revenue − total production cost`.
9. Calculate profit margin: `profit ÷ total production cost × 100`.
10. Compare the profit margin with the target and display whether the target is met.

## Flowchart
 flowchart TD
    A([Start]) --> B[/Read units, rates, hours, wastage, selling price, and target/]
    B --> C[Calculate material cost]
    C --> D[Calculate wastage cost]
    D --> E[Calculate labor and machine costs]
    E --> F[Calculate total production cost]
    F --> G[Calculate revenue and profit]
    G --> H[Calculate profit margin]
    H --> I{Profit margin >= target?}
    I -- Yes --> J[Display target met]
    I -- No --> K[Display target not met]
    J --> L([End])
    K --> L

## Sample input

```text
Number of units produced: 100
Material cost per unit: 20
Total labor hours: 40
Labor cost per hour: 15
Wastage percentage: 5
Total machine hours: 10
Machine cost per hour: 30
Selling price per unit: 45
Target profit percentage: 20
```

## Sample output

```text
Cost and Profit Summary
---------------------------------------------
Material cost:       2,000.00
Wastage cost:        100.00
Labor cost:          600.00
Machine cost:        300.00
Total production cost: 3,000.00
Total revenue:       4,500.00
Profit / loss:       1,500.00
Profit per unit:     15.00
Profit margin:       50.00%
Target profit:       20.00%
Result: Profit target met.
```

## Mermaid flowchart code

```mermaid
flowchart TD
    A([Start]) --> B[/Read units, rates, hours, wastage, selling price, and target/]
    B --> C[Calculate material cost]
    C --> D[Calculate wastage cost]
    D --> E[Calculate labor and machine costs]
    E --> F[Calculate total production cost]
    F --> G[Calculate revenue and profit]
    G --> H[Calculate profit margin]
    H --> I{Profit margin >= target?}
    I -- Yes --> J[Display target met]
    I -- No --> K[Display target not met]
    J --> L([End])
    K --> L
```
