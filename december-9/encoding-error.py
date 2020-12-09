from helpers.SolutionPrinter import SolutionPrinter

def has_two_different_terms_in_list(sum, int_list):
    int_list = set(int_list)
    for term in int_list:
        other_term = sum - term
        if other_term in int_list:
            return True
    return False


def find_first_invalid_number(int_list, sequence_length):
    for index, number in enumerate(int_list[sequence_length:]):
        is_valid = has_two_different_terms_in_list(number, int_list[index: sequence_length + index])
        if not is_valid:
            return number
    return None


def find_first_and_last_terms_in_contiguous_set_of_terms_for_sum(sought_sum, int_list):
    start_index = 0
    end_index = 1
    test_sum = 0
    sub_list = []
    while test_sum != sought_sum:
        if test_sum < sought_sum:
            end_index += 1
        else:
            start_index += 1

        sub_list = int_list[start_index:end_index]
        test_sum = sum(sub_list)
    return min(sub_list), max(sub_list)


def read_file_to_int_list(file_name):
    with open(file_name) as file:
        int_list = [int(line) for line in file.read().splitlines()]
    return int_list


def solve_part_1(int_list, solution_printer):
    sequence_length = 25
    first_invalid_number = find_first_invalid_number(int_list, sequence_length)
    solution_printer.add_part_solution(1, first_invalid_number)
    return first_invalid_number


def solve_part_2(int_list, first_invalid_number, solution_printer):
    min_term, max_term = find_first_and_last_terms_in_contiguous_set_of_terms_for_sum(
        first_invalid_number,
        int_list)
    sum_of_min_max_terms = min_term + max_term
    solution_printer.add_part_solution(2, sum_of_min_max_terms)


def run():
    solution_printer = SolutionPrinter(9)
    int_list = read_file_to_int_list('input')
    first_invalid_number = solve_part_1(int_list, solution_printer)
    solve_part_2(int_list, first_invalid_number, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
