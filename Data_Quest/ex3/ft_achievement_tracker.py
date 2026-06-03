import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    n: int = random.randint(4, len(achievements))
    return set(random.sample(achievements, n))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    achievements: list[str] = [
        "Crafting Genius", "Strategist", "WorldSavior",
        "Speed Runner", "Survivor", "Master Explorer",
        "Treasure Hunter", "Unstoppable", "First Steps",
        "Collector Supreme", "Untouchable",
        "Sharp Mind", "Boss Slayer", "Hidden Path Finder"
    ]
    player_names: list[str] = ["Solaire", "Siegmeyer", "Lautrec", "Havel"]
    p_achivements: list[set[str]] = []
    for i in range(len(player_names)):
        p_achivements.append(gen_player_achievements(achievements))

    for i in range(len(player_names)):
        print(f"Player {player_names[i]}: {p_achivements[i]}")

    print(f"All distinct achievements: "
          f"{p_achivements[0].union(*p_achivements[1:])}")

    print(f"Common achievements: "
          f"{p_achivements[0].intersection(*p_achivements[1:])}")

    for i in range(len(player_names)):
        rest: list[set[str]] = p_achivements[:i] + p_achivements[i + 1:]
        print(f"Only {player_names[i]}: "
              f"{p_achivements[i].difference(*(rest))}")

    for i in range(len(player_names)):
        print(f"{player_names[i]} is missing: "
              f"{set(achievements).difference(p_achivements[i])}")
