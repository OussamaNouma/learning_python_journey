def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
    elif unit == "area":
        area_unit: str = "square meters"
        print(f"{seed_type.capitalize()} seeds: covers {quantity} {area_unit}")
    else:
        print("Unknown unit type")
