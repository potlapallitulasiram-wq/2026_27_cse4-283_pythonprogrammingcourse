# University Scholarship Allocation

## Problem statement

Design a system that evaluates scholarship applicants using their aggregate marks, subject-wise minimum scores, attendance, and family income. The system must:

- Decide whether each applicant meets all eligibility criteria.
- Rank eligible applicants by academic performance.
- Resolve ties using predefined rules.
- Display the eligibility decision and rank for each applicant.

**Assumptions for this example:** Applicants must have an aggregate of at least 75%, at least 60% in every subject, attendance of at least 75%, and annual family income of no more than ₹300,000. Eligible students are ranked by aggregate marks, then attendance, then lower family income. Remaining ties are broken by applicant name in alphabetical order.

## Algorithm

1. Set the eligibility thresholds and tie-breaking rules.
2. Read the number of applicants.
3. For each applicant, read their name, subject marks, attendance, and annual family income.
4. Calculate the aggregate as the average of their subject marks.
5. Mark the applicant eligible only if:
   - Aggregate meets the minimum.
   - Every subject mark meets the minimum.
   - Attendance meets the minimum.
   - Family income does not exceed the maximum.
6. Sort eligible applicants by:
   1. Aggregate marks, highest first.
   2. Attendance, highest first.
   3. Annual family income, lowest first.
   4. Name, alphabetical order.
7. Assign ranks to eligible applicants.
8. Display each applicant’s eligibility and the ranked list.

## Flowchart


flowchart TD
    Start([Start]) --> Criteria[Set minimum aggregate, subject marks, and attendance; set maximum income]
    Criteria --> Count[Read number of applicants]
    Count --> Input[Read applicant name, subject marks, attendance, and family income]
    Input --> Aggregate[Calculate average subject marks]
    Aggregate --> Check{Meets every eligibility criterion?}
    Check -- Yes --> Eligible[Add applicant to eligible list]
    Check -- No --> Ineligible[Record ineligible status and reason]
    Eligible --> More{More applicants to process?}
    Ineligible --> More
    More -- Yes --> Input
    More -- No --> Sort[Sort eligible applicants by aggregate descending]
    Sort --> Tie1{Aggregate tied?}
    Tie1 -- Yes --> Tie2[Compare attendance descending]
    Tie1 -- No --> Rank[Assign ranks]
    Tie2 --> Tie3{Attendance tied?}
    Tie3 -- Yes --> Tie4[Compare income ascending, then name alphabetically]
    Tie3 -- No --> Rank
    Tie4 --> Rank
    Rank --> Output[Display eligibility results and scholarship ranking]
    Output --> End([End])
## Sample output

```text
Applicant results
---------------------------------------------------------------------------
Asha: Eligible (aggregate: 85.00%)
Ravi: Eligible (aggregate: 85.00%)
Meena: Ineligible (aggregate: 79.33%)
  Reason: a subject mark is below 60%

Scholarship ranking
---------------------------------------------------------------------------
1. Asha | Aggregate: 85.00% | Attendance: 92.00% | Income: ₹200,000
2. Ravi | Aggregate: 85.00% | Attendance: 92.00% | Income: ₹250,000
```

## Mermaid flowchart code

```mermaid
flowchart TD
    Start([Start]) --> Criteria[Set minimum aggregate, subject marks, and attendance; set maximum income]
    Criteria --> Count[Read number of applicants]
    Count --> Input[Read applicant name, subject marks, attendance, and family income]
    Input --> Aggregate[Calculate average subject marks]
    Aggregate --> Check{Meets every eligibility criterion?}
    Check -- Yes --> Eligible[Add applicant to eligible list]
    Check -- No --> Ineligible[Record ineligible status and reason]
    Eligible --> More{More applicants to process?}
    Ineligible --> More
    More -- Yes --> Input
    More -- No --> Sort[Sort eligible applicants by aggregate descending]
    Sort --> Tie1{Aggregate tied?}
    Tie1 -- Yes --> Tie2[Compare attendance descending]
    Tie1 -- No --> Rank[Assign ranks]
    Tie2 --> Tie3{Attendance tied?}
    Tie3 -- Yes --> Tie4[Compare income ascending, then name alphabetically]
    Tie3 -- No --> Rank
    Tie4 --> Rank
    Rank --> Output[Display eligibility results and scholarship ranking]
    Output --> End([End])
```
