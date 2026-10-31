"""
Day 25 - 2026-10-31
Tool: Electricity Bill Calculator
What it does: Estimates a home electricity bill from the units
(kWh) used in a month, charging by slabs - the first units are
cheaper and later units cost more, like real home tariffs - plus
a fixed service charge.
Who it helps: Families who want to guess this month's bill from the
meter reading and see what extra usage really costs.
Note: Slabs below are a simple EXAMPLE tariff for learning - real
rates and VAT change, so compare with your actual bill.
"""

# (slab size in units, price per unit in taka); None = all remaining
SLABS = [(50, 4.63), (25, 5.26), (125, 7.20), (100, 7.59),
         (100, 8.02), (None, 12.67)]
SERVICE_CHARGE = 42.00


def estimate_bill(units):
    if units < 0:
        raise ValueError("Units cannot be negative.")
    remaining = units
    cost = 0.0
    for size, price in SLABS:
        if remaining <= 0:
            break
        take = remaining if size is None else min(size, remaining)
        cost += take * price
        remaining -= take
    return round(cost + SERVICE_CHARGE, 2)


def units_between(old_reading, new_reading):
    if new_reading < old_reading:
        raise ValueError("New reading cannot be below the old one.")
    return new_reading - old_reading


if __name__ == "__main__":
    used = units_between(1240, 1395)
    print("Units used this month:", used)
    print("Estimated bill:", estimate_bill(used), "taka")
    print("Light month (40 units):", estimate_bill(40), "taka")
