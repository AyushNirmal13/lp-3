# 0/1 Knapsack using Dynamic Programming
n = int(input("Enter number of items: "))
if n <= 0:
    print("Invalid input")
else:
    weight = []
    value = []
    valid = True

    for i in range(n):
        wt, val = map(int, input("Enter weight and value: ").split())

        if wt <= 0 or val < 0:
            print("Invalid input")
            valid = False
            break

        weight.append(wt)
        value.append(val)

    if valid:
        W = int(input("Enter knapsack capacity: "))

        if W < 0:
            print("Invalid capacity")
        else:
            dp = [[0] * (W + 1) for i in range(n + 1)]

            for i in range(1, n + 1):
                for j in range(W + 1):
                    # Exclude current item
                    dp[i][j] = dp[i - 1][j]

                    # Include current item if it fits
                    if weight[i - 1] <= j:
                        dp[i][j] = max(
                            dp[i][j],
                            value[i - 1] + dp[i - 1][j - weight[i - 1]]
                        )

            print("Maximum value:", dp[n][W])

# SAMPLE INPUT:
# 3
# 10 60
# 20 100
# 30 120
# 50
# SAMPLE OUTPUT: Maximum value: 220
# Time Complexity: O(n x W)
# Space Complexity: O(n x W)
# RUN: python P4.py
