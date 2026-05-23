def ft_water_reminder() -> None:
    watering: int = int(input("Days since last watering: "))
    if watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
