

def secure_archive(filename: str, auth: str = 'r', content: str = "")\
      -> tuple[bool, str]:
    try:
        if auth == 'r':
            with open(filename, auth) as file:
                content = file.read()
                return (True, content)
        elif auth == 'w':
            with open(filename, auth) as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, "Wrong parameter you can only read or write")
    except (PermissionError, FileNotFoundError, IsADirectoryError) as err:
        return (False, str(err))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("Using ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("test1"))
    print("\nUsing ’secure_archive’ to read from an inaccessible file:")
    print(secure_archive("test2"))
    print("\nUsing ’secure_archive’ to read from a regular file:")
    print(secure_archive("test3"))
    print("\nUsing ’secure_archive’ to write previous content to a new file:")
    print(secure_archive("test4", 'w', "Git Gud"))
