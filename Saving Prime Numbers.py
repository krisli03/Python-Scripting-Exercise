def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

start_range, end_range = 1, 250

prime_numbers = [num for num in range(start_range, end_range + 1) if is_prime(num)]

print("Prime numbers between 1 and 250:")
print(prime_numbers)

with open('results.txt', 'w') as file:
    file.write('\n'.join(map(str, prime_numbers)))

print("Results saved to 'results.txt'.")