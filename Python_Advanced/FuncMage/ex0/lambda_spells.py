#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict[str, int | str]])\
      -> list[dict[str, int | str]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict[str, int | str]], min_power: int)\
      -> list[dict[str, int | str]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, int | str]])\
      -> dict[str, int | float]:
    strongest = max(mages, key=lambda x: x['power'])
    weakest = min(mages, key=lambda x: x['power'])
    average = sum(map(lambda x: x['power'], mages)) / len(mages)

    stats: dict[str, int | float] = {
        "max_power": strongest['power'],
        "min_power": weakest['power'],
        "avg_power": round(average, 2)
    }
    return stats


if __name__ == "__main__":
    artifacts = [
        {"name": "Light Prism", "power": 115, "type": "focus"},
        {"name": "Light Prism", "power": 71, "type": "focus"},
        {"name": "Shadow Blade", "power": 101, "type": "focus"},
        {"name": "Water Chalice", "power": 82, "type": "relic"},
    ]
    mages = [
        {"name": "River", "power": 63, "element": "water"},
        {"name": "Casey", "power": 63, "element": "lightning"},
        {"name": "Storm", "power": 79, "element": "ice"},
        {"name": "Phoenix", "power": 58, "element": "water"},
        {"name": "Rowan", "power": 85, "element": "fire"},
    ]
    spells = ["earthquake", "tornado", "flash", "blizzard"]
    sorted_art: list[dict[str, int | str]] = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(f"{sorted_art[0]['name']} ({sorted_art[0]['power']} power)"
          f" comes before {sorted_art[1]['name']}"
          f"({sorted_art[1]['power']} power)")
    
