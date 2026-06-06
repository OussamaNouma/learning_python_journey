#!/usr/bin/env python3
import sys
import typing

if __name__ == "__main__":
    try:
        if len(sys.argv) == 1 or len(sys.argv) > 2:
            raise ValueError("Usage: ft_ancient_text.py <file>")
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file ’{sys.argv[1]}’")
        f: typing.IO[str] = open(sys.argv[1], "r")
        to_print = f.read()
        print(f"---\n{to_print}\n---")
        f.close()
        print(f"File ’{sys.argv[1]}’ closed.")
    except (FileNotFoundError, PermissionError, ValueError) as err:
        if len(sys.argv) == 1:
            print(err)
        else:
            print(f"Error opening file ’{sys.argv[1]}’: {err}")
