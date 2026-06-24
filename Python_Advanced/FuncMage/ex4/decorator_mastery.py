from functools import wraps
from collections.abc import Callable
from time import time, sleep
from typing import Any, TypeAlias, cast
Fn: TypeAlias = Callable[..., Any]


def spell_timer(func: Fn) -> Fn:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start: float = time()
        result = func(*args, **kwargs)
        print(f"Spell completed in {round(time() - start, 3)} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[[Fn], Fn]:
    def decorator(func: Fn) -> Fn:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if (args[0] < min_power):
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[[Fn], Fn]:
    def decorator(func: Fn) -> Fn:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            i = 1
            while i <= max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(f"Spell failed, retrying..."
                          f" (attempt {i}/{max_attempts})")
                    i += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(i.isalpha() or i == ' ' for i in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(min_power=10)
        def inner(power: int) -> str:
            return f"Successfully cast {spell_name} with {power} power"
        return cast(str, inner(power))


@spell_timer
def kamehameha() -> str:
    sleep(1)
    print("KAAAAAAA... MEEEEEEEEEEE...")
    sleep(2)
    print("HHAAAAAA... ")
    sleep(1.5)
    print("MEEEEEEEEEEEEEE...")
    sleep(3)
    print("HAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!")
    sleep(1)
    return ("Kamehameha")


@power_validator(min_power=300)
def super_saiyan_rage(power: int) -> str:
    print("OORRRRH NOOON")
    sleep(0.5)
    print("COMMENT OSE-TU ????")
    sleep(1)
    print("FRAPPER MA BULMAAAAAAAAAARGGGGGGGHHHHHH !!!!")
    sleep(1)
    return ("Vegeta super saiyan rage")


class UltraInstinct:
    def __init__(self) -> None:
        self.attempts = 0

    def __call__(self, power: int) -> str:
        self.attempts += 1
        if self.attempts < 5:
            raise ValueError
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAARGHHH!!!")
        return "Ultra Instinct"


ultra_instinct_obj = UltraInstinct()


@retry_spell(max_attempts=8)
def ultra_instinct(power: int) -> str:
    return ultra_instinct_obj(power)


if __name__ == "__main__":
    print("Testing spell timer...")
    spell = kamehameha()
    print(f"Result: {spell} casted")
    print("\nTesting with invalid power in power validator...")
    rage1 = super_saiyan_rage(200)
    print(rage1)
    print("\nTesting with valid power in power validator...")
    rage2 = super_saiyan_rage(200000000)
    print(f"Result: {rage2}")
    print("\nTesting retrying spell..")
    print("Goku tries to go ultra instinct")
    ul = ultra_instinct(100)
    print(f"Goku goes {ul}")
    print("\nTesting mage guild..")
    mage: MageGuild = MageGuild()
    print(mage.validate_mage_name("Babidi"))
    print(mage.validate_mage_name("Bu"))
    print(mage.cast_spell('Mind Control', 8))
    print(mage.cast_spell('Mind Control', 100))
