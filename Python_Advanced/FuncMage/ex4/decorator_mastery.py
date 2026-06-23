from functools import wraps
from collections.abc import Callable
from time import time
from typing import Any, TypeAlias
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
