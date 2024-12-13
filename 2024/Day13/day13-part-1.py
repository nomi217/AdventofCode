import re

def parse_input(file_path):
    machines = []
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n\n')
        for entry in data:
            lines = entry.split('\n')
            button_a = re.findall(r'X\+(\d+), Y\+(\d+)', lines[0])[0]
            button_b = re.findall(r'X\+(\d+), Y\+(\d+)', lines[1])[0]
            prize = re.findall(r'X=(\d+), Y=(\d+)', lines[2])[0]
            machines.append((
                (int(button_a[0]), int(button_a[1])),
                (int(button_b[0]), int(button_b[1])),
                (int(prize[0]), int(prize[1]))
            ))
    return machines

def calculate_min_tokens(machines):
    total_prizes = 0
    total_tokens = 0

    for (ax, ay), (bx, by), (px, py) in machines:
        found = False
        min_tokens = float('inf')

        for a in range(101):
            for b in range(101):
                if ax * a + bx * b == px and ay * a + by * b == py:
                    tokens = 3 * a + 1 * b
                    found = True
                    min_tokens = min(min_tokens, tokens)

        if found:
            total_prizes += 1
            total_tokens += min_tokens

    return total_prizes, total_tokens

# Main execution
if __name__ == "__main__":
    machines = parse_input('input.txt')
    total_prizes, total_tokens = calculate_min_tokens(machines)
    print(f'Maximum prizes won: {total_prizes}')
    print(f'Minimum tokens spent: {total_tokens}')