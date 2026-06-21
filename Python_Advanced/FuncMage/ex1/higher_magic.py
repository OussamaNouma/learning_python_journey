from collections.abc import Callable
from typing import TypeAlias

SpellFunc: TypeAlias = Callable[[str, int], str]
SpellBool: TypeAlias = Callable[[str, int], bool]
CombReturn: TypeAlias = Callable[[str, int], tuple[str, str]]
SeqReturn: TypeAlias = Callable[[str, int], list[str]]


def spell_combiner(spell1: SpellFunc, spell2: SpellFunc) -> CombReturn:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: SpellFunc, multiplier: int) -> SpellFunc:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: SpellBool, spell: SpellFunc) -> SpellFunc:
    def call_me_maybe(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return call_me_maybe


def spell_sequence(spells: list[SpellFunc]) -> SeqReturn:
    def armagedon(target: str, power: int) -> list[str]:
        return list(map(lambda x: x(target, power), spells))
    return armagedon


def crystal_soul_spear(target: str, power: int) -> str:
    return (f"Crystal Soul Spear and hit {target} dealing {power} damages")


def soothing_sunlight(target: str, power: int) -> str:
    return (f"Soothing Sunlight to heal {target} by {power} health")


def sunlight_spear(target: str, power: int) -> str:
    return (f"Sunlight Spear and hit {target} dealing {power} damages")


def power_checker(target: str, power: int) -> bool:
    return power >= 40 and target == "Pinwheel"


if __name__ == "__main__":
    combined_spells: CombReturn = spell_combiner(soothing_sunlight,
                                                 sunlight_spear)
    sooth, attack = combined_spells("The Chosen Undead", 800)
    solaire: str = "Solaire of astora uses "
    bgl: str = "Big Hat Logan uses "
    print(f"""Testing spell combiner...
Combined spell result: {solaire}{sooth}, {solaire}{attack}
""")
    original_power = 300
    multiplier = 5
    amplified_spell = power_amplifier(sunlight_spear, multiplier)
    result = amplified_spell("Sir Alonne", original_power)
    print(f"""Testing power amplifier...
The Bearer of the Curse has eaten a bright bug
Power temporarily increases by {multiplier} times
The Bearer of the Curse uses {result}
Original power: {original_power}
Amplified power: {original_power * multiplier}
""")

    cond: SpellFunc = conditional_caster(power_checker, crystal_soul_spear)
    print(f"""Testing conditional caster...
{cond("Pinwheel", 20)}
{bgl}{cond("Pinwheel", 1400)}
Pinwheel has been one shotted
""")
    spells: list[SpellFunc] = [
        crystal_soul_spear,
        soothing_sunlight,
        sunlight_spear
    ]
    print("Testing sequence caster...")
    chaos: SeqReturn = spell_sequence(spells)
    res_chaos: list[str] = chaos("The Chosen Undead", 800)
    for x in res_chaos:
        print(f"Trusty Patches uses {x}")
