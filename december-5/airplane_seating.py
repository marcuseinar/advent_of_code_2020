from helpers.SolutionPrinter import SolutionPrinter


def calculate_row_number(row_string):
    column = range(128)
    for char in row_string:
        divider = int(len(column)/2)
        if char == 'B':
            column = column[divider:]
        elif char == 'F':
            column = column[:divider]
    return column[0]


def calculate_column_number(row_string):
    row = range(8)
    for char in row_string:
        divider = int(len(row)/2)
        if char == 'R':
            row = row[divider:]
        elif char == 'L':
            row = row[:divider]
    return row[0]


def calculate_seat_id(boarding_card):
    row = calculate_row_number(boarding_card[:7])
    column = calculate_column_number(boarding_card[-3:])
    return row * 8 + column


def read_file_to_boarding_card_list(file_name):
    with open(file_name) as file:
        boarding_cards = file.read().splitlines()
    return boarding_cards


def solve_part_1(boarding_cards_list, solution_printer):
    seat_id_list = [calculate_seat_id(boarding_card) for boarding_card in boarding_cards_list]
    highest_seat = max(seat_id_list)
    solution_printer.add_part_solution(1, highest_seat)


def solve_part_2(boarding_cards_list, solution_printer):
    seat_id_list = [calculate_seat_id(boarding_card) for boarding_card in boarding_cards_list]
    lowest_seat = min(seat_id_list)
    highest_seat = max(seat_id_list)
    seat_id = sum(range(lowest_seat, highest_seat + 1)) - sum(seat_id_list)
    solution_printer.add_part_solution(2, seat_id)


def run():
    solution_printer = SolutionPrinter(5)
    boarding_cards_list = read_file_to_boarding_card_list('input')
    solve_part_1(boarding_cards_list, solution_printer)
    solve_part_2(boarding_cards_list, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
