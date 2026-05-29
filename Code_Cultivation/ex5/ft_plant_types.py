class Plant:
    _name: str
    _height: float
    _age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name, self._height, self._age_days = name, height, age_days

    def grow(self) -> None:
        self._height += 2.1

    def age(self) -> None:
        self._age_days += 1

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age_days} days old")


class Tree(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of"
              f" {round(self._height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 color: str) -> None:
        super().__init__(name, height, age_days)
        self.color = color
        self.flag = False

    def bloom(self) -> None:
        self.flag = True
        print(f"[asking the {self._name} to bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.flag is True:
            print(f"{self._name} is blooming beautifully!")
        elif self.flag is False:
            print(f"{self._name} has not bloomed yet")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "Red")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    tomato: Vegetable = Vegetable("Tomato", 5.0, 10, "April")
    rose.show()
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for x in range(0, 20):
        tomato.grow()
        tomato.age()
    tomato.show()
