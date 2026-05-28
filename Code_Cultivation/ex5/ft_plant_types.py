class Plant:
    _name: str
    _height: float
    _age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name, self._height, self._age_days = name, height, age_days

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age_days += 1

    def show(self) -> None:
        print(f"Created: {self._name}: {round(self._height, 1)}cm, "
              f"{self._age_days} days old")


class Tree(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter
    super.show()

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of"
              f" {round(self._height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 color: str) -> None:
        super().__init__(name, height, age_days)
        self.color = color
    super.show()

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    super.show()
