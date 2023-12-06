from solutions.solution import Solution


class DaySolution(Solution):
    def solve_part_one(self) -> str:
        print(self.input_data)
        time_input = [
            int(time.strip())
            for time in self.input_data[0].split(": ")[1].strip().split(" ")
            if len(time) > 0
        ]
        distance_input = [
            int(dist.strip())
            for dist in self.input_data[1].split(": ")[1].strip().split(" ")
            if len(dist) > 0
        ]

        totals = []
        for ndx, race_time in enumerate(time_input):
            current_record = distance_input[ndx]

            # print(
            #     f"Evaluating race with time {race_time} at current record {current_record}"
            # )
            total_ways_we_beat_record = 0

            for button_held_time in range(0, int(race_time)):
                distance = (race_time - button_held_time) * button_held_time
                # print(
                #     f"If you hold button for {button_held_time}, then you go this far: {distance}"
                # )
                if distance > current_record:
                    total_ways_we_beat_record += 1

            totals.append(total_ways_we_beat_record)

        total = 1
        for num in totals:
            total *= num if num != 0 else 1

        return str(total)

    def solve_part_two(self) -> str:
        print(self.input_data)
        race_time = int(self.input_data[0].split(": ")[1].strip().replace(" ", ""))
        current_record = int(self.input_data[1].split(": ")[1].strip().replace(" ", ""))

        totals = []
        # print(
        #     f"Evaluating race with time {race_time} at current record {current_record}"
        # )
        total_ways_we_beat_record = 0

        for button_held_time in range(0, int(race_time)):
            distance = (race_time - button_held_time) * button_held_time
            # print(
            #     f"If you hold button for {button_held_time}, then you go this far: {distance}"
            # )
            if distance > current_record:
                total_ways_we_beat_record += 1

        totals.append(total_ways_we_beat_record)

        total = 1
        for num in totals:
            total *= num if num != 0 else 1

        return str(total)


if __name__ == "__main__":
    today_solution = DaySolution("input0.txt")
    print("running part one")
    part_one = today_solution.solve_part_two()
    print("part one results:")
    print(part_one)

    # enable once part one solved
    # print("running part two")
    # part_two = today_solution.solve_part_two()
    # print("part two results:")
    # print(part_two)
