from helpers.SolutionPrinter import SolutionPrinter
from collections import Counter


def sum_yes_questions_anyone(group_declaration):
    group_declaration = group_declaration.replace('\n', '')
    number_of_yes_questions = len(set(group_declaration))
    return number_of_yes_questions


def sum_yes_questions_everyone(group_declaration):
    group_size = len(group_declaration.split())
    group_declaration = group_declaration.replace('\n', '')
    yes_count_dict = Counter(group_declaration)
    questions_all_answered_yes_to = 0
    for number_yes in yes_count_dict.values():
        if number_yes == group_size:
            questions_all_answered_yes_to += 1
    return questions_all_answered_yes_to


def solve_part_1(customs_declaration_list, solution_printer):
    sum_of_yes_counts = 0
    for group_declaration in customs_declaration_list:
        sum_of_yes_counts += sum_yes_questions_anyone(group_declaration)
    solution_printer.add_part_solution(1, sum_of_yes_counts)


def solve_part_2(customs_declaration_list, solution_printer):
    sum_of_yes_counts = 0
    for group_declaration in customs_declaration_list:
        sum_of_yes_counts += sum_yes_questions_everyone(group_declaration)
    solution_printer.add_part_solution(2, sum_of_yes_counts)


def read_file_to_customs_declaration_list(file_name):
    with open(file_name) as file:
        customs_declaration_list = file.read().split("\n\n")
    return customs_declaration_list


def run():
    solution_printer = SolutionPrinter(6)
    customs_declaration_list = read_file_to_customs_declaration_list('input')
    solve_part_1(customs_declaration_list, solution_printer)
    solve_part_2(customs_declaration_list, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
