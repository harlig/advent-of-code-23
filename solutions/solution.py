import inspect
from pathlib import Path
from typing import Optional


class Solution:
    def __init__(self, input_file: Optional[str] = "input.txt") -> None:
        self.input_file_path: Path = self.get_input_file_path(input_file)
        self.input_data: list[str] = self.read_input()

    def get_input_file_path(self, input_file: str) -> Path:
        # Get the path of the derived class
        derived_class_file = inspect.getfile(self.__class__)
        derived_class_path = Path(derived_class_file).parent
        return derived_class_path / input_file

    def read_input(self) -> list[str]:
        with open(self.input_file_path, "r") as file:
            return [line.strip() for line in file.readlines()]

    def solve(self) -> str:
        raise NotImplementedError("Solve method must be implemented by subclasses.")
