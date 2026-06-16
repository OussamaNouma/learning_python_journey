import importlib as lb
import importlib.metadata as md


def check_for_dependencies() -> bool:
    dependencies: list[str] = ["pandas", "numpy",
                               "matplotlib"]
    success: bool = True
    for x in dependencies:
        try:
            lb.import_module(x)
            summary = md.metadata(x)["Summary"]
            print(f"[OK] {x} {md.version(x)} - {summary}")
        except ImportError as err:
            print(f"[KO] {err} - Install it with pip3 install {x}"
                  f"or Install it with poetry add {x}")
            success = False
    return success


if __name__ == "__main__":
    print("""LOADING STATUS: Loading programs...
Checking dependencies:""")
    if check_for_dependencies():
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt  # type: ignore
        player_hp: np.ndarray = np.random.randint(50, 250, size=1000)
        boss_hp: np.ndarray = np.random.randint(350, 650, size=1000)
        success_rate: np.ndarray = \
            np.round(((player_hp + 100) / boss_hp) * 100, 1)
        result = np.column_stack((player_hp, boss_hp, success_rate))
        frame = pd.DataFrame(result,
                             columns=["Player_hp",
                                      "Boss_hp", "Success_rate"])
        print("""\nAnalyzing Matrix data...
Processing 1000 data points...
Generating visualization...\n""")
        plt.scatter(frame["Player_hp"], frame["Success_rate"],
                    s=10, c=frame["Boss_hp"], cmap="plasma")
        plt.colorbar(label="Boss HP")
        plt.title("Player vs Boss")
        plt.xlabel("Player Health")
        plt.ylabel("Win rate")
        plt.savefig("matrix_analysis.png")
        print("""Analysis complete!
Results saved to: matrix_analysis.png""")
