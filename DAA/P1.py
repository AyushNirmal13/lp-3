# Fibonacci series using iterative and recursive methods
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def iterative(n):
    a, b = 0, 1
    print("Non-Recursive:", end=" ")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

n = int(input("Enter number of terms (0 to 30): "))

if n < 0 or n > 30:
    print("Enter a value between 0 and 30")
else:
    iterative(n)

    print("Recursive:", end=" ")
    for i in range(n):
        print(fib(i), end=" ")
    print()

    print("Iterative Time: O(n), Space: O(1)")
    print("Recursive Time: O(2^n), Space: O(n)")

# SAMPLE INPUT: 5
# SAMPLE OUTPUT:
# Non-Recursive: 0 1 1 2 3
# Recursive: 0 1 1 2 3
# Iterative Time: O(n), Space: O(1)
# Recursive Time: O(2^n), Space: O(n)
#
# RUN: python P1.py
