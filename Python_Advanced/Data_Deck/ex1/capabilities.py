import abc
from ex0 import Creature
from ex0 import CreatureFactory


class HealCapability(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def heal(self, target: str = "itself") -> str:
        pass


class TransformCapability(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.flag = False

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Sproutling"
        self.type = "Grass"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!!"

    def heal(self, target: str = "itself") -> str:
        return f"{self.name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Bloomelle"
        self.type = "Grass/Fairy"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str = "itself and others") -> str:
        return f"{self.name} heals {target} for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Shiftling"
        self.type = "Normal"

    def attack(self) -> str:
        if self.flag is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.flag = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.flag = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Morphagon"
        self.type = "Normal/Dragon"

    def attack(self) -> str:
        if self.flag is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.flag = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.flag = False
        return f"{self.name} stabilizes its form"


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
