import re

from helpers.SolutionPrinter import SolutionPrinter


class NavigationSystem:
    def __init__(self, navigation_instruction_list):
        self.nav_instructions = navigation_instruction_list
        self.x = 0
        self.y = 0
        self.direction = 'E'
        self.relative_directions = {'R': 1, 'L': -1}
        self.absolute_directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    def calculate_route_distance(self):
        for instruction, value in self.nav_instructions:
            self.execute_instruction(instruction, value)
        manhattan_distance = abs(self.x) + abs(self.y)
        return manhattan_distance

    def execute_instruction(self, instruction, value):
        if instruction in self.relative_directions.keys():
            degrees = value * self.relative_directions[instruction]
            self.turn_ship(degrees)
            return
        direction = instruction if instruction[0] in self.absolute_directions.keys() \
            else self.direction
        distance = value
        dx, dy = self.absolute_directions[direction]
        self.x += dx * distance
        self.y += dy * distance

    def turn_ship(self, degrees):
        turn = int(degrees/90)
        current_direction_index = list(self.absolute_directions.keys()).index(self.direction)
        new_direction_index = (current_direction_index + turn) % len(self.absolute_directions.keys())
        self.direction = list(self.absolute_directions.keys())[new_direction_index]


class WaypointNavigationSystem:
    def __init__(self, navigation_instruction_list):
        self.nav_instructions = navigation_instruction_list
        self.ship_x = 0
        self.ship_y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.relative_directions = {'R': 1, 'L': -1}
        self.absolute_directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    def calculate_route_distance(self):
        for instruction, value in self.nav_instructions:
            self.execute_instruction(instruction, value)
        manhattan_distance = abs(self.ship_x) + abs(self.ship_y)
        return manhattan_distance

    def execute_instruction(self, instruction, value):
        if instruction == 'F':
            self.move_ship(value)
        elif instruction in self.absolute_directions.keys():
            self.move_waypoint(instruction, value)
        elif instruction in self.relative_directions.keys():
            self.rotate_waypoint(instruction, value)

    def move_ship(self, times):
        self.ship_x += self.waypoint_x * times
        self.ship_y += self.waypoint_y * times

    def move_waypoint(self, instruction, distance):
        self.waypoint_x += self.absolute_directions[instruction][0] * distance
        self.waypoint_y += self.absolute_directions[instruction][1] * distance

    def rotate_waypoint(self, instruction, degrees):
        direction = self.relative_directions[instruction]
        quarter_rotations = (int(degrees/90))
        for _ in range(quarter_rotations):
            self.waypoint_x, self.waypoint_y = \
                (self.waypoint_y * direction, -self.waypoint_x * direction)


def read_file_to_navigation_instructions(file_name):
    with open(file_name) as file:
        lines = file.read().splitlines()
    navigation_instruction_list = [(line[:1], int(line[1:])) for line in lines]
    return navigation_instruction_list


def solve_part_1(navigation_instructions, solution_printer):
    nav_system = NavigationSystem(navigation_instructions)
    distance = nav_system.calculate_route_distance()
    solution_printer.add_part_solution(1, distance)


def solve_part_2(navigation_instructions, solution_printer):
    nav_system = WaypointNavigationSystem(navigation_instructions)
    distance = nav_system.calculate_route_distance()
    solution_printer.add_part_solution(2, distance)


def run():
    solution_printer = SolutionPrinter(12)
    navigation_instructions = read_file_to_navigation_instructions('input')
    solve_part_1(navigation_instructions, solution_printer)
    solve_part_2(navigation_instructions, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
