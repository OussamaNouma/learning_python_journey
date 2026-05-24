def garden_operations(operation_number: int):
    if operation_number == 0:
        return int("abc")
    elif operation_number == 1:
        return 42 / 0
    elif operation_number == 2:
        return open("./test.txt", "r")
    elif operation_number == 3:
        return "abc" + 42
    else:
        return


def test_error_types():
    print("=== Garden Error Types Demo ===")
    for x in range(5):
        print(f"Testing operation {x}...")
        try:
            garden_operations(x)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as error:
            print(f"Caught {error.__class__.__name__}: {error}")


if __name__ == "__main__":
    test_error_types()
    print("All tests completed - program didn’t crash!")
