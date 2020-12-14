import re

from helpers.SolutionPrinter import SolutionPrinter


class DockingComputerSystem:
    def __init__(self, initialization_program):
        self.initialization_program = initialization_program
        self.memory = {}
        self.mask_one = 0
        self.mask_zero = 0
        self.mask = '0' * 36

    def initialize_memory(self):
        for instruction in self.initialization_program:
            verb = instruction[0]
            value_string = instruction[1]
            if verb == 'mask':
                self.set_mask(value_string)
            else:
                self.set_memory(verb, value_string)

    def initialize_memory_v2(self):
        for instruction in self.initialization_program:
            verb = instruction[0]
            value_string = instruction[1]
            if verb == 'mask':
                self.set_mask_v2(value_string)
            else:
                self.set_memory_v2(verb, value_string)

    def get_memory_sum_memory(self):
        return sum(self.memory.values())

    def set_mask(self, mask_string):
        self.mask_one = int(mask_string.replace('X', '0'), 2)
        self.mask_zero = int(mask_string.replace('X', '1'), 2)

    def set_memory(self, address_string, value_string):
        address = self.decode_address(address_string)
        value = int(value_string) | self.mask_one
        value = value & self.mask_zero
        self.memory[address] = value

    @staticmethod
    def decode_address(address_string):
        return int(re.search(r'\[(\d+)\]', address_string).group(1))

    def set_mask_v2(self, value_string):
        self.mask = value_string

    def set_memory_v2(self, address_string, value_string):
        bin_address_string = self.get_address_as_masked_bin_string(address_string)
        address_list = self.generate_all_possible_addresses(bin_address_string)
        for address in address_list:
            self.memory[address] = int(value_string)

    def get_address_as_masked_bin_string(self, address_string):
        decoded_address = self.decode_address(address_string)
        bin_address_string = bin(int(decoded_address))[2:]
        bin_address_string = bin_address_string.rjust(36, '0')
        bin_address_string = "".join([a if m == '0' else m
                                      for a, m in zip(bin_address_string, self.mask)])
        return bin_address_string

    def generate_all_possible_addresses(self, bin_address_string):
        num_x_in_mask = self.mask.count('X')
        address_list = []
        for number in range(2**num_x_in_mask):
            temp_bin_address_string = bin_address_string
            bin_number = bin(number)[2:].rjust(num_x_in_mask, '0')
            for bit in bin_number:
                temp_bin_address_string = temp_bin_address_string.replace('X', bit, 1)
            address_list.append(int(temp_bin_address_string, 2))
        return address_list


def read_file_to_initialization_program(file_name):
    with open(file_name) as file:
        lines = file.read().splitlines()
    initialization_program = [line.split(' = ') for line in lines]
    return initialization_program


def solve_part_1(initialization_program, solution_printer):
    docking_computer_system = DockingComputerSystem(initialization_program)
    docking_computer_system.initialize_memory()
    memory_sum = docking_computer_system.get_memory_sum_memory()
    solution_printer.add_part_solution(1, memory_sum)


def solve_part_2(initialization_program, solution_printer):
    docking_computer_system = DockingComputerSystem(initialization_program)
    docking_computer_system.initialize_memory_v2()
    memory_sum = docking_computer_system.get_memory_sum_memory()
    solution_printer.add_part_solution(2, memory_sum)


def run():
    solution_printer = SolutionPrinter(14)
    initialization_program = read_file_to_initialization_program('input')
    solve_part_1(initialization_program, solution_printer)
    solve_part_2(initialization_program, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
