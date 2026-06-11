class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose: Plant
    sunflower: Plant
    cactus: Plant
    rose, sunflower, cactus = Plant(), Plant(), Plant()
    rose.name, rose.age, rose.height = "Rose", 30, 25
    sunflower.name, sunflower.age, sunflower.height = "sunflower", 30, 25
    cactus.name, cactus.age, cactus.height = "cactus", 30, 25
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
