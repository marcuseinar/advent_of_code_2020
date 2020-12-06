from helpers.SolutionPrinter import SolutionPrinter


def read_file_to_expense_list(filename):
    with open(filename) as file:
        expense_list = [int(item) for item in file.readlines()]
    return expense_list


def find_2_numbers_with_sum(expense_list, sum_to_find):
    for term in expense_list:
        other_term = sum_to_find - term
        if other_term in expense_list:
            return term, other_term
    return 0, 0


def find_3_numbers_with_sum(expense_list, sum_to_find):
    while expense_list:
        term = expense_list.pop()
        sub_sum = 2020 - term
        second_term, third_term = find_2_numbers_with_sum(expense_list, sub_sum)
        if second_term and third_term:
            return term, second_term, third_term


def solve_part_1(expense_list, solution_printer):
    factor1, factor2 = find_2_numbers_with_sum(expense_list, 2020)
    product = factor1 * factor2
    solution_printer.add_part_solution(1, product)


def solve_part_2(expense_list, solution_printer):
    factor1, factor2, factor3 = find_3_numbers_with_sum(expense_list, 2020)
    product = factor1 * factor2 * factor3
    solution_printer.add_part_solution(2, product)


def run():
    solution_printer = SolutionPrinter(1)
    expense_list = read_file_to_expense_list('input')
    solve_part_1(expense_list, solution_printer)
    solve_part_2(expense_list, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()

