import itertools

import numpy as np

from helpers.SolutionPrinter import SolutionPrinter


def get_occupied_adjacent_seats(row, column, seat_matrix, visual_range):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    occupied_seats = 0
    for dy, dx in directions:
        x = column + dx
        y = row + dy
        steps = 0
        while -1 < x < len(seat_matrix[0]) and -1 < y < len(seat_matrix) and steps < visual_range:
            seat = seat_matrix[y][x]
            if seat == "#":
                occupied_seats += 1
            if seat == '#' or seat == 'L':
                break
            steps += 1
            x += dx
            y += dy

    return occupied_seats


def get_next_seat(row, column, seat_matrix, max_neighbours, visual_range):
    seat = seat_matrix[row][column]
    if seat == ".":
        return "."
    occupied_adjacent_seats = get_occupied_adjacent_seats(row, column, seat_matrix, visual_range)
    if seat == "L":
        return "#" if occupied_adjacent_seats == 0 else "L"
    if seat == "#":
        return "L" if occupied_adjacent_seats >= max_neighbours else "#"


def calculate_final_seating(seat_matrix, max_neighbours, visual_range=None):
    current_seating = [row for row in seat_matrix]
    rows = len(seat_matrix)
    columns = len(seat_matrix[0])
    visual_range = visual_range if visual_range else max(rows, columns)
    new_seating = ["".join([get_next_seat(
        row_index, column_index, current_seating, max_neighbours, visual_range)
                            for column_index in range(columns)])
                   for row_index in range(rows)]
    return new_seating if current_seating == new_seating else \
        calculate_final_seating(new_seating, max_neighbours, visual_range)


def read_file_to_seat_matrix(file_name):
    with open(file_name) as file:
        seat_matrix = [line for line in file.read().splitlines()]
    return seat_matrix


def solve_part_1(seat_matrix, solution_printer):
    final_seating = calculate_final_seating(seat_matrix, max_neighbours=4, visual_range=1)
    occupied_seats = "".join(final_seating).count("#")
    solution_printer.add_part_solution(1, occupied_seats)


def solve_part_2(seat_matrix, solution_printer):
    final_seating = calculate_final_seating(seat_matrix, max_neighbours=5)
    occupied_seats = "".join(final_seating).count("#")
    solution_printer.add_part_solution(2, occupied_seats)


def run():
    solution_printer = SolutionPrinter(11)
    seat_matrix = read_file_to_seat_matrix('input')
    solve_part_1(seat_matrix, solution_printer)
    solve_part_2(seat_matrix, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
