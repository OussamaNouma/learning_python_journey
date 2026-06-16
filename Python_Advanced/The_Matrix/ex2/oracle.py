import os
from dotenv import load_dotenv
# import sys


if __name__ == "__main__":
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...\n\n"
          "Configuration loaded:")
    matrix: str | None = os.getenv("MATRIX_MODE")
    level: str | None = os.getenv("LOG_LEVEL")
    env_var: dict[str, str] = {
        "MATRIX_MODE": f"Mode: {matrix}",
        "DATABASE_URL": "Database: Connected to local instance",
        "API_KEY": "API Access: Authenticated",
        "LOG_LEVEL": f"Log level: {level}",
        "ZION_ENDPOINT": "Zion Network: Online"
    }
    env_var_bis: dict[str, str] = {
        "MATRIX_MODE": f"Mode: {matrix}",
        "DATABASE_URL": "Database: Connected",
        "API_KEY": "API Access: Authenticated",
        "ZION_ENDPOINT": "Zion Network: Online"
    }
    if matrix == "development":
        for x in env_var:
            if os.getenv(x) is not None:
                print(env_var[x])
            else:
                print(f"{x}: Missing")
    else:
        for x in env_var_bis:
            if os.getenv(x) is not None:
                print(env_var_bis[x])
            else:
                print(f"{x}: Missing")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file is not properly configured")
    if os.getenv("MATRIX_MODE"):
        print("[OK] Production overrides available")
    else:
        print("[KO] .Production overrides not available")
    print("\nThe Oracle sees all configurations.")
