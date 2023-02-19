# B. T-primes
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# We know that prime numbers are positive integers that have exactly two distinct positive divisors. Similarly, we'll call a positive integer t Т-prime, if t has exactly three distinct positive divisors.

# You are given an array of n positive integers. For each of them determine whether it is Т-prime or not.

# Input
# The first line contains a single positive integer, n (1 ≤ n ≤ 105), showing how many numbers are in the array. The next line contains n space-separated integers xi (1 ≤ xi ≤ 1012).

# Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is advised to use the cin, cout streams or the %I64d specifier.

# Output
# Print n lines: the i-th line should contain "YES" (without the quotes), if number xi is Т-prime, and "NO" (without the quotes), if it isn't.

# Examples
# inputCopy
# 3
# 4 5 6
# outputCopy
# YES
# NO
# NO
# Note
# The given test has three numbers. The first number 4 has exactly three divisors — 1, 2 and 4, thus the answer for this number is "YES". The second number 5 has two divisors (1 and 5), and the third number 6 has four divisors (1, 2, 3, 6), hence the answer for them is "NO".



limit = 1000000
def calculate_prime_flag_for_each_number_upto_limit():
    prime_flag = [True] * limit
    prime_flag[0] = prime_flag[1] = False
    for i in range(2,limit):
        if prime_flag[i] == True:
            for j in range(i*i, limit, i):
                prime_flag[j] = False
    return prime_flag                    

def check_if_a_number_is_t_prime(n):
    if n == 4:
        return True
    if n < 4 or n%2==0:
        return False
    sqrt_n = n**0.5
    if sqrt_n==int(sqrt_n):
        if prime_flag[int(sqrt_n)] == True:
            return True
    return False

prime_flag = calculate_prime_flag_for_each_number_upto_limit()
total_numbers = int(input())
input_array = list(map(int,input().split()))
for i in input_array:
    if check_if_a_number_is_t_prime(i)==True:
        print("YES")
    else:
        print("NO")