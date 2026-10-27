# Multi-Product Price Fluctuation Analysis

## Problem statement

Given historical prices for multiple products, calculate the percentage change between each pair of consecutive prices. Find each product’s maximum absolute percentage fluctuation and flag products whose maximum fluctuation exceeds a supplied threshold.

A positive percentage means the price increased; a negative percentage means it decreased. The maximum fluctuation is measured by the absolute percentage change.

## Algorithm

1. Read the fluctuation threshold.
2. For each product, read its name and list of historical prices.
3. For each consecutive pair of prices:
   - If the previous price is nonzero, calculate  
     `((current_price - previous_price) / previous_price) * 100`.
   - Record the percentage change.
4. Find the change with the largest absolute value.
5. Flag the product if that absolute change is greater than the threshold.
6. Display each product’s changes, maximum fluctuation, and flag status.

## Flowchart

flowchart TD
    Start([Start]) --> Threshold[/Input fluctuation threshold/]
    Threshold --> Products[/Input product names and historical price lists/]
    Products --> Check{Another product to analyze?}

    Check -- Yes --> Select[Select next product and its prices]
    Select --> Changes[Calculate percentage changes between consecutive prices]
    Changes --> Maximum[Find change with greatest absolute value]
    Maximum --> Compare{Maximum fluctuation exceeds threshold?}

    Compare -- Yes --> Flag[Set flagged status to Yes]
    Compare -- No --> NoFlag[Set flagged status to No]

    Flag --> Output[Display changes, maximum fluctuation, and status]
    NoFlag --> Output
    Output --> Check

    Check -- No --> End([End])

## Sample input

```text
Threshold: 15.0%

Laptop prices: 1000, 1100, 990, 1089
Phone prices: 500, 525, 520, 546
Headphones prices: 100, 115, 92, 101.2
```

## Sample output

```text
Threshold: 15.00%

Product: Laptop
Consecutive changes: +10.00%, -10.00%, +10.00%
Largest change: +10.00%
Maximum fluctuation: 10.00%
Flagged: No

Product: Phone
Consecutive changes: +5.00%, -0.95%, +5.00%
Largest change: +5.00%
Maximum fluctuation: 5.00%
Flagged: No

Product: Headphones
Consecutive changes: +15.00%, -20.00%, +10.00%
Largest change: -20.00%
Maximum fluctuation: 20.00%
Flagged: Yes
```

## Mermaid flowchart code

```mermaid
flowchart TD
    Start([Start]) --> Threshold[/Input fluctuation threshold/]
    Threshold --> Products[/Input product names and historical price lists/]
    Products --> Check{Another product to analyze?}

    Check -- Yes --> Select[Select next product and its prices]
    Select --> Changes[Calculate percentage changes between consecutive prices]
    Changes --> Maximum[Find change with greatest absolute value]
    Maximum --> Compare{Maximum fluctuation exceeds threshold?}

    Compare -- Yes --> Flag[Set flagged status to Yes]
    Compare -- No --> NoFlag[Set flagged status to No]

    Flag --> Output[Display changes, maximum fluctuation, and status]
    NoFlag --> Output
    Output --> Check

    Check -- No --> End([End])
```
