def recursive_counter(day: int) -> None:
    if day >= 1:
        recursive_counter(day - 1)
        print(f"Day {day}")


def ft_count_harvest_recursive() -> None:
    day: int = int(input("Days until harvest: "))
    recursive_counter(day)
    print("Harvest time!")
