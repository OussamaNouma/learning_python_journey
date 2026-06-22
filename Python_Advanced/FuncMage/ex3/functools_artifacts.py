from functools import reduce, partial, lru_cache, singledispatch
import operator
from collections.abc import Callable
from typing import Any, TypeAlias

enchant_type: TypeAlias = Callable[..., Any]
enchant_return: TypeAlias = dict[str, Callable[..., Any]]


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations: dict[str, Callable[..., Any]] = {
        'add': operator.add,
        'multiply': operator.mul,
        'min': min,
        'max': max
    }
    try:
        op = operations[operation]
        return reduce(op, spells)
    except KeyError as err:
        raise ValueError(f"Unknown operation: {operation}") from err


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element.capitalize()} enchantment (+{power}) on {target}"


def partial_enchanter(base_enchantment: enchant_type) -> enchant_return:
    enchants: dict[str, enchant_type] = {
        'fire': partial(base_enchantment, power=50, element='fire'),
        'water': partial(base_enchantment, power=50, element='water'),
        'dragon': partial(base_enchantment, power=50, element='dragon')
    }
    return enchants


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def _(spell: int) -> str:
        return f"{spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return f"{spell}"

    @cast.register
    def _(spell: list) -> str:  # type: ignore[type-arg]
        return f"{len(spell)} spells"

    return cast


if __name__ == "__main__":
    spell_powers = [27, 41, 18, 20, 21, 43]
    fib = memoized_fibonacci
    enchants = partial_enchanter(base_enchantment)
    cast = spell_dispatcher()
    print(f"""
Testing spell reducer...
Sum: {spell_reducer(spell_powers, 'add')}
Product: {spell_reducer(spell_powers, 'multiply')}
Max: {spell_reducer(spell_powers, 'max')}
Min: {spell_reducer(spell_powers, 'min')}

Testing partial enchanter...
{enchants['fire'](target="Sword")}
{enchants['water'](target="Shield")}
{enchants['dragon'](target="Lance")}

Testing memoized fibonacci...
Fib(0): {fib(0)}
Fib(1): {fib(1)}
Fib(10): {fib(10)}
Fib(15): {fib(15)}
Cache stat: {memoized_fibonacci.cache_info()}

Testing spell dispatcher...
Damage spell: {cast(42)}
Enchantment: {cast('Sunlight spear')}
Multi-cast: {cast(['fireball', 'Dragon wrath', 'heal'])}
{cast(None)}""")
