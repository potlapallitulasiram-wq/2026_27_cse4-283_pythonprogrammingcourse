
def analyze_orders(initial_inventory, orders):
    inventory = initial_inventory
    results = []

    for order in orders:
        order_id = order["id"]
        ordered = order["ordered"]
        dispatched = order["dispatched"]
        returned = order["returned"]

        issues = []

        if ordered < 0 or dispatched < 0 or returned < 0:
            issues.append("quantities cannot be negative")
        if dispatched > ordered:
            issues.append("dispatched quantity exceeds ordered quantity")
        if returned > dispatched:
            issues.append("returned quantity exceeds dispatched quantity")

        if issues:
            results.append({
                "id": order_id,
                "status": "INCONSISTENT",
                "outstanding": None,
                "issues": issues,
                "inventory": inventory,
            })
            continue

        outstanding = ordered - dispatched
        inventory = inventory - dispatched + returned

        results.append({
            "id": order_id,
            "status": "OK",
            "outstanding": outstanding,
            "issues": [],
            "inventory": inventory,
        })

    return results, inventory


def main():
    initial_inventory = int(input("Enter starting inventory: "))
    count = int(input("Enter number of orders: "))

    orders = []
    for _ in range(count):
        order_id = input("Order ID: ")
        ordered = int(input("Ordered quantity: "))
        dispatched = int(input("Dispatched quantity: "))
        returned = int(input("Returned quantity: "))

        orders.append({
            "id": order_id,
            "ordered": ordered,
            "dispatched": dispatched,
            "returned": returned,
        })

    results, final_inventory = analyze_orders(initial_inventory, orders)

    print("\nOrder analysis")
    for result in results:
        if result["status"] == "OK":
            print(
                f'{result["id"]}: OK, '
                f'outstanding={result["outstanding"]}, '
                f'inventory={result["inventory"]}'
            )
        else:
            print(
                f'{result["id"]}: INCONSISTENT, '
                f'issues={"; ".join(result["issues"])}, '
                f'inventory unchanged at {result["inventory"]}'
            )

    print(f"\nFinal inventory: {final_inventory}")


if __name__ == "__main__":
    main()
