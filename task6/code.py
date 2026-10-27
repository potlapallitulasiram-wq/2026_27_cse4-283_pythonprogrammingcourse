def classify_congestion(vehicle_count, capacity):
    """Return a congestion label based on capacity utilization."""
    utilization = vehicle_count / capacity

    if utilization < 0.50:
        return "Low"
    elif utilization < 0.80:
        return "Moderate"
    elif utilization <= 1.00:
        return "High"
    else:
        return "Over capacity"


def main():
    try:
        road_count = int(input("Enter number of roads: "))
        interval_count = int(input("Enter number of time intervals: "))

        if road_count <= 0 or interval_count <= 0:
            print("Road and interval counts must be positive.")
            return

        roads = []

        for road_index in range(road_count):
            print(f"\nRoad {road_index + 1}")
            name = input("Road name: ").strip()
            capacity = int(input("Capacity (vehicles per interval): "))

            if capacity <= 0:
                print("Capacity must be positive.")
                return

            counts = []
            for interval_index in range(interval_count):
                count = int(input(
                    f"Vehicle count for interval {interval_index + 1}: "
                ))
                if count < 0:
                    print("Vehicle counts cannot be negative.")
                    return
                counts.append(count)

            roads.append({
                "name": name,
                "capacity": capacity,
                "counts": counts,
            })

        print("\nTRAFFIC ANALYSIS")
        print("-" * 60)

        for road in roads:
            name = road["name"]
            capacity = road["capacity"]
            counts = road["counts"]

            peak_count = max(counts)
            peak_interval = counts.index(peak_count) + 1

            print(f"\nRoad: {name}")
            for interval_index, count in enumerate(counts, start=1):
                level = classify_congestion(count, capacity)
                print(
                    f"  Interval {interval_index}: "
                    f"{count} vehicles — {level}"
                )

            print(
                f"  Peak traffic: {peak_count} vehicles "
                f"in interval {peak_interval}"
            )

            if peak_count > capacity:
                print(
                    f"  Capacity alert: exceeds capacity "
                    f"({capacity} vehicles)"
                )
            else:
                print("  Capacity status: within capacity")

    except ValueError:
        print("Please enter valid whole numbers.")


if __name__ == "__main__":
    main()
