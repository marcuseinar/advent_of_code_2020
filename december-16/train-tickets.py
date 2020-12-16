import re

import numpy as np

from helpers.SolutionPrinter import SolutionPrinter


class TrainTicketValdator:
    def __init__(self, valid_ranges_dict, tickets):
        self.valid_ranges = valid_ranges_dict
        self.tickets = tickets
        self.valid_tickets = []

    def store_valid_tickets_and_invalid_numbers(self):
        invalid_numbers = []
        for ticket in self.tickets:
            ticket_invalid_numbers = [number for number in ticket if not self._is_number_valid(number)]
            if ticket_invalid_numbers:
                invalid_numbers += ticket_invalid_numbers
            else:
                self.valid_tickets.append(ticket)
        return invalid_numbers

    def get_correct_index_per_field(self):
        possible_index_dict = {name: [n for n in range(len(self.valid_tickets[0]))]
                               for name in self.valid_ranges.keys()}
        for name in possible_index_dict.keys():
            impossible_index_list = []
            for ticket in self.valid_tickets:
                impossible_index_list += \
                    self._get_ticket_impossible_index_list(name, ticket)
            possible_index_dict[name] = [index for index in possible_index_dict[name]
                                         if index not in impossible_index_list]
        possible_index_dict = self._deduce_final_indexes(possible_index_dict)
        return possible_index_dict

    def _get_ticket_impossible_index_list(self, name, ticket):
        return [index for index, value in enumerate(ticket)
                                  if not self._is_value_in_range(value, self.valid_ranges[name])]

    def _is_number_valid(self, number):
        for name, ranges in self.valid_ranges.items():
            if any(lower <= number <= upper for lower, upper in ranges):
                return True
        return False

    @staticmethod
    def _is_value_in_range(value, range_list):
        for lower, upper in range_list:
            if lower <= value <= upper:
                return True
        return False

    @staticmethod
    def _deduce_final_indexes(possible_index_dict):
        keys_sorted_by_list_len = \
            sorted(possible_index_dict, key=lambda key: len(possible_index_dict[key]))
        for key in keys_sorted_by_list_len:
            for name in possible_index_dict:
                if name != key:
                    possible_index_dict[name] = [index for index in possible_index_dict[name]
                                                 if index not in possible_index_dict[key]]
        possible_index_dict = {key: index_list[0]
                               for key, index_list in possible_index_dict.items()}
        return possible_index_dict



def read_file_to_ranges_and_tickets(file_name):
    with open(file_name) as file:
        lines = file.read().splitlines()
    ranges = {}
    tickets = []
    for line in lines:
        if re.findall(r'(\d+,)+(\d+)$', line):
            tickets.append([int(number) for number in line.split(",")])
        else:
            match = re.match(r'(.+): (\d+-\d+) or (\d+-\d+)', line)
            if match:
                ranges[match.group(1)] = \
                    [tuple([int(number) for number in match.group(2).split('-')]),
                     tuple([int(number) for number in match.group(3).split('-')])]
    return ranges, tickets


def solve_part_1(ranges, tickets, solution_printer):
    train_ticket_validator = TrainTicketValdator(ranges, tickets)
    invalid_numbers = train_ticket_validator.store_valid_tickets_and_invalid_numbers()
    answer = sum(invalid_numbers)
    solution_printer.add_part_solution(1, answer)


def solve_part_2(ranges, tickets, solution_printer):
    train_ticket_validator = TrainTicketValdator(ranges, tickets)
    train_ticket_validator.store_valid_tickets_and_invalid_numbers()
    correct_filed_index_dict = train_ticket_validator.get_correct_index_per_field()
    index_with_departure = [value for key, value in correct_filed_index_dict.items()
                            if 'departure' in key]
    answer = 1
    for index in index_with_departure:
        answer *= tickets[0][index]
    solution_printer.add_part_solution(2, answer)


def run():
    solution_printer = SolutionPrinter(16)
    ranges, tickets = read_file_to_ranges_and_tickets('input')
    solve_part_1(ranges, tickets, solution_printer)
    solve_part_2(ranges, tickets, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
