
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

def calculate_trailhead_rating(grid, trailhead):
    """
    Calculate the number of distinct hiking trails from a trailhead
    """
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Set to track unique 9-height destinations
    nine_destinations = set()
    
    # Queue to track all possible paths from the trailhead
    paths = [(trailhead[0], trailhead[1], 0, set([(trailhead[0], trailhead[1])]))]
    
    while paths:
        curr_r, curr_c, curr_height, current_path = paths.pop(0)
        
        # If reached a 9, add the unique path to destinations
        if grid[curr_r][curr_c] == 9:
            nine_destinations.add(frozenset(current_path))
        
        # Explore next moves
        for dr, dc in directions:
            curr_r_next, curr_c_next = curr_r + dr, curr_c + dc
            
            # Check if move is valid and not revisiting the same position
            if (is_valid_move(grid, curr_r, curr_r_next, curr_c, curr_c_next) and 
                (curr_r_next, curr_c_next) not in current_path):
                
                # Create new path by adding the next position
                new_path = set(current_path)
                new_path.add((curr_r_next, curr_c_next))
                
                # Add new path to exploration
                paths.append((
                    curr_r_next, 
                    curr_c_next, 
                    grid[curr_r_next][curr_c_next], 
                    new_path
                ))
    
    return len(nine_destinations)

def solve_hiking_trails_rating(map_input):
    """
    Solve the hiking trail problem by calculating trailhead ratings
    """
    grid = parse_map(map_input)
    trailheads = find_trailheads(grid)
    
    # Calculate ratings for each trailhead
    trailhead_ratings = [calculate_trailhead_rating(grid, th) for th in trailheads]
    
    return sum(trailhead_ratings), trailhead_ratings

# Read input from file
with open('input.txt', 'r') as file:
    input_map = file.read().strip()

# Solve the problem
total_rating, trailhead_ratings = solve_hiking_trails_rating(input_map)
print(f"Sum of trailhead ratings: {total_rating}")
print(f"Individual trailhead ratings: {trailhead_ratings}")