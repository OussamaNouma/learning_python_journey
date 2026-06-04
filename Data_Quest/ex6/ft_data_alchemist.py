import random

if __name__ == "__main__":
    names: list[str] = [
        "Solaire",
        "Havel",
        "Siegmeyer",
        "Laurentius",
        "orstein",
        "smough",
        "Logan",
        "gough",
        "artorias"
    ]
cap_names: list[str] = [name.capitalize() for name in names]
only_cap: list[str] = [name for name in names if name == name.capitalize()]
scores: dict[str, int] = {key: random.randint(50, 1000) for key in cap_names}
print("=== Game Data Alchemist ===")
print(f"Initial list of players: {names}")
print(f"New list with all names capitalized: {cap_names}")
print(f"New list of capitalized names only: {only_cap}")
print(f"Score dict: {scores}")
sum: int = sum(scores.values())
average: float = round(sum/len(scores), 2)
print(f"Score average is {average}")
s: dict[str, int] = {k: v for k, v in scores.items() if v > average}
print(f"High scores: {s}")
