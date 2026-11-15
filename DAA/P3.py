# Fractional Knapsack using Greedy Method
n = int(input("Enter number of items: "))
if n <= 0:
    print("Invalid input")
else:
    items = []
    valid = True

    for i in range(n):
        wt, val = map(int, input("Enter weight and value: ").split())

        if wt <= 0 or val < 0:
            print("Invalid input")
            valid = False
            break

        ratio = val / wt
        items.append((ratio, wt, val))

    if valid:
        W = int(input("Enter knapsack capacity: "))

        if W < 0:
            print("Invalid capacity")
        else:
            items.sort(reverse=True)
            total = 0

            for ratio, wt, val in items:
                if W == 0:
                    break

                if wt <= W:
                    total += val
                    W -= wt
                else:
                    total += ratio * W
                    W = 0

            print("Maximum value:", total)
# SAMPLE INPUT:
# 3
# 10 60
# 20 100
# 30 120
# 50
# SAMPLE OUTPUT: Maximum value: 240.0
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# RUN: python P3.py
