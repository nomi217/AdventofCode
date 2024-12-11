def transform_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:  # Even number of digits
                mid = len(stone_str) // 2
                left_half = int(stone_str[:mid])
                right_half = int(stone_str[mid:])
                new_stones.append(left_half)
                new_stones.append(right_half)
            else:  # Odd number of digits
                new_stones.append(stone * 2024)
    return new_stones

def blink_stones(initial_stones, blinks):
    stones = initial_stones
    for _ in range(blinks):
        stones = transform_stones(stones)
    return stones

# Initial input
input_stones = [64599, 31, 674832, 2659361, 1, 0, 8867, 321]

# Number of blinks
blinks = 75

# Simulate the blinking process
final_stones = blink_stones(input_stones, blinks)

# Output the number of stones after the specified number of blinks
print(len(final_stones))