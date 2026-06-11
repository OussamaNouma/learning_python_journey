from .elements import create_air
from .elements import create_earth
from elements import create_fire
from elements import create_water


def healing_potion():
    return (f"Healing potion brewed with "
            f"'{create_earth()}' and '{create_air()}'")


def strength_potion():
    return (f"Strength potion brewed with "
            f"'{create_fire()}' and '{create_water()}'")
