def distribute_copies(book_name, available_copies, branches):
    """
    branches: list of dictionaries with:
        name: branch name
        stock: copies currently available at the branch
        demand: total copies requested
        priority: larger number means higher priority
    """
    if available_copies < 0:
        raise ValueError("Available copies cannot be negative.")

    for branch in branches:
        if branch["stock"] < 0 or branch["demand"] < 0:
            raise ValueError("Stock and demand cannot be negative.")

    # Highest priority first, then largest shortage, then alphabetical name.
    ordered = sorted(
        branches,
        key=lambda branch: (
            -branch["priority"],
            -max(0, branch["demand"] - branch["stock"]),
            branch["name"].lower(),
        ),
    )

    remaining = available_copies
    results = []

    for branch in ordered:
        need = max(0, branch["demand"] - branch["stock"])
        allocated = min(need, remaining)
        remaining -= allocated

        unmet = max(0, need - allocated)

        results.append({
            "name": branch["name"],
            "priority": branch["priority"],
            "stock": branch["stock"],
            "demand": branch["demand"],
            "allocated": allocated,
            "unmet": unmet,
        })

    return results, remaining


def main():
    book_name = input("Book title: ").strip()
    available_copies = int(input("Copies available for distribution: "))
    branch_count = int(input("Number of branches: "))

    branches = []

    for i in range(branch_count):
        print(f"\nBranch {i + 1}")
        name = input("Name: ").strip()
        stock = int(input("Current stock: "))
        demand = int(input("Borrowing demand: "))
        priority = int(input("Priority (higher number = higher priority): "))

        branches.append({
            "name": name,
            "stock": stock,
            "demand": demand,
            "priority": priority,
        })

    results, leftover = distribute_copies(
        book_name, available_copies, branches
    )

    print(f"\nDistribution for: {book_name}")
    print("-" * 70)
    print(f"{'Branch':<18}{'Priority':>10}{'Stock':>10}"
          f"{'Demand':>10}{'Allocated':>12}{'Unmet':>10}")
    print("-" * 70)

    for result in results:
        print(
            f"{result['name']:<18}"
            f"{result['priority']:>10}"
            f"{result['stock']:>10}"
            f"{result['demand']:>10}"
            f"{result['allocated']:>12}"
            f"{result['unmet']:>10}"
        )

    print("-" * 70)
    print(f"Copies left undistributed: {leftover}")


if __name__ == "__main__":
    main()
