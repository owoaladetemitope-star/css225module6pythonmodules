# Barakat Owoalade
# february 25, 2026

# Problem 6: Use a for statement to calculate the factorial
# of a user input value. Print this value as well as the value
# using math.factorial()

import math

number = int(input("Enter a positive integer: "))

# Manual factorial using for loop
factorial_manual = 1

for i in range(1, number + 1):
    factorial_manual *= i

# Using math module
factorial_math = math.factorial(number)

print("Manual factorial:", factorial_manual)
print("Using math.factorial():", factorial_math)
