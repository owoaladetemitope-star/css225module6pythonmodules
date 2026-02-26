# Barakat Owoalade
# february 25, 2026

# Problem 5: Convert radians to degrees using a user input value
# and compare it to math.degrees()

import math

radians = float(input("Enter a value in radians: "))

# Manual conversion
degrees_manual = radians * (180 / math.pi)

# Using math module
degrees_math = math.degrees(radians)

print("Converted manually:", degrees_manual)
print("Using math.degrees():", degrees_math)
