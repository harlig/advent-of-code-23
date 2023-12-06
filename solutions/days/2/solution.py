from solutions.solution import Solution


class DaySolution(Solution):
    def solve_part_one(self) -> str:
        print(self.input_data)
        possible_game_ids = []
        cubes_in_bag = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        for game_line in self.input_data:
            print(f"Processing {game_line}")
            game_scores = game_line.split(":", 2)[1].strip().split(";")
            parsed_game_score = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            game_score_satisfies_criteria = True
            for game_score in game_scores:
                parsed_pull_score = dict()
                for full_color_score in game_score.split(","):
                    values = full_color_score.strip().split(" ")
                    if cubes_in_bag[values[1]] < int(values[0]):
                        print(
                            f"cubes in bag at {values[1]} has more than {cubes_in_bag[values[1]]} cubes when it "
                            f"wants {values[0]}"
                        )
                        game_score_satisfies_criteria = False
                        break

            if game_score_satisfies_criteria:
                print("game score satisfies")
                possible_game_ids.append(game_line.split(":")[0].strip().split(" ")[1])
        print(possible_game_ids)
        total = 0
        for game_id in possible_game_ids:
            total += int(game_id)

        return str(total)

    def solve_part_two(self) -> str:
        print(self.input_data)
        all_powers = 0
        for game_line in self.input_data:
            print(f"Processing {game_line}")
            game_scores = game_line.split(":", 2)[1].strip().split(";")
            most_cubes_per_game = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for game_score in game_scores:
                for full_color_score in game_score.split(","):
                    values = full_color_score.strip().split(" ")
                    if most_cubes_per_game[values[1]] < int(values[0]):
                        most_cubes_per_game[values[1]] = int(values[0])

            power = 1
            for cube_color in most_cubes_per_game.keys():
                power *= most_cubes_per_game[cube_color]
            all_powers += power
        print(all_powers)
        return str(all_powers)


if __name__ == "__main__":
    today_solution = DaySolution("input0.txt")
    # print("running part one")
    # part_one = today_solution.solve_part_one()
    # print("part one results:")
    # print(part_one)

    # enable once part one solved
    print("running part two")
    part_two = today_solution.solve_part_two()
    print("part two results:")
    print(part_two)
