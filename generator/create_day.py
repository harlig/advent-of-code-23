from pathlib import Path
import os
from typing import NoReturn


class SolutionDirectoryCreator:
    def __init__(self, day: str) -> None:
        self.day: str = day
        self.base_path: str = "../solutions/days"

    def create_directories(self) -> NoReturn:
        day_path_str = f"{self.base_path}/{self.day}"
        print(f"Creating day directory of {day_path_str}")
        day_path = Path(day_path_str)
        day_path.mkdir(parents=True, exist_ok=True)
        self.create_init_file(day_path)
        self.create_boilerplate_file(day_path)
        self.create_input_files(day_path)

    @staticmethod
    def create_init_file(path: Path) -> None:
        print(f"Creating init file for path {path}")
        init_file_path = path / "__init__.py"
        init_file_path.touch(exist_ok=True)

    @staticmethod
    def create_boilerplate_file(path: Path) -> None:
        print(f"Creating boilerplate file for path {path}")
        boilerplate_code = """from solutions.solution import Solution


class DaySolution(Solution):
    def solve_part_one(self) -> str:
        print(self.input_data)
        return str("change me pls")

    def solve_part_two(self) -> str:
        print(self.input_data)
        return str("change me pls")


if __name__ == "__main__":
    today_solution = DaySolution("input0.txt")
    print("running part one")
    part_one = today_solution.solve_part_one()
    print("part one results:")
    print(part_one)

    # enable once part one solved
    # print("running part two")
    # part_two = today_solution.solve_part_two()
    # print("part two results:")
    # print(part_two)
"""
        with open(os.path.join(path, "solution.py"), "w") as file:
            file.write(boilerplate_code)

    @staticmethod
    def create_input_files(path: Path) -> None:
        print(f"Creating input files for path {path}")
        for input_file_number in range(3):
            input_file_path = path / f"input{input_file_number}.txt"
            input_file_path.touch(exist_ok=True)


def create_solution_directory(day: str) -> None:
    creator = SolutionDirectoryCreator(day)
    creator.create_directories()
