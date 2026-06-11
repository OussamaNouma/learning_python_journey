class Plant:
    class Statistic:
        _nb_age: int = 0
        _nb_grow: int = 0
        _nb_show: int = 0

        def display(self) -> None:
            print(f"Stats: {self._nb_grow} grow, "
                  f"{self._nb_age} age, {self._nb_show} show")
    _name: str
    _height: float
    _age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name, self._height, self._age_days = name, height, age_days
        self.stats = Plant.Statistic()

    @staticmethod
    def is_olde_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def unknown_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self._height += 15
        self.stats._nb_grow += 1

    def age(self) -> None:
        self._age_days += 20
        self.stats._nb_age += 1

    def show(self) -> None:
        self.stats._nb_show += 1
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age_days} days old")


class Tree(Plant):
    class TreeStat(Plant.Statistic):
        _nb_shade: int = 0

        def display(self) -> None:
            super().display()
            print(f"{self._nb_shade} shade")

    def __init__(self, name: str, height: float, age_days: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter
        self.stats: Tree.TreeStat = Tree.TreeStat()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}")

    def produce_shade(self) -> None:
        self.stats._nb_shade += 1
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
        self.seed = 0

    def bloom(self) -> None:
        self.flag = True
        self.seed += 42

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.flag is True:
            print(f"{self._name} is blooming beautifully!")
        elif self.flag is False:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed}")


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


def display_stats(plant: Plant) -> None:
    plant.stats.display()


if __name__ == "__main__":
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    seed: Seed = Seed("Tulipe", 15.0, 45, "red")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    tomato: Vegetable = Vegetable("Tomato", 5.0, 10, "April")
    unknown: Plant = Plant.unknown_plant()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_olde_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_olde_than_year(400)}")
    print("\n=== Flower")
    rose.show()
    print(f"[statistics for {rose._name}]")
    rose.stats.display()
    print(f"[asking the {rose._name} to bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    print(f"[statistics for {rose._name}]")
    rose.stats.display()

    print("\n=== Tree")
    oak.show()
    print(f"[statistics for {oak._name}]")
    display_stats(oak)
    oak.produce_shade()
    print(f"[statistics for {oak._name}]")
    display_stats(oak)

    print("\n=== Seed")
    seed.show()
    print(f"[make {seed._name} grow, age and bloom]")
    seed.bloom()
    seed.grow()
    seed.age()
    seed.show()
    print(f"[statistics for {seed._name}]")
    seed.stats.display()

    print("\n=== Unknown")
    unknown.show()
    unknown.stats.display()
