from solutions.solution import Solution


class DaySolution(Solution):
    def solve_part_one(self) -> str:
        print(self.input_data)
        part_sum = 0
        parts_summed_coords = []
        for row_ndx, row in enumerate(self.input_data):
            for col_ndx, char in enumerate(row):
                # if 32 <= int(char) <= 47 and int(char) != 46:
                if ("!" <= char <= "/" and char != ".") or char == "@" or char == "=":
                    for row_offset_to_process in range(-1, 2):
                        for col_offset_to_process in range(-1, 2):
                            if (
                                row_offset_to_process == 0
                                and col_offset_to_process == 0
                            ):
                                continue
                            check_row_ndx = row_ndx + row_offset_to_process
                            check_col_ndx = col_ndx + col_offset_to_process
                            check_row = self.input_data[check_row_ndx]
                            check_char = check_row[check_col_ndx]
                            if (
                                check_row_ndx < 0
                                or check_row_ndx > len(self.input_data)
                                or check_col_ndx < 0
                                or check_col_ndx > len(row)
                            ):
                                parts_summed_coords.append(
                                    (check_row_ndx, check_col_ndx)
                                )
                                continue
                            if (
                                check_row_ndx,
                                check_col_ndx,
                            ) not in parts_summed_coords:
                                if check_char.isdigit():
                                    number_str = check_char
                                    for number_col in range(check_col_ndx - 1, -1, -1):
                                        if str(check_row[number_col]).isdigit():
                                            number_str = (
                                                str(check_row[number_col]) + number_str
                                            )
                                            parts_summed_coords.append(
                                                (check_row_ndx, number_col)
                                            )
                                        else:
                                            break
                                    for number_col in range(
                                        check_col_ndx + 1, len(check_row)
                                    ):
                                        if str(check_row[number_col]).isdigit():
                                            number_str = number_str + str(
                                                check_row[number_col]
                                            )
                                            parts_summed_coords.append(
                                                (check_row_ndx, number_col)
                                            )
                                        else:
                                            break
                                    part_sum += int(number_str)
                            parts_summed_coords.append((check_row_ndx, check_col_ndx))

        return str(part_sum)

    def solve_part_two(self) -> str:
        print(self.input_data)
        return str("../solutions/days/3 part 2")


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
