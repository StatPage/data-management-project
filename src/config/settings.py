import os
from pathlib import Path


def get_proj_root():
    """Returns the path of project root directory

    Returns:
        str: text sequence type (strings) of the path of project root directory
    """
    return (
        # os.path.dirname(Path(__file__).resolve())
        # TODO: update project root path
        os.path.dirname(Path(__file__).resolve().parent)
        # os.path.dirname(Path(__file__).resolve().parents[1])
        if "__file__" in locals() or "__file__" in globals()
        # NOTICE: The current working directory should be the project root folder in Python Terminal
        else os.path.dirname(os.path.realpath("__file__"))
    )


PROJ_ROOT = get_proj_root()

if __name__ == "__main__":
    print(f"PROJ_ROOT: {PROJ_ROOT}")