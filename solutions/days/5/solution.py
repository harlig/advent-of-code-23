from solutions.solution import Solution
import pprint


class DaySolution(Solution):
    def solve_part_one(self) -> str:
        maps = {}

        current_name = None
        affected_source_ranges = []
        for line in self.input_data[2:]:
            if len(line.strip()) == 0:
                # TODO: add this to the end of the final iteration too
                existing_map = maps[current_name]
                existing_map["affected_source_ranges"] = affected_source_ranges
                maps[current_name] = existing_map
                affected_source_ranges = []
            elif line.strip().endswith("map:"):
                old_name = current_name
                current_name = line.split(" ")[0].strip()
                maps[current_name] = {
                    "goes_to": None,
                    "comes_from": old_name,
                    "affected_source_ranges": affected_source_ranges,
                }

                if old_name in maps:
                    old_name_map = maps[old_name]
                    old_name_map["goes_to"] = current_name
                    maps[old_name] = old_name_map
                continue
            else:
                split = line.strip().split(" ")
                destination_range_start = int(split[0])
                source_range_start = int(split[1])
                range_len = int(split[2])
                affected_source_ranges.append(
                    (
                        source_range_start,
                        source_range_start + range_len,
                        destination_range_start,
                    )
                )

                existing_map = maps[current_name]
                existing_map["affected_source_ranges"] = affected_source_ranges
                maps[current_name] = existing_map

        results = []

        # get answer for each of the initial seeds
        for seed in self.input_data[0].split(": ")[1].split(" "):
            starting_map_key = [
                possible_map_key
                for possible_map_key in maps.keys()
                if maps[possible_map_key]["comes_from"] is None
            ][0]
            current_map_key = starting_map_key
            current_index = int(seed)
            while current_map_key is not None:
                current_map = maps[current_map_key]

                new_value = current_index
                for affected_source_range in current_map["affected_source_ranges"]:
                    if (
                        affected_source_range[0]
                        <= current_index
                        < affected_source_range[1]
                    ):
                        new_value = (
                            current_index
                            - affected_source_range[0]
                            + affected_source_range[2]
                        )
                        break
                current_index = new_value
                current_map_key = current_map["goes_to"]
            results.append(int(current_index))

        return str(min(results))

    def solve_part_two_old(self) -> str:
        maps = {}

        current_name = None
        affected_source_ranges = []
        for line in self.input_data[2:]:
            if len(line.strip()) == 0:
                # TODO: add this to the end of the final iteration too
                existing_map = maps[current_name]
                existing_map["affected_source_ranges"] = affected_source_ranges
                maps[current_name] = existing_map
                affected_source_ranges = []
            elif line.strip().endswith("map:"):
                old_name = current_name
                current_name = line.split(" ")[0].strip()
                maps[current_name] = {
                    "goes_to": None,
                    "comes_from": old_name,
                    "affected_source_ranges": affected_source_ranges,
                }

                if old_name in maps:
                    old_name_map = maps[old_name]
                    old_name_map["goes_to"] = current_name
                    maps[old_name] = old_name_map
                continue
            else:
                split = line.strip().split(" ")
                destination_range_start = int(split[0])
                source_range_start = int(split[1])
                range_len = int(split[2])
                affected_source_ranges.append(
                    (
                        source_range_start,
                        source_range_start + range_len,
                        destination_range_start,
                    )
                )

                existing_map = maps[current_name]
                existing_map["affected_source_ranges"] = affected_source_ranges
                maps[current_name] = existing_map

        results = []

        seed_ranges_raw = self.input_data[0].split(": ")[1].split(" ")
        current_indexes = []
        for ndx in range(0, len(seed_ranges_raw), 2):
            start_seed = int(seed_ranges_raw[ndx].strip())
            seed_range = int(seed_ranges_raw[ndx + 1].strip())

            for seed_offset in range(seed_range):
                if seed_offset not in current_indexes:
                    current_indexes.append(start_seed + seed_offset)

        starting_map_key = [
            possible_map_key
            for possible_map_key in maps.keys()
            if maps[possible_map_key]["comes_from"] is None
        ][0]
        current_map_key = starting_map_key
        # current_value = int(start_seed)
        # current_indexes = [ndx + int(start_seed) for ndx in range(seed_range)]
        while current_map_key is not None:
            current_map = maps[current_map_key]

            current_indexes = list(set(current_indexes))

            for index_into_current_indexes, current_value in enumerate(current_indexes):
                for affected_source_range in current_map["affected_source_ranges"]:
                    if (
                        affected_source_range[0]
                        <= current_value
                        < affected_source_range[1]
                    ):
                        current_indexes[index_into_current_indexes] = (
                            current_value
                            - affected_source_range[0]
                            + affected_source_range[2]
                        )
                        break

            current_map_key = current_map["goes_to"]
        results.append(min([int(location) for location in current_indexes]))

        return str(min(results))

    def solve_part_two(self) -> str:
        results = []

        seed_ranges_raw = self.input_data[0].split(": ")[1].split(" ")
        current_indexes = []
        for ndx in range(0, len(seed_ranges_raw), 2):
            start_seed = int(seed_ranges_raw[ndx].strip())
            seed_range = int(seed_ranges_raw[ndx + 1].strip())

            for seed_index in range(start_seed + seed_range):
                while seed_index >= len(current_indexes):
                    current_indexes.append(len(current_indexes))

        for line in self.input_data[2:]:
            if len(line.strip()) == 0:
                continue
            elif line.strip().endswith("map:"):
                continue
            else:
                split = line.strip().split(" ")
                destination_range_start = int(split[0])
                source_range_start = int(split[1])
                range_len = int(split[2])
                processed_indexes = []
                for value in range(source_range_start, source_range_start + range_len):
                    while value >= len(current_indexes):
                        print(
                            f"Extending current indexes bc value si {value} and len is {len(current_indexes)}"
                        )
                        current_indexes.append(len(current_indexes))
                    for ndx, current_index_val in enumerate(current_indexes):
                        if current_index_val == value and ndx not in processed_indexes:
                            current_indexes[ndx] = (
                                destination_range_start + value - source_range_start
                            )
                            processed_indexes.append(ndx)
            print(current_indexes)
        results.append(min(current_indexes))

        return str(min(results))


if __name__ == "__main__":
    today_solution = DaySolution("input1.txt")
    # print("running part one")
    # part_one = today_solution.solve_part_one()
    # print("part one results:")
    # print(part_one)

    # enable once part one solved
    print("running part two")
    part_two = today_solution.solve_part_two()
    print("part two results:")
    print(part_two)
