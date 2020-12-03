from helpers.SolutionPrinter import SolutionPrinter


class TrajectoryCalculator:
    def __init__(self, slope_section_map):
        self.map = slope_section_map
        self.tree_char = '#'

    def calculate_collisions(self, x_steps, y_steps):
        row_width = len(self.map[0])
        row_position = 0
        collisions = 0
        for row in self.map[::y_steps]:
            if row[row_position] == self.tree_char:
                collisions += 1
            row_position = (row_position + x_steps) % row_width
        return collisions


def read_file_to_slope_section_map(file_name):
    with open(file_name) as file:
        slope_data_list = [line.rstrip() for line in file.readlines()]
    return slope_data_list


def solve_part_1(slope_section_map, solution_printer):
    trajectory_calculator = TrajectoryCalculator(slope_section_map)
    num_collisions = trajectory_calculator.calculate_collisions(3, 1)
    solution_printer.add_part_solution(2, num_collisions)


def solve_part_2(slope_section_map, solution_printer):
    trajectory_calculator = TrajectoryCalculator(slope_section_map)
    steps_x_y = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    prod_collisions = 1
    for slope in steps_x_y:
        prod_collisions *= trajectory_calculator.calculate_collisions(slope[0], slope[1])
    solution_printer.add_part_solution(2, prod_collisions)


def run():
    solution_printer = SolutionPrinter(3)
    expense_list = read_file_to_slope_section_map('input')
    solve_part_1(expense_list, solution_printer)
    solve_part_2(expense_list, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
