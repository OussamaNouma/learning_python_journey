class Plant:
    _name: str
    _height: float
    _age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name, self._height, self._age_days = name, height, age_days

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can’t be negative"
                  "\nHeight update rejected")
            return
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can’t be negative"
                  "\nAge update rejected")
        else:
            self._age_days = new_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def show(self) -> None:
        print(f"Plant created: {self._name}: {round(self._height, 1)}cm, "
              f"{self._age_days} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose: Plant = Plant("Rose", round(25.0, 1), 30)
    rose.show()
    rose.set_age(60)
    rose._age_days = -19
    rose.set_height(35.0)
    print(f"\nHeight updated: {rose.get_height()}cm")
    print(f"Age updated: {rose.get_age()} days\n")
    rose.set_age(-60)
    rose.set_height(-35)
    print(f"\nCurrent state: {rose._name}: "
          f"{rose.get_height()}cm, {rose.get_age()} days old")
