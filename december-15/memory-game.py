from helpers.SolutionPrinter import SolutionPrinter


class MemoryGameCalculator:
    def __init__(self, initial_numbers):
        self.previous_numbers = {int(number): int(turn)
                                 for turn, number in enumerate(initial_numbers)}
        self.start_turn = len(initial_numbers)
        self.next_number = 0

    def get_nth_number(self, n):
        for turn in range(self.start_turn, n):
            number = self.next_number
            self.next_number = turn - self.previous_numbers[number] \
                if number in self.previous_numbers \
                else 0
            self.previous_numbers[number] = turn
        return number


def read_file_to_initial_numbers(file_name):
    with open(file_name) as file:
        initial_numbers = file.read().split(",")
    return initial_numbers


def solve_part_1(initial_numbers, solution_printer):
    memory_game_calculator = MemoryGameCalculator(initial_numbers)
    number_2020 = memory_game_calculator.get_nth_number(2020)
    solution_printer.add_part_solution(1, number_2020)


def solve_part_2(initial_numbers, solution_printer):
    memory_game_calculator = MemoryGameCalculator(initial_numbers)
    number_30000000 = memory_game_calculator.get_nth_number(30000000)
    solution_printer.add_part_solution(2, number_30000000)


def run():
    solution_printer = SolutionPrinter(14)
    initial_numbers = read_file_to_initial_numbers('input')
    solve_part_1(initial_numbers, solution_printer)
    solve_part_2(initial_numbers, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
