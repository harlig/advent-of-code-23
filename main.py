import importlib
import argparse
import datetime
import sys
from generator import create_day
from typing import Optional
import importlib.util

from solutions.solution import Solution


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Main script to create or run solutions."
    )
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create")
    create_parser.add_argument(
        "-d", "--day", type=int, help="Day of the month for solution creation"
    )

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument(
        "-d", "--day", type=int, required=True, help="Day of the solution to run"
    )
    run_parser.add_argument(
        "-p", "--part", type=int, required=True, help="Part of the solution to run"
    )
    run_parser.add_argument("-i", "--input", type=int, help="Input file number")

    args = parser.parse_args()

    if args.command == "create":
        handle_create(args.day)
    elif args.command == "run":
        handle_run(args.day, args.part, args.input)
    else:
        parser.print_help()


def handle_create(day: Optional[int]) -> None:
    if day is None:
        day = datetime.datetime.now().day
    if not (1 <= day <= 31):
        sys.exit("Error: Invalid day. Please provide a day between 1 and 31.")

    create_day.create_solution_directory(str(day))


def handle_run(day: int, part: int, input_number: Optional[int] = None) -> None:
    module_name = f"solutions.days.{day}.solution"
    class_name = "PartSolution"

    input_file = f"input{input_number}.txt" if input_number is not None else "input.txt"

    try:
        module = importlib.import_module(module_name)

        solution_class = getattr(module, class_name)
        solution_instance: Solution = solution_class(input_file)

        solution = (
            solution_instance.solve_part_one()
            if part == 1
            else solution_instance.solve_part_two()
        )
        print(f"Solution is {solution}")
    except (ModuleNotFoundError, AttributeError) as e:
        print(e)
        print(f"Solution for Day {day}, Part {part} not found or not implemented.")


if __name__ == "__main__":
    main()
