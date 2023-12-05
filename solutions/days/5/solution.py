from solutions.solution import Solution
import pprint


class DaySolution(Solution):
    def solve_part_one(self) -> str:
        pp = pprint.PrettyPrinter()
        print(self.input_data)
        seeds = dict()

        maps = {
            # "seed-to-soil": {
            #     "source": "seed",
            #     "destination": "soil",
            #     "source_mappings_via_ndx": [
            #         0,
            #         1,
            #         2,
            #     ],  # ... should be set to ndx initially
            # }
        }

        current_name = None
        current_mappings = {}

        for line in self.input_data[2:]:
            if len(line.strip()) == 0:
                # TODO: add this to the end of the final iteration too
                existing_map = maps[current_name]
                existing_map["mappings"] = current_mappings
                maps[current_name] = existing_map
                current_mappings = {}
            elif line.strip().endswith("map:"):
                old_name = current_name
                current_name = line.split(" ")[0].strip()
                maps[current_name] = {
                    "mappings": current_mappings,
                    "goes_to": None,
                    "comes_from": old_name,
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
                for ndx, range_ndx in enumerate(
                    range(source_range_start, source_range_start + range_len)
                ):
                    current_mappings[range_ndx] = destination_range_start + ndx

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
                new_value = (
                    current_map["mappings"][current_index]
                    if current_index in current_map["mappings"]
                    else current_index
                )
                current_index = new_value
                current_map_key = current_map["goes_to"]
            results.append(int(current_index))

        return str(min(results))

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
