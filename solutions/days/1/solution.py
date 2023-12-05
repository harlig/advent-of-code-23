from solutions.solution import Solution


class PartSolution(Solution):
    def solve_part_one(self) -> str:
        print(self.input_data)
        total: int = 0
        for calibration_line in self.input_data:
            digits = [char for char in calibration_line if char.isdigit()]
            total += int(digits[0] + digits[-1])
        return str(total)

    def solve_part_two(self) -> str:
        valid_digit_spellings = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        print(self.input_data)
        print()
        total: int = 0
        for calibration_line in self.input_data:
            # we're considering index 0 in each word to begin with
            current_considered_index_into_word_at_word_index = [
                0 for _ in valid_digit_spellings
            ]
            digits = []
            for char in calibration_line:
                if char.isdigit():
                    digits.append(str(char))
                    continue

                print(
                    f"Checking char {char}; state of indexes {current_considered_index_into_word_at_word_index}"
                )

                # loop over digit spelling and we can just always consider all of them
                for digit_ndx, spelling in enumerate(valid_digit_spellings):
                    # get index of char in this digit spelling
                    consideration_index_for_spelling = (
                        current_considered_index_into_word_at_word_index[digit_ndx]
                    )
                    # for the word we're on, if the letter at the current index consideration equals the character in
                    # the line we're checking then let's consider the next letter in the word next iteration
                    if char == spelling[consideration_index_for_spelling]:
                        current_considered_index_into_word_at_word_index[digit_ndx] += 1
                        if (
                            len(spelling)
                            == current_considered_index_into_word_at_word_index[
                                digit_ndx
                            ]
                        ):
                            digits.append(str(digit_ndx + 1))
                            current_considered_index_into_word_at_word_index[
                                digit_ndx
                            ] = 0
                    else:
                        current_considered_index_into_word_at_word_index[digit_ndx] = 0

            print(f"digits are {digits}")
            total_str = digits[0]
            if len(digits) > 1:
                total_str += digits[-1]
            total += int(total_str)
            print(f"total is now {total}")
        return str(total)
