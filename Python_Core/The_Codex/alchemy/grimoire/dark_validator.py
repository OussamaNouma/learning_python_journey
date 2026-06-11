from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lst_cmp: list[str] = dark_spell_allowed_ingredients()
    if any(x in ingredients.lower() for x in lst_cmp):
        return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
