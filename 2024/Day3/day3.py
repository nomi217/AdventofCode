# Part 1
# import re

# def parse_mul_instructions(memory):
#     # More precise regex to match exactly mul(X,Y)
#     # Ensures parentheses are correct () and no invalid characters
#     mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
#     total = 0
    
#     # Find all valid mul instructions
#     for match in re.finditer(mul_pattern, memory):
#         # Extract the two numbers and multiply them
#         x, y = map(int, match.groups())
#         result = x * y
#         total += result
#         print(f"Found valid mul instruction: mul({x},{y}) = {result}")
    
#     return total

# # For testing the example in the problem description
# test_memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
# test_result = parse_mul_instructions(test_memory)
# print(f"Test case result: {test_result}")

# # Read the input file
# with open('input.txt', 'r') as file:
#     corrupted_memory = file.read().strip()

# # Calculate the total of mul instructions
# result = parse_mul_instructions(corrupted_memory)
# print(f"\nFinal result: {result}")

# Part 2
import re

def parse_mul_instructions(memory):
    # Track whether mul instructions are currently enabled
    mul_enabled = True
    total = 0
    
    # Regex patterns for different instruction types
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r'don\'t\(\)')
    
    # Scan through the entire memory string
    pos = 0
    while pos < len(memory):
        # Check for do() instruction
        do_match = do_pattern.match(memory, pos)
        if do_match:
            mul_enabled = True
            pos = do_match.end()
            continue
        
        # Check for don't() instruction
        dont_match = dont_pattern.match(memory, pos)
        if dont_match:
            mul_enabled = False
            pos = dont_match.end()
            continue
        
        # Check for mul instruction
        mul_match = mul_pattern.match(memory, pos)
        if mul_match:
            if mul_enabled:
                x, y = map(int, mul_match.groups())
                result = x * y
                total += result
                print(f"Found enabled mul instruction: mul({x},{y}) = {result}")
            pos = mul_match.end()
            continue
        
        # Move to next character if no match
        pos += 1
    
    return total

# Test cases
test_cases = [
    # Original example from problem description
    #'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))',
    # New example with do() and don't() instructions
    #'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))'
]

for i, test_memory in enumerate(test_cases, 1):
    print(f"\nTest Case {i}:")
    test_result = parse_mul_instructions(test_memory)
    print(f"Test case result: {test_result}")

# Read the input file
with open('input.txt', 'r') as file:
    corrupted_memory = file.read().strip()

# Calculate the total of mul instructions
result = parse_mul_instructions(corrupted_memory)
print(f"\nFinal result: {result}")