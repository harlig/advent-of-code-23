import os
from typing import NoReturn


class SolutionDirectoryCreator:
    def __init__(self, day: str) -> None:
        self.day: str = day
        self.base_path: str = "../solutions/days/"

    def create_directories(self) -> NoReturn:
        # Create the main directory for the day
        day_path = os.path.join(self.base_path, self.day)
        os.makedirs(day_path, exist_ok=True)

        print(f"Made directory at {day_path} {self.day}")

        # Create subdirectories for parts 'one' and 'two'
        for part in ["one", "two"]:
            part_path = os.path.join(day_path, part)
            os.makedirs(part_path, exist_ok=True)
            self.create_boilerplate_file(part_path)

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
