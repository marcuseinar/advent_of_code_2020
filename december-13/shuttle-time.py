import math

from helpers.SolutionPrinter import SolutionPrinter


def calculate_earliest_bus(earliest_time, bus_times):
    earliest_bus_times = {time: math.ceil(earliest_time/time) * time
                          for time in bus_times if isinstance(time, int)}
    bus_number = min(earliest_bus_times, key=earliest_bus_times.get)
    return bus_number, earliest_bus_times[bus_number]


def calculate_repeating_interval(first, second):
    if max(first, second) % min(first, second) == 0:
        return max(first, second)
    return first * second


def calculate_offset_time(start_time, interval, value, offset):
    time = start_time
    while (time + offset) % value != 0:
        time += interval
    return time


def calculate_time_of_rising_sequence(bus_times):
    time = bus_times[0]
    interval = bus_times[0]
    for index, value in enumerate(bus_times[1:]):
        offset = index + 1
        if not isinstance(value, int):
            continue
        time = calculate_offset_time(time, interval, value, offset)
        interval = calculate_repeating_interval(interval, value)
    return time


def read_file_to_bus_info(file_name):
    with open(file_name) as file:
        lines = file.read().splitlines()
    earliest_time = int(lines[0])
    bus_times = [int(time) if time.isdigit() else time for time in lines[1].split(',')]
    return earliest_time, bus_times


def solve_part_1(earliest_time, bus_times, solution_printer):
    earliest_bus_number, earliest_bus_time = calculate_earliest_bus(earliest_time, bus_times)
    answer = (earliest_bus_time - earliest_time) * earliest_bus_number
    solution_printer.add_part_solution(1, answer)


def solve_part_2(earliest_time, bus_times, solution_printer):
    earliest_time = calculate_time_of_rising_sequence(bus_times)
    solution_printer.add_part_solution(2, earliest_time)


def run():
    solution_printer = SolutionPrinter(13)
    earliest_time, bus_times = read_file_to_bus_info('input')
    solve_part_1(earliest_time, bus_times, solution_printer)
    solve_part_2(earliest_time, bus_times, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
