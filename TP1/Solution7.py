def digit_sum(n):
    total = 0
    temp = n
    while temp > 0:
        total += temp % 10  # Gets the last digit
        temp //= 10         # Removes the last digit
    return total

def reverse_number(n):
    reversed_num = 0
    temp = n
    while temp > 0:
        last_digit = temp % 10
        reversed_num = (reversed_num * 10) + last_digit
        temp //= 10
    return reversed_num

def is_palindrome(n):
    return n == reverse_number(n)

print("EXPECTED OUTPUT:")
test_numbers = [2026, 12321, 9875]

for num in test_numbers:
    d_sum = digit_sum(num)
    rev = reverse_number(num)
    pal = is_palindrome(num)
    print(f"{num}: digit sum = {d_sum}, reversed = {rev}, palindrome = {pal}")

palindrome_count = 0

for i in range(10, 1000):  # range(10, 1000) generates numbers from 10 to 999
    if is_palindrome(i):
        palindrome_count += 1

print(f"Palindromes from 10 to 999: {palindrome_count}")

