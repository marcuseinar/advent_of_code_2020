class SolutionPrinter:
    def __init__(self, task_nr):
        self.task_nr = task_nr
        self.part_solutions = []

    def add_part_solution(self, part_nr, solution):
        self.part_solutions.append((part_nr, solution))

    def print_solutions(self):
        print(f' ********** Task {self.task_nr} **********')
        for part_solution in sorted(self.part_solutions):
            print(f' * Part {part_solution[0]}: {part_solution[1]}')
