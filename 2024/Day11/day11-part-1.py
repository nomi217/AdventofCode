def transform_stones(stones):
    """
    Transform the stones according to the specified rules:
    1. If stone is 0, replace with 1
    2. If stone has an even number of digits, split into two stones
    3. If no other rules apply, multiply stone by 2024
    """
    new_stones = []
    
    for stone in stones:
        # Rule 1: If stone is 0, replace with 1
        if stone == 0:
            new_stones.append(1)
        
        # Rule 2: If stone has an even number of digits, split
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            mid = len(stone_str) // 2
            left_stone = int(stone_str[:mid])
            right_stone = int(stone_str[mid:])
            
            # Remove leading zeros
            left_stone = int(str(left_stone))
            right_stone = int(str(right_stone))
            
            new_stones.extend([left_stone, right_stone])
        
        # Rule 3: Multiply by 2024
        else:
            new_stones.append(stone * 2024)
    
    return new_stones

def simulate_blinks(initial_stones, num_blinks):
    """
    Simulate the stone transformation for a given number of blinks
    """
    current_stones = initial_stones.copy()
    
    for _ in range(num_blinks):
        current_stones = transform_stones(current_stones)
    
    return current_stones

# Puzzle input
initial_stones = [64599, 31, 674832, 2659361, 1, 0, 8867, 321]

# Simulate 25 blinks
final_stones = simulate_blinks(initial_stones, 75)

# Print the number of stones after 25 blinks
print(f"Number of stones after 25 blinks: {len(final_stones)}")