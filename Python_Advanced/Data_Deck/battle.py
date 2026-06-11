from ex0 import AquaFactory
from ex0 import FlameFactory

if __name__ == "__main__":
    print("Testing factory")
    fire_base = FlameFactory().create_base()
    print(fire_base.describe())
    print(fire_base.attack())
    fire_evolved = FlameFactory().create_evolved()
    print(fire_evolved.describe())
    print(fire_evolved.attack())

    print("\nTesting factory")
    water_base = AquaFactory().create_base()
    print(water_base.describe())
    print(water_base.attack())
    water_evolved = AquaFactory().create_evolved()
    print(water_evolved.describe())
    print(water_evolved.attack())

    print("\nTesting battle")
    print(fire_base.describe())
    print("vs.")
    print(water_base.describe())
    print("fight!")
    print(fire_base.attack())
    print(water_base.attack())
