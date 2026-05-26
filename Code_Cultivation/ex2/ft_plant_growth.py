class Plant:
    name: str
    height: float
    age_days: int

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose: Plant
    sunflower: Plant
    cactus: Plant
    rose = Plant()
    rose.name, rose.age_days, rose.height = "Rose", 30, 25.0
    total: float = rose.height
    rose.show()
    for x in range(1, 8):
        print(f"=== Day {x} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - total, 1)}cm")
