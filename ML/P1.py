# Gradient Descent to find the minimum of y = (x + 3)^2
def f(x):
    return (x + 3) ** 2

def slope(x):
    return 2 * (x + 3)

x = 2
learning_rate = 0.1

for i in range(50):
    x = x - learning_rate * slope(x)
    print("Step", i + 1, ": x =", round(x, 4),
          " y =", round(f(x), 4))

print("\nLocal minimum is at x =", round(x, 4))
print("Minimum value of y =", round(f(x), 4))
# -----------------------------------------
# SAMPLE INPUT:
# No user input required.
# Starting x = 2
# Learning rate = 0.1
# Iterations = 50
#
# SAMPLE OUTPUT (final lines):
# Step 50 : x = -2.9999  y = 0.0
#
# Local minimum is at x = -2.9999
# Minimum value of y = 0.0
#
# NOTE:
# Gradient Descent is an optimization algorithm.
# It updates x using the derivative (slope).
# The minimum occurs near x = -3.
#
# RUN:
# python P6.py
# -----------------------------------------
