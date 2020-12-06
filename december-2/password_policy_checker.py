from helpers.SolutionPrinter import SolutionPrinter


class PasswordEntry:
    def __init__(self, policy_string, letter_string, password):
        self.min_range, self.max_range = self._get_range(policy_string)
        self.letter = letter_string[0]
        self.password = password

    @staticmethod
    def _get_range(range_string):
        ranges = [int(value) for value in range_string.split(sep='-')]
        return ranges[0], (ranges[1])

    def is_in_range(self):
        occurrences = self.password.count(self.letter)
        return self.min_range <= occurrences <= self.max_range

    def is_valid_positions(self):
        first_char = self.password[self.min_range-1]
        second_char = self.password[self.max_range-1]
        return (first_char == self.letter) ^ (second_char == self.letter)


def read_file_get_password_entries_list(filename):
    with open(filename) as file:
        line_string_list = [line.split() for line in file.readlines()]
        password_entries = [PasswordEntry(sub_str[0], sub_str[1], sub_str[2])
                            for sub_str in line_string_list]
    return password_entries


def solve_part_1(password_entries_list, solution_printer):
    num_valid_entries = 0
    for password_entry in password_entries_list:
        if password_entry.is_in_range():
            num_valid_entries += 1
    solution_printer.add_part_solution(1, num_valid_entries)


def solve_part_2(password_entries_list, solution_printer):
    num_valid_entries = 0
    for password_entry in password_entries_list:
        if password_entry.is_valid_positions():
            num_valid_entries += 1
    solution_printer.add_part_solution(2, num_valid_entries)


def run():
    solution_printer = SolutionPrinter(2)
    password_entries_list = read_file_get_password_entries_list('input')
    solve_part_1(password_entries_list, solution_printer)
    solve_part_2(password_entries_list, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
