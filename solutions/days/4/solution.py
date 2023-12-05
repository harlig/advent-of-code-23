from solutions.solution import Solution


class DaySolution(Solution):
    def solve_part_one(self) -> str:
        print(self.input_data)
        total = 0
        for card_text in self.input_data:
            print(card_text)
            score = 0
            numbers_text = card_text.split(":")[1].strip().split("|")
            winning_numbers = [
                num.strip()
                for num in numbers_text[0].strip().split(" ")
                if len(num) > 0
            ]
            my_numbers = [
                num.strip()
                for num in numbers_text[1].strip().split(" ")
                if len(num) > 0
            ]

            for number in winning_numbers:
                if number in my_numbers:
                    print(f"Found number {number} in my numbers {my_numbers}")
                    score = score * 2 if score > 0 else 1
            total += score

        return str(total)

    def solve_part_two(self) -> str:
        print(self.input_data)
        # initially we have one of each of our scratchcards
        scratchcard_index_to_count = [1 for line in self.input_data]
        for ndx, card_text in enumerate(self.input_data):
            print(card_text)
            numbers_text = card_text.split(":")[1].strip().split("|")
            winning_numbers = [
                num.strip()
                for num in numbers_text[0].strip().split(" ")
                if len(num) > 0
            ]
            my_numbers = [
                num.strip()
                for num in numbers_text[1].strip().split(" ")
                if len(num) > 0
            ]

            matching_numbers_count = 0
            for number in winning_numbers:
                if number in my_numbers:
                    matching_numbers_count += 1

            print(f"Total matching numbers {matching_numbers_count}")
            print(scratchcard_index_to_count)
            for match in range(matching_numbers_count):
                scratchcard_index_to_count[
                    ndx + match + 1
                ] += scratchcard_index_to_count[ndx]
            print(scratchcard_index_to_count)

        print(scratchcard_index_to_count)
        return str(sum(scratchcard_index_to_count))


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
