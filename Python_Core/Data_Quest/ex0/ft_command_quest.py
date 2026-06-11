import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if (len(sys.argv) > 1):
        print(f"Arguments received: {len(sys.argv) - 1}")
        for x in range(1, len(sys.argv)):
            print(f"Argument {x}: {sys.argv[x]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print("No arguments provided!")
        print("Total arguments: 1")
