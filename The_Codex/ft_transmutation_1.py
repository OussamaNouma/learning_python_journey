import alchemy.transmutation

gold = alchemy.transmutation.recipes

if __name__ == "__main__":
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {gold.lead_to_gold()}")
