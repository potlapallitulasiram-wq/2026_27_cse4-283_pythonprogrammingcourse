import math

# Fixed event costs
venue_cost = float(input("Venue cost: "))
equipment_cost = float(input("Equipment cost: "))

# Costs for each participant
catering_cost_per_participant = float(input("Catering cost per participant: "))
transport_cost_per_participant = float(input("Transport cost per participant: "))
certificate_cost_per_participant = float(input("Certificate cost per participant: "))

# Funding and attendance
sponsorship = float(input("Sponsorship amount: "))
contribution_per_participant = float(input("Contribution per participant: "))
expected_registrations = int(input("Expected registrations: "))

fixed_costs = venue_cost + equipment_cost

variable_cost_per_participant = (
    catering_cost_per_participant
    + transport_cost_per_participant
    + certificate_cost_per_participant
)

total_costs = fixed_costs + (
    variable_cost_per_participant * expected_registrations
)

participant_contributions = (
    contribution_per_participant * expected_registrations
)

total_funding = sponsorship + participant_contributions
shortfall = max(0, total_costs - total_funding)

net_per_participant = (
    contribution_per_participant - variable_cost_per_participant
)

print("\n--- Event Financial Summary ---")
print(f"Fixed costs:                 {fixed_costs:.2f}")
print(f"Variable cost per participant: {variable_cost_per_participant:.2f}")
print(f"Total costs:                 {total_costs:.2f}")
print(f"Participant contributions:   {participant_contributions:.2f}")
print(f"Sponsorship:                 {sponsorship:.2f}")
print(f"Funding shortfall:           {shortfall:.2f}")

if net_per_participant > 0:
    amount_to_cover = max(0, fixed_costs - sponsorship)
    break_even_registrations = math.ceil(
        amount_to_cover / net_per_participant
    )
    print(f"Break-even registrations:    {break_even_registrations}")
else:
    print(
        "Break-even registrations:    Not possible through registrations "
        "alone; the contribution per participant must exceed the "
        "variable cost per participant."
    )
