#!/usr/bin/env python3
import sys
import typing

if __name__ == "__main__":
    f_name: str = ""
    try:
        if len(sys.argv) == 1 or len(sys.argv) > 2:
            raise ValueError("Usage: ft_ancient_text.py <file>")
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file ’{sys.argv[1]}’")
        f: typing.IO[str] = open(sys.argv[1], "r")
        to_print: str = f.read()
        print(f"---\n{to_print}\n---")
        f.close()
        print(f"File ’{sys.argv[1]}’ closed.")
        transformed: list[str] = [line + "#" for line in to_print.splitlines()]
        new_data: str = "\n".join(transformed)
        if to_print.endswith("\n"):
            new_data += "\n#"
        print(f"Transform data:\n---\n{new_data}\n---")
        f_name = input("Enter new file name (or empty): ")
        if not f_name:
            raise ValueError("Not saving data.")
        print(f"Saving data to {f_name}")
        new_f: typing.IO[str] = open(f_name, "w")
        new_f.write(new_data)
        print(f"Data saved in file {f_name}.")
        new_f.close()
        print(f"File ’{f_name}’ closed.")
    except (FileNotFoundError, PermissionError, ValueError) as err:
        if len(sys.argv) == 1:
            print(err)
        elif not f_name:
            print(err)
        else:
            print(f"Error opening file ’{sys.argv[1]}’: {err}")
