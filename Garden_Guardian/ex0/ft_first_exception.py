def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    try:
        print("Input data is ’25’")
        print(f"Temperature is now {input_temperature("25")}°C")
    except ValueError as err:
        print(err)
    try:
        print("Input data is 'abc'")
        print(input_temperature("abc"))
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")


if __name__ == "__main__":
    test_temperature()
    print("All tests completed - program didn’t crash!")
