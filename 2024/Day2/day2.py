# Part 1

# def is_report_safe(levels):
#     # Check if levels are strictly increasing or decreasing
#     is_increasing = True
#     is_decreasing = True
    
#     for i in range(1, len(levels)):
#         diff = levels[i] - levels[i-1]
        
#         # Check if levels are changing consistently
#         if diff == 0:
#             is_increasing = False
#             is_decreasing = False
#             break
        
#         # Check if the change is between 1 and 3
#         if abs(diff) > 3:
#             is_increasing = False
#             is_decreasing = False
#             break
        
#         # Adjust consistency flags
#         if diff > 0:
#             is_decreasing = False
#         elif diff < 0:
#             is_increasing = False
    
#     return is_increasing or is_decreasing

# def count_safe_reports(reports):
#     safe_reports = 0
    
#     for report in reports:
#         levels = list(map(int, report.split()))
#         if is_report_safe(levels):
#             safe_reports += 1
    
#     return safe_reports

# # Read input from input.txt and solve the puzzle
# def solve_puzzle():
#     with open('input.txt', 'r') as file:
#         reports = file.readlines()
    
#     # Remove any trailing whitespace
#     reports = [report.strip() for report in reports]
    
#     return count_safe_reports(reports)

# # print the result
# print("Puzzle solution:", solve_puzzle())


# Part 2
def is_report_safe(levels):
    # Check if levels are strictly increasing or decreasing
    is_increasing = True
    is_decreasing = True
    
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i-1]
        
        # Check if levels are changing consistently
        if diff == 0:
            is_increasing = False
            is_decreasing = False
            break
        
        # Check if the change is between 1 and 3
        if abs(diff) > 3:
            is_increasing = False
            is_decreasing = False
            break
        
        # Adjust consistency flags
        if diff > 0:
            is_decreasing = False
        elif diff < 0:
            is_increasing = False
    
    return is_increasing or is_decreasing

def is_safe_with_dampener(levels):
    # First, check if the report is already safe
    if is_report_safe(levels):
        return True
    
    # Try removing each level and check if the resulting list is safe
    for i in range(len(levels)):
        # Create a new list without the i-th element
        modified_levels = levels[:i] + levels[i+1:]
        
        # Check if the modified list is safe
        if is_report_safe(modified_levels):
            return True
    
    return False

def count_safe_reports(reports):
    safe_reports = 0
    
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe_with_dampener(levels):
            safe_reports += 1
    
    return safe_reports

# Read input from input.txt and solve the puzzle
def solve_puzzle():
    with open('input.txt', 'r') as file:
        reports = file.readlines()
    
    # Remove any trailing whitespace
    reports = [report.strip() for report in reports]
    
    return count_safe_reports(reports)

# Print the result
print("Puzzle solution:", solve_puzzle())

# Optional: Verify with the example input
# example_reports = [
#     "7 6 4 2 1",
#     "1 2 7 8 9",
#     "9 7 6 2 1",
#     "1 3 2 4 5",
#     "8 6 4 4 1",
#     "1 3 6 7 9"
# ]
#print("Example reports safe count:", count_safe_reports(example_reports))