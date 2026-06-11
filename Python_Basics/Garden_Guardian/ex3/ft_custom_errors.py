class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def ft_custom_errors(temp: int, water_level: int, plant: str) -> None:
    if temp > 40 and water_level <= 0:
        raise PlantError(f"The {plant} plant is wilting!")
    elif water_level <= 0:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        ft_custom_errors(42, 0, "tomato")
    except PlantError as err:
        print(f"Caught PlantError: {err}\n")
    try:
        print("Testing WaterError...")
        ft_custom_errors(30, 0, "tomato")
    except WaterError as err:
        print(f"Caught WaterError: {err}\n")
    print("Testing catching all garden errors...")
    try:
        ft_custom_errors(42, 0, "tomato")
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        ft_custom_errors(30, 0, "tomato")
    except GardenError as err:
        print(f"Caught GardenError: {err}\n")


if __name__ == "__main__":
    test_custom_errors()
    print("All tests completed - program didn’t crash!")
