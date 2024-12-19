def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    
    # Split the input into towel patterns and designs
    towel_patterns = data[0].split(', ')
    designs = data[2:]  # Skip the blank line
    return towel_patterns, designs

def can_construct_design(design, towel_patterns, memo):
    if design in memo:
        return memo[design]
    
    # If the design is empty, it can be constructed
    if not design:
        return True
    
    for towel in towel_patterns:
        # Check if the design starts with the current towel pattern
        if design.startswith(towel):
            # Recursively check the rest of the design
            if can_construct_design(design[len(towel):], towel_patterns, memo):
                memo[design] = True
                return True
    
    memo[design] = False
    return False

def count_possible_designs(towel_patterns, designs):
    memo = {}
    count = 0
    
    for design in designs:
        if can_construct_design(design, towel_patterns, memo):
            count += 1
            
    return count

def main():
    towel_patterns, designs = read_input('input.txt')
    possible_designs_count = count_possible_designs(towel_patterns, designs)
    print(f"Number of possible designs: {possible_designs_count}")

if __name__ == "__main__":
    main()