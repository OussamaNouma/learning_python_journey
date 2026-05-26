class Plant:
    name: str
    height: float
    age_days: int

    def __init__(self, name, height, age_days) -> None:
        self.name, self.height, self.age_days = name, height, age_days

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"Created: {self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose: Plant = Plant("Rose", round(25, 1), 30)
    piment: Plant = Plant("Piment", round(12.3, 1), 25)
    lys: Plant = Plant("Fleur de Lys", round(28, 1), 45)
    figuier: Plant = Plant("Figuier", round(435, 1), 2131)
    olivier: Plant = Plant("Olivier", round(345, 1), 6324)
    rose.show()
    piment.show()
    lys.show()
    figuier.show()
    olivier.show()
