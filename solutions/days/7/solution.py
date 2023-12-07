import functools
from solutions.solution import Solution


class DaySolution(Solution):
    @staticmethod
    def list_item_from_hand_and_bid(hand: str, bid: int) -> tuple[str, int, list[int]]:
        scores = []
        for card in hand:
            scores.append(DaySolution.score_from_card(card))
        return hand, bid, scores

    @staticmethod
    def score_from_card(card: str) -> int:
        if card.isdigit():
            score = int(card)
        elif card == "T":
            score = 10
        elif card == "J":
            score = 11
        elif card == "Q":
            score = 12
        elif card == "K":
            score = 13
        elif card == "A":
            score = 14
        else:
            print(f"WARNING, unknown card {card}")
            raise
        return score

    @staticmethod
    def compare_two_list_items(first, second) -> int:
        for ndx, card in enumerate(first[0]):
            first_score = DaySolution.score_from_card(card)
            second_score = DaySolution.score_from_card(second[0][ndx])
            if first_score != second_score:
                print(f"not equal; first {first_score}; second {second_score}")
                return first_score - second_score
        return 0

    def solve_part_one(self) -> str:
        print(self.input_data)
        hands = []
        bids = []

        five_of_kind = []
        four_of_kind = []
        full_house = []
        three_of_kind = []
        two_pair = []
        one_pair = []
        high_card = []
        # array of each possible type
        # keep track of hand and bid
        for line in self.input_data:
            hand = line.split(" ")[0]
            bid = int(line.strip().split(" ")[1])

            counts = {}
            for card in hand:
                if card not in counts:
                    counts[card] = 0
                counts[card] += 1

            if len(counts.keys()) == 1:
                five_of_kind.append(self.list_item_from_hand_and_bid(hand, bid))
                continue
            if len(counts.keys()) == 2:
                is_four_of_kind = False
                for key in counts.keys():
                    if counts[key] == 4:
                        is_four_of_kind = True
                        four_of_kind.append(self.list_item_from_hand_and_bid(hand, bid))
                        break
                if not is_four_of_kind:
                    full_house.append(self.list_item_from_hand_and_bid(hand, bid))
                continue
            if len(counts.keys()) == 3:
                is_three_of_kind = False
                for key in counts.keys():
                    if counts[key] == 3:
                        three_of_kind.append(
                            self.list_item_from_hand_and_bid(hand, bid)
                        )
                        is_three_of_kind = True
                        break
                if not is_three_of_kind:
                    two_pair.append(self.list_item_from_hand_and_bid(hand, bid))
                continue
            is_one_pair = False
            for key in counts.keys():
                if counts[key] == 2:
                    one_pair.append(self.list_item_from_hand_and_bid(hand, bid))
                    is_one_pair = True
                    break
            if not is_one_pair:
                high_card.append(self.list_item_from_hand_and_bid(hand, bid))

            hands.append(hand)
            bids.append(bid)

        # determine type of hand, include it in the type for that thing,
        # then sort within the type array to figure out where to insert, keep track of bid

        five_of_kind = sorted(
            five_of_kind, key=functools.cmp_to_key(self.compare_two_list_items)
        )
        four_of_kind = sorted(
            four_of_kind, key=functools.cmp_to_key(self.compare_two_list_items)
        )
        full_house = sorted(
            full_house, key=functools.cmp_to_key(self.compare_two_list_items)
        )
        three_of_kind = sorted(
            three_of_kind, key=functools.cmp_to_key(self.compare_two_list_items)
        )
        two_pair = sorted(
            two_pair, key=functools.cmp_to_key(self.compare_two_list_items)
        )
        one_pair = sorted(
            one_pair, key=functools.cmp_to_key(self.compare_two_list_items)
        )
        high_card = sorted(
            high_card, key=functools.cmp_to_key(self.compare_two_list_items)
        )

        lowest_to_highest_types = [
            high_card,
            one_pair,
            two_pair,
            three_of_kind,
            full_house,
            four_of_kind,
            five_of_kind,
        ]

        total = 0
        hand_to_process = 1
        for hand_type in lowest_to_highest_types:
            winnings, hand_to_process = self.compute_winnings(
                hand_type, hand_to_process
            )
            total += winnings
        print(total)

        return str("../solutions/days/7 part 1")

    @staticmethod
    def compute_winnings(arr, hand_to_process) -> (int, int):
        total = 0
        max_ndx = hand_to_process
        for ndx, list_item in enumerate(arr):
            bid = list_item[1]
            total += bid * (hand_to_process + ndx)
            max_ndx += 1
        return total, max_ndx

    def solve_part_two(self) -> str:
        print(self.input_data)
        return str("../solutions/days/7 part 2")


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
