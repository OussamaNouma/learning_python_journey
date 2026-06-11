from ex0 import CreatureFactory
from ex0 import AquaFactory
from ex0 import FlameFactory
from ex0 import Creature
from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory
from ex2 import BattleStrategy
from ex2 import AggressiveStrategy
from ex2 import NormalStrategy
from ex2 import DefensiveStrategy
from ex2 import IncompatibleStratCreature


def duel(creatures: list[tuple[CreatureFactory,
                               BattleStrategy]]) -> None:
    print("*** Tournament ***")
    size_c: int = len(creatures)
    print(f"{size_c} opponents involved\n")
    print("* Battle *")
    for n in range(size_c):
        for x in range(n + 1, size_c):
            first: Creature = creatures[n][0].create_base()
            second: Creature = creatures[x][0].create_base()
            print(first.describe())
            print("vs.")
            print(second.describe())
            try:
                act_one: str = creatures[n][1].act(first)
                act_two: str = creatures[x][1].act(second)
                print(f"{act_one}\n{act_two}")
            except IncompatibleStratCreature as err:
                print(f"Battle error, aborting tournament: {err}")


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    duel([(FlameFactory(), NormalStrategy()),
          (HealingCreatureFactory(), DefensiveStrategy())])
    print("\nTournament 1 (error)\n")
    duel([(FlameFactory(), AggressiveStrategy()),
          (HealingCreatureFactory(), DefensiveStrategy())])
    print("Tournament 2 (basic)")
    duel([(AquaFactory(), NormalStrategy()),
          (HealingCreatureFactory(), DefensiveStrategy()),
          (TransformCreatureFactory(), AggressiveStrategy())])
