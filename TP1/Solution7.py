# 1. Function to sum the digits of a number
def digit_sum(n):
    total = 0
    temp = n
    while temp > 0:
        total += temp % 10  # Gets the last digit
        temp //= 10         # Removes the last digit
    return total

# 2. Function to reverse the digits of a number
def reverse_number(n):
    reversed_num = 0
    temp = n
    while temp > 0:
        last_digit = temp % 10
        reversed_num = (reversed_num * 10) + last_digit
        temp //= 10
    return reversed_num

# 3. Function to check if a number is a palindrome
def is_palindrome(n):
    # A number is a palindrome if it equals its reversed self
    return n == reverse_number(n)


# (a) Test the functions with 2026, 12321, and 9875

print("EXPECTED OUTPUT")
test_numbers = [2026, 12321, 9875]

for num in test_numbers:
    d_sum = digit_sum(num)
    rev = reverse_number(num)
    pal = is_palindrome(num)
    print(f"{num}: digit sum = {d_sum}, reversed = {rev}, palindrome = {pal}")

# (b) Count how many palindromes there are from 10 to 999

palindrome_count = 0
for i in range(10, 1000):  # range(10, 1000) generates numbers from 10 to 999
    if is_palindrome(i):
        palindrome_count += 1

print(f"Palindromes from 10 to 999: {palindrome_count}")

