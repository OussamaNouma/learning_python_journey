def ft_count_harvest_iterative() -> None:
    day: int = int(input("Days until harvest: "))
    for x in range(1, day + 1):
        print(f"Day {x}")
    print("Harvest time!")
