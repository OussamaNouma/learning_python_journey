def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    lst_cmp: list[str] = light_spell_allowed_ingredients()
    if any(x in ingredients.lower() for x in lst_cmp):
        return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
