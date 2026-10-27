def get_non_negative_float(prompt):
    """Read a number and reject negative values."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Enter a value that is zero or greater.")
                continue
            return value
        except ValueError:
            print("Enter a valid number.")


def main():
    print("Manufacturing Cost and Profitability Analysis")
    print("-" * 45)

    units = get_non_negative_float("Number of units produced: ")
    material_per_unit = get_non_negative_float("Material cost per unit: ")
    labor_hours = get_non_negative_float("Total labor hours: ")
    hourly_wage = get_non_negative_float("Labor cost per hour: ")
    wastage_percent = get_non_negative_float("Wastage percentage: ")
    machine_hours = get_non_negative_float("Total machine hours: ")
    machine_rate = get_non_negative_float("Machine cost per hour: ")
    selling_price = get_non_negative_float("Selling price per unit: ")
    target_percent = get_non_negative_float("Target profit percentage: ")

    # Calculate production costs.
    material_cost = units * material_per_unit
    wastage_cost = material_cost * wastage_percent / 100
    labor_cost = labor_hours * hourly_wage
    machine_cost = machine_hours * machine_rate

    total_cost = material_cost + wastage_cost + labor_cost + machine_cost
    revenue = units * selling_price
    profit = revenue - total_cost

    if total_cost > 0:
        profit_margin = profit / total_cost * 100
    else:
        profit_margin = 0.0

    profit_per_unit = profit / units if units > 0 else 0.0

   .
    print("\nCost and Profit Summary")
    print("-" * 45)
    print(f"Material cost:       {material_cost:,.2f}")
    print(f"Wastage cost:        {wastage_cost:,.2f}")
    print(f"Labor cost:          {labor_cost:,.2f}")
    print(f"Machine cost:        {machine_cost:,.2f}")
    print(f"Total production cost: {total_cost:,.2f}")
    print(f"Total revenue:       {revenue:,.2f}")
    print(f"Profit / loss:       {profit:,.2f}")
    print(f"Profit per unit:     {profit_per_unit:,.2f}")
    print(f"Profit margin:       {profit_margin:.2f}%")
    print(f"Target profit:       {target_percent:.2f}%")

    if profit_margin >= target_percent:
        print("Result: Profit target met.")
    else:
        print("Result: Profit target not met.")


if __name__ == "__main__":
    main()
