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
        try:
            f: typing.IO[str] = open(sys.argv[1], "r")
        except FileNotFoundError as err:
            raise FileNotFoundError(f"Error opening file "
                                    f"’{sys.argv[1]}’: {err}")
        except PermissionError as err:
            raise PermissionError(f"Error opening file ’{sys.argv[1]}’: {err}")
        to_print: str = f.read()
        print(f"---\n{to_print}\n---")
        f.close()
        print(f"File ’{sys.argv[1]}’ closed.")
        transformed: list[str] = [line + "#" for line in to_print.splitlines()]
        new_data: str = "\n".join(transformed)
        if to_print.endswith("\n"):
            new_data += "\n#"
        print(f"Transform data:\n---\n{new_data}\n---")
        print("Enter new file name (or empty): ", end='')
        sys.stdout.flush()
        f_name = sys.stdin.readline().strip("\n")
        if not f_name:
            raise ValueError("Not saving data.")
        print(f"Saving data to {f_name}")
        try:
            new_f: typing.IO[str] = open(f_name, "w")
        except FileNotFoundError as err:
            raise FileNotFoundError(f"Error opening file ’{f_name}’: {err}")
        except PermissionError as err:
            raise PermissionError(f"Error opening file ’{f_name}’: {err}")
        new_f.write(new_data)
        print(f"Data saved in file {f_name}.")
        new_f.close()
        print(f"File ’{f_name}’ closed.")
    except (FileNotFoundError, PermissionError, ValueError) as err:
        sys.stderr.write(f"[STDERR] {err}\n")
