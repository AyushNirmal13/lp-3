# N-Queens using Backtracking
def is_safe(row, col):
    for r in range(row):
        if q[r] == col or abs(q[r] - col) == row - r:
            return False
    return True

def solve(row):
    if row == n:
        return True

    for col in range(n):
        if is_safe(row, col):
            q[row] = col

            if solve(row + 1):
                return True

    return False

n = int(input("Enter value of N: "))

if n <= 0:
    print("Invalid N")
else:
    col = int(input("Enter first queen column (1 to " + str(n) + "): "))

    if col < 1 or col > n:
        print("Invalid column")
    else:
        q = [-1] * n
        q[0] = col - 1

        if solve(1):
            print("N-Queens Matrix:")
            for i in range(n):
                for j in range(n):
                    print(1 if q[i] == j else 0, end=" ")
                print()
        else:
            print("No solution exists")

# SAMPLE INPUT:
# 4
# 3
# SAMPLE OUTPUT:
# N-Queens Matrix:
# 0 0 1 0
# 1 0 0 0
# 0 0 0 1
# 0 1 0 0
#
# 1 = queen, 0 = empty position.
# The first queen stays in the column entered.
# Time Complexity: O(N!) upper bound
# Space Complexity: O(N)
# RUN: python P5.py
