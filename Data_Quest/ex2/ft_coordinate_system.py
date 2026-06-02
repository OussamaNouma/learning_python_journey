import math


def get_player_pos() -> tuple:
    while True:
        try:
            x, y, z = input("Enter new coordinates as "
                            "floats in format ’x,y,z’: ").split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        my_list: list[str] = [x, y, z]
        new_list: list[float] = []
        for i in my_list:
            try:
                new_list.append(float(i))
            except ValueError:
                print(f"Error on parameter ’{i}’: "
                      f"could not convert string to float: ’{i}’")
                break
        else:
            return tuple(new_list)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_pos: tuple = get_player_pos()
    x1, y1, z1 = first_pos[0], first_pos[1], first_pos[2]
    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    middle: float = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    print(f"Distance to center: {round(middle, 4)}")
    print("Get a second set of coordinates")
    second_pos: tuple = get_player_pos()
    x2, y2, z2 = second_pos[0], second_pos[1], second_pos[2]
    x_d, y_d, z_d = x1 - x2, y1 - y2, z1 - z2
    distance: float = math.sqrt((x_d) ** 2 + (y_d) ** 2 + (z_d) ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")
