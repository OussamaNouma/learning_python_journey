from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["arsenic", "bats", "frogs", "eyball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    response: str = validate_ingredients(ingredients)
    if response.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({response})"
    return f"Spell rejected: {spell_name} ({response})"
