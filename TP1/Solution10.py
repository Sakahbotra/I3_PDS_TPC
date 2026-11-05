def is_prime(n):
    if n < 2:
        return False
    d = 2
    while (d * d <= n):
        if (n % d == 0):
            return False
        d += 1
    return True

def goldbach(n):
    for p in range(2, n):
        if is_prime(p):
            q = n - p
            if is_prime(q):
                return (p , q) 
    return None

print("EXPECTED OUTPUT:")
print("Primes below 50:", end=" ")

for x in range(2, 50):
    if is_prime(x):
        print(x, end=" ")
print()  # Newline

primes_below_100_count = 0
for x in range(2, 100):
    if is_prime(x):
        primes_below_100_count += 1
print(f"Number of primes below 100: {primes_below_100_count}")

for even_num in range(4, 31, 2):
    pair = goldbach(even_num)
    if pair:
        print(f"The number is :{pair} plus together = {even_num}")

conjecture_holds = True
for even_num in range(4, 10001, 2):
    if not goldbach(even_num):
        conjecture_holds = False
        break

print(f"Goldbach holds for every even number from 4 to 10000: {conjecture_holds}")
