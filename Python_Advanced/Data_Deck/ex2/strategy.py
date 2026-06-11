import abc
import typing
from ex0 import Creature
from ex1 import TransformCapability
from ex1 import HealCapability


class IncompatibleStratCreature(Exception):
    def __init__(self, name: str) -> None:
        self.name = name
        self.message = (f"Invalid Creature '{self.name}' "
                        f"for this aggressive strategy")
        super().__init__(self.message)


class TransformProtocol(typing.Protocol):
    name: str

    def attack(self) -> str:
        pass

    def transform(self) -> str:
        pass

    def revert(self) -> str:
        pass


class HealProtocol(typing.Protocol):
    name: str

    def attack(self) -> str:
        pass

    def heal(self, target: str = "itself and others") -> str:
        pass


class BattleStrategy(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> str:
        return f"{creature.attack()}"

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        transformed: TransformProtocol = \
            typing.cast(TransformProtocol, creature)
        if self.is_valid(creature):
            return (f"{transformed.transform()}\n{transformed.attack()}"
                    f"\n{transformed.revert()}")
        else:
            raise IncompatibleStratCreature(creature.name)


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        healed: HealProtocol = \
            typing.cast(HealProtocol, creature)
        if self.is_valid(creature):
            return (f"{healed.attack()}\n{healed.heal()}")
        else:
            raise IncompatibleStratCreature(healed.name)
