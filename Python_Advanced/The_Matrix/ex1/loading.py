import importlib as lb
import importlib.metadata as md


def check_for_dependencies() -> bool:
    dependencies: list[str] = ["pandas", "numpy", "requests", "matplotlib"]
    success: bool = True
    for x in dependencies:
        try:
            lib = lb.import_module(x)
            print(f"[OK] {x} {md.version(x)} - {md.metadata(x)["Summary"]}")
        except ImportError as err:
            print(f"[KO] {err} - Install it with pip3 install {x}")
            success = False
        else:
            globals()[x] = lib
    return success


check_for_dependencies()


def data_generator() -> None:
    np = numpy