def parse_map(map_input):
    """
    Parse the input into a 2D grid of heights
    """
    return [list(map(int, line.strip())) for line in map_input.split('\n') if line.strip()]

def find_trailheads(grid):
    """
    Find all trailheads (positions with height 0)
    """
    trailheads = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def is_valid_move(grid, curr_r, curr_r_next, curr_c, curr_c_next):
    """
    Check if the move is valid (within grid and increases height by exactly 1)
    """
    # Check grid bounds
    if (curr_r_next < 0 or curr_r_next >= len(grid) or 
        curr_c_next < 0 or curr_c_next >= len(grid[0])):
        return False
    
    # Check height increase is exactly 1
    return grid[curr_r_next][curr_c_next] == grid[curr_r][curr_c] + 1

def calculate_trailhead_score(grid, trailhead):
    """
    Calculate the number of 9-height positions reachable from a trailhead
    """
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Keep track of visited positions and 9-height positions found
    visited = set([trailhead])
    nine_positions = set()
    
    # Paths to explore
    paths = [(trailhead[0], trailhead[1], 0)]
    
    while paths:
        curr_r, curr_c, curr_height = paths.pop(0)
        
        # Add 9 positions
        if grid[curr_r][curr_c] == 9:
            nine_positions.add((curr_r, curr_c))
        
        # Explore next moves
        for dr, dc in directions:
            curr_r_next, curr_c_next = curr_r + dr, curr_c + dc
            
            # Check if move is valid and not yet visited
            if (is_valid_move(grid, curr_r, curr_r_next, curr_c, curr_c_next) and 
                (curr_r_next, curr_c_next) not in visited):
                visited.add((curr_r_next, curr_c_next))
                paths.append((curr_r_next, curr_c_next, grid[curr_r_next][curr_c_next]))
    
    return len(nine_positions)

def solve_hiking_trails(map_input):
    """
    Solve the hiking trail problem by calculating trailhead scores
    """
    grid = parse_map(map_input)
    trailheads = find_trailheads(grid)
    
    # Calculate scores for each trailhead
    trailhead_scores = [calculate_trailhead_score(grid, th) for th in trailheads]
    
    return sum(trailhead_scores), trailhead_scores

# Read input from file
with open('input.txt', 'r') as file:
    input_map = file.read().strip()

# Solve the problem
total_score, trailhead_scores = solve_hiking_trails(input_map)
print(f"Sum of trailhead scores: {total_score}")
print(f"Individual trailhead scores: {trailhead_scores}")