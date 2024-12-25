# Part 1

# import itertools

# def read_input(file_path):
#     with open(file_path, 'r') as file:
#         return file.readlines()

# def parse_equation(line):
#     test_value, numbers = line.split(':')
#     test_value = int(test_value.strip())
#     numbers = list(map(int, numbers.strip().split()))
#     return test_value, numbers

# def evaluate_expression(numbers, operators):
#     result = numbers[0]
#     for i in range(len(operators)):
#         if operators[i] == '+':
#             result += numbers[i + 1]
#         elif operators[i] == '*':
#             result *= numbers[i + 1]
#     return result

# def find_valid_equations(equations):
#     total_calibration_result = 0

#     for line in equations:
#         test_value, numbers = parse_equation(line)
#         num_positions = len(numbers) - 1
        
#         # Generate all combinations of operators
#         for operators in itertools.product(['+', '*'], repeat=num_positions):
#             if evaluate_expression(numbers, operators) == test_value:
#                 total_calibration_result += test_value
#                 break  # No need to check further combinations for this equation

#     return total_calibration_result

# # Main execution
# if __name__ == "__main__":
#     input_file = 'input.txt'  # Path to your input file
#     equations = read_input(input_file)
#     result = find_valid_equations(equations)
#     print(f"Total calibration result: {result}")

# Part 2

import itertools

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def parse_equation(line):
    test_value, numbers = line.split(':')
    test_value = int(test_value.strip())
    numbers = list(map(int, numbers.strip().split()))
    return test_value, numbers

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(f"{result}{numbers[i + 1]}")  # Concatenate and convert to int
    return result

def find_valid_equations(equations):
    total_calibration_result = 0

    for line in equations:
        test_value, numbers = parse_equation(line)
        num_positions = len(numbers) - 1
        
        # Generate all combinations of operators including the new concatenation operator
        for operators in itertools.product(['+', '*', '||'], repeat=num_positions):
            if evaluate_expression(numbers, operators) == test_value:
                total_calibration_result += test_value
                break  # No need to check further combinations for this equation

    return total_calibration_result

# Main execution
if __name__ == "__main__":
    input_file = 'input.txt'  # Path to your input file
    equations = read_input(input_file)
    result = find_valid_equations(equations)
    print(f"Total calibration result: {result}")