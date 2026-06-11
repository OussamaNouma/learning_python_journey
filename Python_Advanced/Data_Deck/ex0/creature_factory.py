import abc


class Creature(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = ""
        self.type: str = ""

    @abc.abstractmethod
    def attack(self) -> str:
        return ""

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class CreatureFactory(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def create_base(self) -> Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        pass


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Flameling"
        self.type = "Fire"

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pyrodon"
        self.type = "Fire/Flying"

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Aquabub"
        self.type = "Water"

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Torragon"
        self.type = "Water"

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
