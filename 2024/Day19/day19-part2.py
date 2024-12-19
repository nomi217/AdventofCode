def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    
    # Split the input into towel patterns and designs
    towel_patterns = data[0].split(', ')
    designs = data[2:]  # Skip the blank line
    return towel_patterns, designs

def count_ways_to_construct_design(design, towel_patterns, memo):
    if design in memo:
        return memo[design]
    
    # If the design is empty, there is one way to construct it (by using no towels)
    if not design:
        return 1
    
    total_ways = 0
    
    for towel in towel_patterns:
        # Check if the design starts with the current towel pattern
        if design.startswith(towel):
            # Recursively count the ways to construct the rest of the design
            total_ways += count_ways_to_construct_design(design[len(towel):], towel_patterns, memo)
    
    memo[design] = total_ways
    return total_ways

def count_total_ways(towel_patterns, designs):
    memo = {}
    total_count = 0
    
    for design in designs:
        total_count += count_ways_to_construct_design(design, towel_patterns, memo)
            
    return total_count

def main():
    towel_patterns, designs = read_input('input.txt')
    total_ways = count_total_ways(towel_patterns, designs)
    print(f"Total number of ways to construct designs: {total_ways}")

if __name__ == "__main__":
    main()