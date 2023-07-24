import os
from pathlib import Path


def get_proj_root():
    return (
        os.path.dirname(Path(__file__).resolve().parent)
        if "__file__" in locals() or "__file__" in globals()
        # NOTICE: The current working directory should be the project root folder in Python Terminal
        else os.path.dirname(os.path.realpath("__file__"))
    )


PROJ_ROOT = get_proj_root()

if __name__ == "__main__":
    print(f"PROJ_ROOT: {PROJ_ROOT}")