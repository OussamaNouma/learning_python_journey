def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    try:
        print("Input data is ’25’")
        print(f"Temperature is now {input_temperature("25")}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    try:
        print("Input data is 'abc'")
        print(input_temperature("abc"))
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    try:
        print("Input data is '100'")
        print(input_temperature("100"))
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    try:
        print("Input data is '-50'")
        print(input_temperature("-50"))
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")


if __name__ == "__main__":
    test_temperature()
    print("All tests completed - program didn’t crash!")
