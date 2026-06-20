#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict[str, int | str]])\
      -> list[dict[str, int | str]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict[str, int | str]], min_power: int)\
      -> list[dict[str, int | str]]:
    return list(filter(lambda x: int(x['power']) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, int | str]])\
      -> dict[str, int | float]:
    strongest = max(mages, key=lambda x: x['power'])
    weakest = min(mages, key=lambda x: int(x['power']))
    average = sum(map(lambda x: int(x['power']), mages)) / len(mages)

    stats: dict[str, int | float] = {
        "max_power": int(strongest['power']),
        "min_power": int(weakest['power']),
        "avg_power": round(average, 2)
    }
    return stats


if __name__ == "__main__":
    artifacts: list[dict[str, int | str]] = [
        {"name": "Light Prism", "power": 115, "type": "focus"},
        {"name": "Light Prism", "power": 71, "type": "focus"},
        {"name": "Shadow Blade", "power": 101, "type": "focus"},
        {"name": "Water Chalice", "power": 82, "type": "relic"},
    ]
    mages: list[dict[str, int | str]] = [
        {"name": "River", "power": 63, "element": "water"},
        {"name": "Casey", "power": 63, "element": "lightning"},
        {"name": "Storm", "power": 79, "element": "ice"},
        {"name": "Phoenix", "power": 58, "element": "water"},
        {"name": "Rowan", "power": 85, "element": "fire"},
    ]
    spells: list[str] = ["earthquake", "tornado", "flash", "blizzard"]
    sorted_art: list[dict[str, int | str]] = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(f"{sorted_art[0]['name']} ({sorted_art[0]['power']} power)"
          f" comes before {sorted_art[1]['name']}"
          f" ({sorted_art[1]['power']} power)")

    print("\nFiltering mages above 65 power...")
    strongest: list[dict[str, int | str]] = power_filter(mages, 65)
    for x in strongest:
        print(f"{x['name']} is a {x['element']} mage with {x['power']} power")

    print("\nTesting spell transformer...")
    print(*spell_transformer(spells))

    stats: dict[str, int | float] = mage_stats(mages)
    print(f"""\nChecking mage stats...
The strongest mage possess: {stats['max_power']}
The weakest mage possess: {stats['min_power']}
The Average power is : {stats['avg_power']}
""")
