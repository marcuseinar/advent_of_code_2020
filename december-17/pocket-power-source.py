import numpy as np

from helpers.SolutionPrinter import SolutionPrinter


class PocketDimension:
    def __init__(self, initial_configuration):
        self.dimensions_grid = self._init_array(initial_configuration)
        self.num_neighbours_keep = [2, 3]
        self.num_neighbours_activate = [3]

    def get_active_after_cycles(self, cycles):
        for cycle in range(cycles):
            self._expand_dimensions()
            self._calculate_and_set_next_state()
        return np.sum(self.dimensions_grid)

    def _calculate_and_set_next_state(self):
        next_dimensions_grid = self.dimensions_grid.copy()
        for x, y, z in np.ndindex(self.dimensions_grid.shape):
            next_dimensions_grid[x, y, z] = self._get_next_state(x, y, z)
        self.dimensions_grid = next_dimensions_grid

    def _expand_dimension(self, stack_function, edge_0, edge_max, axis):
        x, y, z = self.dimensions_grid.shape
        x = 1 if axis == 'x' else x
        y = 1 if axis == 'y' else y
        z = 1 if axis == 'z' else z
        zeros = np.zeros((x, y, z))
        self.dimensions_grid = stack_function([zeros, self.dimensions_grid]) \
            if 1 in edge_0 else self.dimensions_grid
        self.dimensions_grid = stack_function([self.dimensions_grid, zeros]) \
            if 1 in edge_max else self.dimensions_grid

    def _expand_dimensions(self):
        x_edge_0 = self.dimensions_grid[0, :, :]
        x_edge_max = self.dimensions_grid[-1, :, :]
        self._expand_dimension(np.vstack, x_edge_0, x_edge_max, 'x')
        y_edge_0 = self.dimensions_grid[:, 0, :]
        y_edge_max = self.dimensions_grid[:, -1, :]
        self._expand_dimension(np.hstack, y_edge_0, y_edge_max, 'y')
        z_edge_0 = self.dimensions_grid[:, :, 0]
        z_edge_max = self.dimensions_grid[:, :, -1]
        self._expand_dimension(np.dstack, z_edge_0, z_edge_max, 'z')
        self.dimensions_grid = self.dimensions_grid.astype(np.int)

    @staticmethod
    def _init_array(array_2d_initial):
        array_2d_zeros = np.zeros_like(array_2d_initial)
        array_3d = np.dstack((array_2d_zeros, array_2d_initial, array_2d_zeros))
        return array_3d

    def _get_next_state(self, x, y, z):
        current_state = self.dimensions_grid[x, y, z]
        neighbourhood = self.dimensions_grid[
                        max(0, x - 1): x + 2,
                        max(0, y - 1): y + 2,
                        max(0, z - 1): z + 2]
        neighbour_sum = np.sum(neighbourhood) - self.dimensions_grid[x, y, z]
        num_to_active = self.num_neighbours_keep if current_state else self.num_neighbours_activate
        return 1 if neighbour_sum in num_to_active else 0


def read_file_to_initial_configuration(file_name):
    with open(file_name) as file:
        lines = file.read().splitlines()
    initial_config = np.array([[1 if char == "#" else 0 for char in list(line)] for line in lines])
    return initial_config


def solve_part_1(initial_config, solution_printer):
    pocket_dimension = PocketDimension(initial_config)
    active_neighbours = pocket_dimension.get_active_after_cycles(6)
    solution_printer.add_part_solution(1, active_neighbours)


def solve_part_2(initial_config, solution_printer):
    solution_printer.add_part_solution(2, initial_config)


def run():
    solution_printer = SolutionPrinter(17)
    initial_config = read_file_to_initial_configuration('input')
    solve_part_1(initial_config, solution_printer)
    solve_part_2(initial_config, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
