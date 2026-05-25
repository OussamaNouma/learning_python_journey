class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        result: str = "Caught PlantError: Invalid plant name to water: '"
        result += plant_name + "'\n.. ending tests and returning to main"
        raise PlantError(result)
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    plant_names: list = ["Tomato", "Lettuce", "Carrot"]
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for x in plant_names:
            try:
                water_plant(x)
            except PlantError as err:
                print(err)
                return
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("lettuce")
    except PlantError as err:
        print(err)
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    test_watering_system()
    print("Cleanup always happens, even with errors!")
