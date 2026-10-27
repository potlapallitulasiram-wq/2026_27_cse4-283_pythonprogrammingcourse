## Problem statement

Create a Python program to plan the finances for a campus event. It calculates total event costs for the venue, equipment, catering, transport, and certificates; the contribution collected from participants; any sponsorship shortfall; and the minimum number of registrations required to break even.

For this example, venue and equipment are fixed costs. Catering, transport, and certificates are costs per participant. Sponsorship is treated as a fixed amount.

## Algorithm

1. Read the venue and equipment costs.
2. Read the catering, transport, and certificate costs per participant.
3. Read the sponsorship amount, contribution per participant, and expected registrations.
4. Calculate fixed costs: venue + equipment.
5. Calculate variable cost per participant: catering + transport + certificates.
6. Calculate total event costs for the expected registrations.
7. Calculate participant contributions and the amount still unfunded after sponsorship and participant contributions.
8. Calculate the net amount available per participant: contribution per participant − variable cost per participant.
9. If the net amount is positive, calculate the break-even registration count as the ceiling of:
   `(fixed costs − sponsorship) ÷ net amount per participant`.
10. If the net amount is zero or negative, report that break-even cannot be reached through registrations alone.

## Flowchart

flowchart TD
    Start([Start])
    Inputs[/Input venue and equipment costs<br/>Input per-participant costs<br/>Input sponsorship, contribution, and registrations/]
    Fixed[Calculate fixed costs<br/>venue + equipment]
    Variable[Calculate variable cost per participant<br/>catering + transport + certificates]
    Total[Calculate total costs and participant contributions]
    Shortfall[Calculate funding shortfall<br/>max(0, total costs - sponsorship - contributions)]
    Check{Is contribution per participant<br/>greater than variable cost per participant?}
    BreakEven[Calculate break-even registrations<br/>ceil(max(0, fixed costs - sponsorship)<br/>/ net per participant)]
    Impossible[Report break-even cannot be reached<br/>through registrations alone]
    Output[/Display costs, contributions,<br/>shortfall, and break-even count/]
    End([End])

    Start --> Inputs --> Fixed --> Variable --> Total --> Shortfall --> Check
    Check -- Yes --> BreakEven --> Output --> End
    Check -- No --> Impossible --> Output

## Sample input

```text
Venue cost: 5000
Equipment cost: 2000
Catering cost per participant: 300
Transport cost per participant: 100
Certificate cost per participant: 50
Sponsorship amount: 3000
Contribution per participant: 600
Expected registrations: 30
```

## Sample output

```text
--- Event Financial Summary ---
Fixed costs:                 7000.00
Variable cost per participant: 450.00
Total costs:                 20500.00
Participant contributions:   18000.00
Sponsorship:                 3000.00
Funding shortfall:           0.00
Break-even registrations:    23
```

## Mermaid flowchart code

```mermaid
flowchart TD
    Start([Start])
    Inputs[/Input venue and equipment costs<br/>Input per-participant costs<br/>Input sponsorship, contribution, and registrations/]
    Fixed[Calculate fixed costs<br/>venue + equipment]
    Variable[Calculate variable cost per participant<br/>catering + transport + certificates]
    Total[Calculate total costs and participant contributions]
    Shortfall[Calculate funding shortfall<br/>max(0, total costs - sponsorship - contributions)]
    Check{Is contribution per participant<br/>greater than variable cost per participant?}
    BreakEven[Calculate break-even registrations<br/>ceil(max(0, fixed costs - sponsorship)<br/>/ net per participant)]
    Impossible[Report break-even cannot be reached<br/>through registrations alone]
    Output[/Display costs, contributions,<br/>shortfall, and break-even count/]
    End([End])

    Start --> Inputs --> Fixed --> Variable --> Total --> Shortfall --> Check
    Check -- Yes --> BreakEven --> Output --> End
    Check -- No --> Impossible --> Output
```
