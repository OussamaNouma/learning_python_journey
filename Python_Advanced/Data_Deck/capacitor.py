from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory

if __name__ == "__main__":
    print("Testing Creature with healing capability\nbase:")
    heal_base = HealingCreatureFactory().create_base()
    print(heal_base.describe())
    print(heal_base.attack())
    print(heal_base.heal())
    print("evolved:")
    heal_evolved = HealingCreatureFactory().create_evolved()
    print(heal_evolved.describe())
    print(heal_evolved.attack())
    print(heal_evolved.heal())

    print("\nTesting Creature with transform capability\nbase:")
    shift_base = TransformCreatureFactory().create_base()
    print(shift_base.describe())
    print(shift_base.attack())
    print(shift_base.transform())
    print(shift_base.attack())
    print(shift_base.revert())
    print("evolved:")
    shift_evolved = TransformCreatureFactory().create_evolved()
    print(shift_evolved.describe())
    print(shift_evolved.attack())
    print(shift_evolved.transform())
    print(shift_evolved.attack())
    print(shift_evolved.revert())
