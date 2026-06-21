from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    accumulator = initial_power

    def counter(power: int) -> int:
        nonlocal accumulator
        accumulator += power
        return accumulator
    return counter


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchanter(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchanter


def memory_vault() -> dict[str, Callable[..., Any]]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value
        return None

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("Testing mage counter...")
    for x in range(1, 4):
        print(f"counter_a call {x}: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting spell accumulator...")
    base = 100
    acc_a = spell_accumulator(base)
    print(f"""base {base}, add 20: {acc_a(20)}
base {base}, add 30: {acc_a(30)}
""")
    print("Testing enchantment factory...")
    weapon = enchantment_factory('Sunlight')
    shield = enchantment_factory('Magic')
    print(weapon('Blade'))
    print(shield('Shield'))
    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('Secret', 'Hit the wall')
    print("'Store' 'Secret' = 'Hit the wall'")
    print(f"'Recall' 'Secret': {vault['recall']('Secret')}")
    print(f"'Recall' 'unknown': {vault['recall']('unknown')}")
