from helpers.SolutionPrinter import SolutionPrinter


class CpuInstructionExecutor:
    OPERATION = 0
    ARGUMENT = 1

    def __init__(self, instruction_string_list):
        self.instruction_list = self.create_instruction_list(instruction_string_list)
        self.acc_register = 0
        self.i_ctr = 0
        self.instruction_set = {'nop': self._nop, 'acc': self._acc, 'jmp': self._jmp}
        self.instruction_history = []

    @staticmethod
    def create_instruction_list(instruction_list):
        instruction_list = [(operation, int(argument)) for operation, argument
                            in (instruction.split() for instruction in instruction_list)]
        return instruction_list

    def execute_instructions_get_acc_at_loop(self):
        self.instruction_history = []
        self._execute_and_check_for_loop()
        return self.acc_register

    def fix_loop_and_return_acc(self):
        self.instruction_history = []
        has_loop = self._execute_and_check_for_loop()
        instruction_history = self.instruction_history
        while has_loop:
            instruction = instruction_history.pop()
            self.i_ctr = instruction
            if self.instruction_list[self.OPERATION] == 'acc':
                self._acc(-self.instruction_list[self.ARGUMENT])
            else:
                self._swap_nop_and_jmp(instruction)
                has_loop = self._execute_and_check_for_loop()
                self._swap_nop_and_jmp(instruction)
        return self.acc_register

    def _execute_and_check_for_loop(self):
        while self.i_ctr < len(self.instruction_list):
            if self.i_ctr in self.instruction_history:
                return True
            temp = self.instruction_list[self.i_ctr]
            self._execute_instruction(temp)
        return False

    def _execute_instruction(self, instruction):
        self.instruction_history.append(self.i_ctr)
        argument = instruction[self.ARGUMENT]
        operation = instruction[self.OPERATION]
        self.instruction_set[operation](argument)

    def _increase_instruction_counter(self):
        self.i_ctr += 1

    def _nop(self, argument):
        self._increase_instruction_counter()

    def _acc(self, argument):
        self.acc_register += argument
        self._increase_instruction_counter()

    def _jmp(self, argument):
        self.i_ctr += argument

    def _swap_nop_and_jmp(self, instruction):
        operation = 'nop' if self.instruction_list[instruction][self.OPERATION] == 'jmp' else 'jmp'
        argument = self.instruction_list[instruction][self.ARGUMENT]
        self.instruction_list[instruction] = (operation, argument)


def read_boot_code_to_instruction_string_list(file_name):
    with open(file_name) as file:
        instruction_string_list = file.read().splitlines()
    return instruction_string_list


def solve_part_1(instruction_string_list, solution_printer):
    instruction_executor = CpuInstructionExecutor(instruction_string_list)
    acc_before_loop = instruction_executor.execute_instructions_get_acc_at_loop()
    solution_printer.add_part_solution(1, acc_before_loop)


def solve_part_2(instruction_string_list, solution_printer):
    instruction_executor = CpuInstructionExecutor(instruction_string_list)
    acc_before_loop = instruction_executor.fix_loop_and_return_acc()
    solution_printer.add_part_solution(2, acc_before_loop)


def run():
    solution_printer = SolutionPrinter(8)
    instruction_string_list = read_boot_code_to_instruction_string_list('input')
    solve_part_1(instruction_string_list, solution_printer)
    solve_part_2(instruction_string_list, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
