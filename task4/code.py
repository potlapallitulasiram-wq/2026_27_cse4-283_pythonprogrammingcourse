def simulate_tank(capacity, initial_level, threshold, intervals):
    level = initial_level
    first_threshold_interval = None
    results = []

    for interval_number, (inflow, outflow) in enumerate(intervals, start=1):
        proposed_level = level + inflow - outflow
        overflow = max(0, proposed_level - capacity)
        shortage = max(0, -proposed_level)

        # Keep the actual tank level within its physical limits.
        level = min(capacity, max(0, proposed_level))

        if first_threshold_interval is None and level >= threshold:
            first_threshold_interval = interval_number

        results.append({
            "interval": interval_number,
            "inflow": inflow,
            "outflow": outflow,
            "level": level,
            "overflow": overflow,
            "shortage": shortage,
        })

    return results, first_threshold_interval


def main():
    number_of_intervals = int(input("Number of intervals: "))
    capacity = float(input("Tank capacity: "))
    initial_level = float(input("Initial water level: "))
    threshold = float(input("Target threshold: "))

    intervals = []
    for i in range(1, number_of_intervals + 1):
        inflow, outflow = map(
            float,
            input(f"Interval {i} inflow and outflow: ").split()
        )
        intervals.append((inflow, outflow))

    results, first_interval = simulate_tank(
        capacity, initial_level, threshold, intervals
    )

    print("\nInterval | Inflow | Outflow | Ending level | Overflow | Shortage")
    for result in results:
        print(
            f"{result['interval']:8} | "
            f"{result['inflow']:6g} | "
            f"{result['outflow']:7g} | "
            f"{result['level']:12g} | "
            f"{result['overflow']:8g} | "
            f"{result['shortage']:8g}"
        )

    if first_interval is None:
        print("\nThe threshold was not reached.")
    else:
        print(f"\nThe threshold was first reached in interval {first_interval}.")


if __name__ == "__main__":
    main()
