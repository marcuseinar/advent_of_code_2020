import re

from helpers.SolutionPrinter import SolutionPrinter


class BagRulesInterpreter:
    def __init__(self, bag_rules_list):
        self.bag_rules = self.bag_rules_to_dict(bag_rules_list)

    def bag_rules_to_dict(self, bag_rules_list):
        bag_rules_list = self.remove_unnecessary_data_from_rules_list(bag_rules_list)
        bag_rules_dict = dict(rule.split(' contain ') for rule in bag_rules_list)
        bag_rules_dict = {bag.strip(): self.extract_rules_from_string(rules_string)
                          for bag, rules_string in bag_rules_dict.items()}
        return bag_rules_dict

    @staticmethod
    def remove_unnecessary_data_from_rules_list(bag_rules_list):
        return [re.sub(r'bags{0,1}|\.', '', bag_rule) for bag_rule in bag_rules_list]

    @staticmethod
    def extract_rules_from_string(rules_string):
        if rules_string == 'no other':
            return None
        return {rule.group(2).strip(): int(rule.group(1))
                for rule in re.finditer(r"(\d+)([\sa-zA-Z]+)", rules_string)}

    def get_bags_that_hold_color(self, color):
        bags_that_holds_color = [bag for bag, rules in self.bag_rules.items()
                                 if color in rules.keys()]
        for holder_color in bags_that_holds_color:

            bags_that_holds_color.extend(self.get_bags_that_hold_color(holder_color))
        return bags_that_holds_color

    def calculate_number_of_bags_inside_color(self, color):
        number_of_bags = 0
        for color, number in self.bag_rules[color].items():
            bags_in_bag = self.calculate_number_of_bags_inside_color(color)
            number_of_bags += number + number * bags_in_bag
        return number_of_bags


def solve_part_1(bag_rules_list, solution_printer):
    rules_interpreter = BagRulesInterpreter(bag_rules_list)
    list_of_colors_that_hold_shiny_gold = rules_interpreter.get_bags_that_hold_color('shiny gold')
    bag_types_that_can_hold_gold = len(set(list_of_colors_that_hold_shiny_gold))
    solution_printer.add_part_solution(1, bag_types_that_can_hold_gold)


def solve_part_2(bag_rules_list, solution_printer):
    rules_interpreter = BagRulesInterpreter(bag_rules_list)
    number_of_bags = rules_interpreter.calculate_number_of_bags_inside_color('shiny gold')
    solution_printer.add_part_solution(2, number_of_bags)


def read_file_to_bag_rules_list(file_name):
    with open(file_name) as file:
        bag_rules_list = file.read().splitlines()
    return bag_rules_list


def run():
    solution_printer = SolutionPrinter(7)
    bag_rules_list = read_file_to_bag_rules_list('input')
    solve_part_1(bag_rules_list, solution_printer)
    solve_part_2(bag_rules_list, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
