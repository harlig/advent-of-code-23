import argparse
import datetime
import sys
from typing import Optional
from generator import create_day


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Main script to create or run solutions."
    )
    subparsers = parser.add_subparsers(dest="command")

    # Create subparser for 'create' command
    create_parser = subparsers.add_parser("create")
    create_parser.add_argument(
        "-d", "--day", type=int, help="Day of the month for solution creation"
    )

    # Create subparser for 'run' command
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument(
        "-d", "--day", type=int, required=True, help="Day of the solution to run"
    )
    run_parser.add_argument(
        "-p", "--part", type=int, required=True, help="Part of the solution to run"
    )

    # Parse arguments
    args = parser.parse_args()

    if args.command == "create":
        handle_create(args.day)
    elif args.command == "run":
        # Placeholder for future implementation
        print(f"Running solution for day {args.day} part {args.part}")
    else:
        parser.print_help()


def handle_create(day: Optional[int]) -> None:
    if day is None:
        day = datetime.datetime.now().day
    if not (1 <= day <= 31):
        sys.exit("Error: Invalid day. Please provide a day between 1 and 31.")

    # Assuming create_day.py has a function named create_solution_directory
    create_day.create_solution_directory(str(day))


if __name__ == "__main__":
    main()
