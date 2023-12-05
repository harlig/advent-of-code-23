from pathlib import Path
import os
from typing import NoReturn


class SolutionDirectoryCreator:
    def __init__(self, day: str) -> None:
        self.day: str = day
        self.base_path: str = "../solutions/days/"

    def create_directories(self) -> NoReturn:
        day_path = self.base_path / self.day
        day_path.mkdir(parents=True, exist_ok=True)
        self.create_init_file(day_path)

        for part in ["1", "2"]:
            part_path = day_path
            part_path.mkdir(parents=True, exist_ok=True)
            self.create_init_file(part_path)
            self.create_boilerplate_file(part_path)

    @staticmethod
    def create_init_file(path: Path) -> None:
        init_file_path = path / "__init__.py"
        init_file_path.touch(exist_ok=True)

    @staticmethod
    def create_boilerplate_file(path: str) -> None:
        boilerplate_code = """
# Boilerplate Python code for solution

def solution():
    # TODO: Implement the solution here
    pass
"""
        with open(os.path.join(path, "solution.py"), "w") as file:
            file.write(boilerplate_code)


def create_solution_directory(day: str) -> None:
    creator = SolutionDirectoryCreator(day)
    creator.create_directories()
