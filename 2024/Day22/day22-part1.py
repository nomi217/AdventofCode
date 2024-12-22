def mix_and_prune(secret):
    # Step 1: Multiply by 64, mix, and prune
    secret = (secret * 64) ^ secret
    secret %= 16777216
    
    # Step 2: Divide by 32, round down, mix, and prune
    secret = (secret // 32) ^ secret
    secret %= 16777216
    
    # Step 3: Multiply by 2048, mix, and prune
    secret = (secret * 2048) ^ secret
    secret %= 16777216
    
    return secret

def simulate_secret_numbers(initial_secret, iterations):
    secret = initial_secret
    for _ in range(iterations):
        secret = mix_and_prune(secret)
    return secret

def main():
    # Read initial secret numbers from input.txt
    with open('input.txt', 'r') as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]

    total_sum = 0
    for initial_secret in initial_secrets:
        # Simulate 2000 new secret numbers
        final_secret = simulate_secret_numbers(initial_secret, 2000)
        total_sum += final_secret

    print(total_sum)

if __name__ == "__main__":
    main()