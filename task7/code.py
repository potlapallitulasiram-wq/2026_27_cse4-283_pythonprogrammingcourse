def analyze_price_fluctuations(products, threshold):
    """Analyze consecutive price changes for each product."""
    results = []

    for product_name, prices in products.items():
        changes = []

        for previous, current in zip(prices, prices[1:]):
            if previous == 0:
                changes.append(None)
            else:
                percentage_change = ((current - previous) / previous) * 100
                changes.append(percentage_change)

        valid_changes = [change for change in changes if change is not None]

        if valid_changes:
            largest_change = max(valid_changes, key=abs)
            max_fluctuation = abs(largest_change)
        else:
            largest_change = None
            max_fluctuation = 0.0

        results.append({
            "name": product_name,
            "changes": changes,
            "largest_change": largest_change,
            "max_fluctuation": max_fluctuation,
            "flagged": max_fluctuation > threshold,
        })

    return results


def main():
    products = {
        "Laptop": [1000, 1100, 990, 1089],
        "Phone": [500, 525, 520, 546],
        "Headphones": [100, 115, 92, 101.2],
    }
    threshold = 15.0

    results = analyze_price_fluctuations(products, threshold)

    print(f"Threshold: {threshold:.2f}%")

    for result in results:
        print(f"\nProduct: {result['name']}")

        changes_text = [
            "N/A (previous price was zero)" if change is None
            else f"{change:+.2f}%"
            for change in result["changes"]
        ]
        print("Consecutive changes:", ", ".join(changes_text) or "None")

        if result["largest_change"] is None:
            print("Largest change: N/A")
        else:
            print(f"Largest change: {result['largest_change']:+.2f}%")

        print(f"Maximum fluctuation: {result['max_fluctuation']:.2f}%")
        print("Flagged:", "Yes" if result["flagged"] else "No")


if __name__ == "__main__":
    main()
