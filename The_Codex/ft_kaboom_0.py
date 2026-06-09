import alchemy.grimoire

if __name__ == "__main__":
    light = alchemy.grimoire
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: "
          f"{light.light_spell_record("Fantasy", "Earth, wind and fire")}")
