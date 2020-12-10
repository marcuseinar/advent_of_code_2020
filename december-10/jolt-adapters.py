import operator
from functools import reduce
from itertools import groupby


from helpers.SolutionPrinter import SolutionPrinter


def get_diff_distribution_dict(differences_list):
    differences_counts = {diff: differences_list.count(diff) for diff in differences_list}
    return differences_counts


def get_differences_list(jolt_adapter_list):
    jolt_adapter_list.append(0)
    jolt_adapter_list.append(max(jolt_adapter_list) + 3)
    jolt_adapter_list.sort()
    differences = [term2 - term1 for term1, term2 in zip(jolt_adapter_list, jolt_adapter_list[1:])]
    return differences


def calculate_combinations(target, partial=[]):
    possible_terms = [1, 2, 3]
    s = sum(partial)
    if s == target:
        return 1
    if s > target:
        return 0
    possible_combinations = 0
    for term in possible_terms:
        possible_combinations += calculate_combinations(target, partial + [term])
    return possible_combinations


def calculate_different_arrangements(diff_list):
    sequence_of_ones_length = [len(list(group)) for value, group
                               in groupby(diff_list)
                               if value == 1]
    possible_combinations_list = [calculate_combinations(value) for value
                                  in sequence_of_ones_length]
    return reduce(operator.mul, possible_combinations_list)


def read_file_to_int_list(file_name):
    with open(file_name) as file:
        int_list = [int(line) for line in file.read().splitlines()]
    return int_list


def solve_part_1(diff_list, solution_printer):
    diff_count = get_diff_distribution_dict(diff_list)
    answer = diff_count[1] * diff_count[3]
    solution_printer.add_part_solution(1, answer)


def solve_part_2(diff_list, solution_printer):
    answer = calculate_different_arrangements(diff_list)
    solution_printer.add_part_solution(2, answer)


def run():
    solution_printer = SolutionPrinter(10)
    int_list = read_file_to_int_list('input')
    diff_list = get_differences_list(int_list)
    solve_part_1(diff_list, solution_printer)
    solve_part_2(diff_list, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
