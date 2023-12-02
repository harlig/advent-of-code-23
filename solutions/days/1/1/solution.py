from solutions.solution import Solution


class PartSolution(Solution):
    def solve(self) -> str:
        print(self.input_data)
        total: int = 0
        for calibration_line in self.input_data:
            digits = [char for char in calibration_line if char.isdigit()]
            total += int(digits[0] + digits[-1])
        return str(total)
