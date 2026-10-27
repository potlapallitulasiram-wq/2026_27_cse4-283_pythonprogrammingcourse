

MIN_AGGREGATE = 75.0
MIN_SUBJECT_MARK = 60.0
MIN_ATTENDANCE = 75.0
MAX_FAMILY_INCOME = 300_000.0


def evaluate_applicants(applicants):
    """Calculate aggregates and separate eligible applicants."""
    eligible = []
    results = []

    for applicant in applicants:
        marks = applicant["subject_marks"]
        aggregate = sum(marks) / len(marks) if marks else 0.0
        applicant["aggregate"] = aggregate

        reasons = []

        if aggregate < MIN_AGGREGATE:
            reasons.append(f"aggregate below {MIN_AGGREGATE:.0f}%")

        if any(mark < MIN_SUBJECT_MARK for mark in marks):
            reasons.append(f"a subject mark is below {MIN_SUBJECT_MARK:.0f}%")

        if applicant["attendance"] < MIN_ATTENDANCE:
            reasons.append(f"attendance below {MIN_ATTENDANCE:.0f}%")

        if applicant["family_income"] > MAX_FAMILY_INCOME:
            reasons.append(f"income exceeds ₹{MAX_FAMILY_INCOME:,.0f}")

        if reasons:
            applicant["status"] = "Ineligible"
            applicant["reason"] = "; ".join(reasons)
        else:
            applicant["status"] = "Eligible"
            applicant["reason"] = ""
            eligible.append(applicant)

        results.append(applicant)

    # Tie-break order:
    # 1. Higher aggregate
    # 2. Higher attendance
    # 3. Lower family income
    # 4. Applicant name alphabetically
    eligible.sort(
        key=lambda applicant: (
            -applicant["aggregate"],
            -applicant["attendance"],
            applicant["family_income"],
            applicant["name"].casefold(),
        )
    )

    for rank, applicant in enumerate(eligible, start=1):
        applicant["rank"] = rank

    return results, eligible


def main():
    count = int(input("Number of applicants: "))
    applicants = []

    for index in range(count):
        print(f"\nApplicant {index + 1}")
        name = input("Name: ")
        subject_count = int(input("Number of subjects: "))

        marks = []
        for subject_index in range(subject_count):
            mark = float(input(f"Subject {subject_index + 1} mark (0-100): "))
            marks.append(mark)

        attendance = float(input("Attendance percentage: "))
        family_income = float(input("Annual family income (₹): "))

        applicants.append(
            {
                "name": name,
                "subject_marks": marks,
                "attendance": attendance,
                "family_income": family_income,
            }
        )

    results, eligible = evaluate_applicants(applicants)

    print("\nApplicant results")
    print("-" * 75)
    for applicant in results:
        print(
            f"{applicant['name']}: {applicant['status']} "
            f"(aggregate: {applicant['aggregate']:.2f}%)"
        )
        if applicant["status"] == "Ineligible":
            print(f"  Reason: {applicant['reason']}")

    print("\nScholarship ranking")
    print("-" * 75)
    if not eligible:
        print("No applicants meet the eligibility criteria.")
    else:
        for applicant in eligible:
            print(
                f"{applicant['rank']}. {applicant['name']} | "
                f"Aggregate: {applicant['aggregate']:.2f}% | "
                f"Attendance: {applicant['attendance']:.2f}% | "
                f"Income: ₹{applicant['family_income']:,.0f}"
            )


if __name__ == "__main__":
    main()
