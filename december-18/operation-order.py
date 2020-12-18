from helpers.SolutionPrinter import SolutionPrinter

operations_same_precedence = {
    '*': {
        'operation': lambda a, b: a * b,
        'precedence': 1
    },
    '+': {
        'operation': lambda a, b: a + b,
        'precedence': 1
    }
}

operations_different_precedence = {
    '*': {
        'operation': lambda a, b: a * b,
        'precedence': 1
    },
    '+': {
        'operation': lambda a, b: a + b,
        'precedence': 2
    }
}


def calculate_output(output, operations):
    start_index = 0
    while len(output) > 1:
        a, b, c = tuple(output[start_index: start_index + 3])
        if c in operations:
            del output[start_index: start_index + 3]
            ans = operations[c]['operation'](int(a), int(b))
            output.insert(start_index, ans)
            start_index = 0
        else:
            start_index += 1
    return output[0]


def should_pop_operations_stack(operation_stack, operations, char):
    return len(operation_stack) \
        and operation_stack[-1] in operations \
        and operations[operation_stack[-1]]['precedence'] >= operations[char]['precedence']


def calculate_expression(expression, operations):
    output = []
    operation_stack = []
    for char in expression:
        if char.isdigit():
            output.append(int(char))
        elif char in operations:
            if should_pop_operations_stack(operation_stack, operations, char):
                output.append(operation_stack.pop())
            operation_stack.append(char)
        elif char == "(":
            operation_stack.append("(")
        elif char == ")":
            while operation_stack[-1] != "(":
                output.append(operation_stack.pop())
            operation_stack.pop()
    while len(operation_stack) > 0:
        output.append(operation_stack.pop())
    answer = calculate_output(output, operations)
    return answer


def calculate_sum_of_expressions(expression_list, operations):
    expression_answers = [calculate_expression(expression, operations)
                          for expression in expression_list]
    return sum(expression_answers)


def read_file_to_expression_list(file_name):
    with open(file_name) as file:
        expression_list = file.read().splitlines()
    expression_list = ["".join(expression.split()) for expression in expression_list]
    return expression_list


def solve_part_1(expression_list, solution_printer):
    answer = calculate_sum_of_expressions(expression_list, operations_same_precedence)
    solution_printer.add_part_solution(1, answer)


def solve_part_2(expression_list, solution_printer):
    answer = calculate_sum_of_expressions(expression_list, operations_different_precedence)
    solution_printer.add_part_solution(2, answer)


def run():
    solution_printer = SolutionPrinter(18)
    expression_list = read_file_to_expression_list('input')
    solve_part_1(expression_list, solution_printer)
    solve_part_2(expression_list, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
