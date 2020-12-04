import re

from helpers.SolutionPrinter import SolutionPrinter


class PassportScanner:
    def __init__(self):
        self.validator = self.PassportCredentialValidator()

    def has_all_mandatory_credentials(self, credentials_dict):
        if 'cid' in credentials_dict: del credentials_dict['cid']
        return self.validator.has_all_credentials(credentials_dict)

    def has_all_credentials_valid(self, credentials_dict):
        if 'cid' in credentials_dict:
            del credentials_dict['cid']
        return self.validator.has_all_credentials(credentials_dict) and \
               all(self.validator.validate_credential(credential, value)
                   for credential, value in credentials_dict.items())

    class PassportCredentialValidator:
        def __init__(self):
            self._validator_dict = {'byr': self._validate_byr,
                                    'iyr': self._validate_iyr,
                                    'eyr': self._validate_eyr,
                                    'hgt': self._validate_hgt,
                                    'hcl': self._validate_hcl,
                                    'ecl': self._validate_ecl,
                                    'pid': self._validate_pid}
            self._eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            self._height_cm_regex = re.compile(r'^[0-9]{3}cm$')
            self._height_in_regex = re.compile(r'^[0-9]{2}in$')
            self._hair_colors_regex = re.compile(r'^#[0-9a-fA-F]{6}$')
            self._passport_id_regex = re.compile(r'^[0-9]{9}$')

        def has_all_credentials(self, credentials_dict):
            return all(credential in credentials_dict.keys()
                       for credential in self._validator_dict.keys())

        def validate_credential(self, field, value):
            return self._validator_dict[field](value)

        @staticmethod
        def _validate_year_range(year, min_year, max_year):
            return len(year) == 4 and min_year <= int(year) <= max_year

        def _validate_byr(self, byr):
            return self._validate_year_range(byr, 1920, 2002)

        def _validate_iyr(self, iyr):
            return self._validate_year_range(iyr, 2010, 2020)

        def _validate_eyr(self, eyr):
            return self._validate_year_range(eyr, 2020, 2030)

        def _validate_hgt(self, hgt):
            if self._height_cm_regex.match(hgt):
                return 150 <= int(hgt[:-2]) <= 193
            elif self._height_in_regex.match(hgt):
                return 59 <= int(hgt[:-2]) <= 76
            return False

        def _validate_hcl(self, hcl):
            return self._hair_colors_regex.match(hcl)

        def _validate_ecl(self, ecl):
            if ecl in self._eye_colors:
                return True
            return False

        def _validate_pid(self, pid):
            return self._passport_id_regex.match(pid)


def read_file_to_passport_credentials_list(file_name):
    with open(file_name) as file:
        credentials_list = file.read().split("\n\n")
    credentials_dict_list = []
    for credentials_string in credentials_list:
        credentials_dict = dict(credential.split(":") for credential in credentials_string.split())
        credentials_dict_list.append(credentials_dict)
    return credentials_dict_list


def solve_part_1(credentials_list, solution_printer):
    passport_scanner = PassportScanner()
    valid_passports = sum(passport_scanner.has_all_mandatory_credentials(credentials)
                          for credentials in credentials_list)
    solution_printer.add_part_solution(1, valid_passports)


def solve_part_2(credentials_list, solution_printer):
    passport_scanner = PassportScanner()
    valid_passports = sum(passport_scanner.has_all_credentials_valid(credentials)
                          for credentials in credentials_list)
    solution_printer.add_part_solution(2, valid_passports)


def run():
    solution_printer = SolutionPrinter(3)
    passport_credentials_list = read_file_to_passport_credentials_list('input')
    solve_part_1(passport_credentials_list, solution_printer)
    solve_part_2(passport_credentials_list, solution_printer)
    solution_printer.print_solutions()


if __name__ == '__main__':
    run()
