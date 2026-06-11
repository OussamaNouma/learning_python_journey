import sys

if __name__ == "__main__":
    size: int = len(sys.argv)
    inventory: dict[str, int] = {}
    print("=== Inventory System Analysis ===")

    for i in range(1, size):
        try:
            tmp: list[str] = sys.argv[i].split(":")
            if len(tmp) != 2:
                raise ValueError(f"Error - invalid parameter {sys.argv[i]}")
            if tmp[0] in inventory:
                raise ValueError(f"Redundant item {tmp[0]} - discarding")
            try:
                inventory[tmp[0]] = int(tmp[1])
            except ValueError as err:
                raise ValueError(f"Quantity error for {tmp[0]}: {err}")
        except ValueError as err:
            print(err)
    size_inv: int = len(inventory)
    items_name: list[str] = list(inventory.keys())
    items_value: list[int] = list(inventory.values())
    total_items: int = sum(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list : {items_name}")
    print(f"Total quantity of the {size_inv} "
          f"items : {total_items}")
    for i in range(len(items_name)):
        percentage: float = round(items_value[i] / total_items * 100, 1)
        print(f"Item {items_name[i]} represents {percentage}%")
    item_max: str = max(inventory, key=inventory.__getitem__)
    item_min: str = min(inventory, key=inventory.__getitem__)
    print(f"Item most abundant: "
          f"{item_max} with quantity {inventory[item_max]}")
    print(f"Item least abundant: "
          f"{item_min} with quantity {inventory[item_min]}")
    inventory.update({"Estus": 4})
    print(f"Updated inventory: {inventory}")
