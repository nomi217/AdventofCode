# Part 1
# def calculate_location_distance(input_data):
#     
#     lines = input_data.strip().split('\n')
#     left_list = []
#     right_list = []
    
#     for line in lines:
#         left, right = map(int, line.split())
#         left_list.append(left)
#         right_list.append(right)
    
#     
#     left_list.sort()
#     right_list.sort()
    
#     
#     total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    
#     return total_distance

# 
# with open('paste.txt', 'r') as file:
#     input_data = file.read()

# 
# result = calculate_location_distance(input_data)
# print(f"Total distance between lists: {result}")


# Part 2
def calculate_similarity_score(input_data):
    
    lines = input_data.strip().split('\n')
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    
    similarity_score = 0
    for num in left_list:
        
        count = right_counts.get(num, 0)
        
        similarity_score += num * count
    
    return similarity_score


with open('input.txt', 'r') as file:
    input_data = file.read()


result = calculate_similarity_score(input_data)
print(f"Similarity score: {result}")