def classify_performance(success_rate):
    if success_rate >= 80:
        return "High"
    elif success_rate >= 50:
        return "Moderate"
    return "Low"


def main():
    student_count, question_count = map(
        int, input("Enter number of students and questions: ").split()
    )

    answer_key = input("Enter the answer key: ").split()

    if len(answer_key) != question_count:
        print(f"Error: The answer key must contain {question_count} answers.")
        return

    student_answers = []

    for student in range(student_count):
        answers = input(f"Enter answers for student {student + 1}: ").split()

        if len(answers) != question_count:
            print(
                f"Error: Student {student + 1} must have "
                f"{question_count} answers."
            )
            return

        student_answers.append(answers)

    correct_counts = [0] * question_count

    for answers in student_answers:
        for question in range(question_count):
            if answers[question] == answer_key[question]:
                correct_counts[question] += 1

    missed_counts = []
    success_rates = []

    print("\nQuestion-wise performance")
    print("Question | Correct | Missed | Success Rate | Classification")
    print("-" * 65)

    for question in range(question_count):
        correct = correct_counts[question]
        missed = student_count - correct
        rate = (correct / student_count) * 100 if student_count > 0 else 0

        missed_counts.append(missed)
        success_rates.append(rate)

        classification = classify_performance(rate)

        print(
            f"Q{question + 1:<8} | {correct:<7} | {missed:<6} | "
            f"{rate:>6.2f}%       | {classification}"
        )

    if student_count == 0:
        print("\nNo student answers were provided.")
        return

    highest_missed_count = max(missed_counts)
    most_missed_questions = [
        question + 1
        for question, count in enumerate(missed_counts)
        if count == highest_missed_count
    ]

    questions_text = ", ".join(f"Q{number}" for number in most_missed_questions)
    print(
        f"\nMost frequently missed: {questions_text} "
        f"({highest_missed_count} students missed each)."
    )


if __name__ == "__main__":
    main()
