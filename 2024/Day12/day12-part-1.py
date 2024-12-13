def find_regions(grid):
    """
    Find and separate distinct regions in the grid.
    
    Args:
        grid (list of str): 2D grid of garden plots
    
    Returns:
        dict: Mapping of plant types to their regions
    """
    def flood_fill(x, y, plant_type, region, visited):
        """Recursively identify a region of connected garden plots."""
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or 
            grid[x][y] != plant_type or (x, y) in visited):
            return set()
        
        visited.add((x, y))
        region.add((x, y))
        
        # Check 4 adjacent directions
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            flood_fill(x+dx, y+dy, plant_type, region, visited)
        
        return region
    
    regions = {}
    visited = set()
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] != '.':
                plant_type = grid[i][j]
                region = flood_fill(i, j, plant_type, set(), visited)
                
                if plant_type not in regions:
                    regions[plant_type] = []
                regions[plant_type].append(region)
    
    return regions

def calculate_region_price(region, grid):
    """
    Calculate the price for a single region.
    
    Args:
        region (set): Set of (x,y) coordinates in the region
        grid (list of str): Original grid
    
    Returns:
        tuple: (area, perimeter, price)
    """
    area = len(region)
    
    # Directions to check adjacent plots
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    perimeter = 0
    for x, y in region:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if adjacent plot is outside region or outside grid
            if ((nx, ny) not in region or 
                nx < 0 or nx >= len(grid) or 
                ny < 0 or ny >= len(grid[0])):
                perimeter += 1
    
    price = area * perimeter
    return area, perimeter, price

def solve_garden_plot_fencing(grid):
    """
    Solve the garden plot fencing problem.
    
    Args:
        grid (list of str): 2D grid of garden plots
    
    Returns:
        int: Total price of fencing all regions
    """
    # Find regions for each plant type
    regions = find_regions(grid)
    
    # Calculate total price
    total_price = 0
    region_details = []
    for plant_type, plant_regions in regions.items():
        for region in plant_regions:
            area, perimeter, price = calculate_region_price(region, grid)
            total_price += price
            region_details.append({
                'plant_type': plant_type,
                'area': area,
                'perimeter': perimeter,
                'price': price
            })
    
    # Print detailed breakdown
    print("Region Details:")
    for detail in sorted(region_details, key=lambda x: x['price'], reverse=True):
        print(f"Plant Type {detail['plant_type']}: Area = {detail['area']}, Perimeter = {detail['perimeter']}, Price = {detail['price']}")
    
    return total_price

def main():
    # Read input from file
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    # Solve and print total price
    total_price = solve_garden_plot_fencing(grid)
    print(f"\nTotal Price of Fencing: {total_price}")

if __name__ == "__main__":
    main()