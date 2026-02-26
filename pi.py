# Barakat Owoalade
# february 25,2026

# Problem 4: Compute an approximation for pi and
# print that value as well as math.pi

import math

terms = 1000
pi_approx = 0

for i in range(terms):
    pi_approx += ((-1)**i) / (2*i + 1)

pi_approx = 4 * pi_approx

print("Approximated pi:", pi_approx)
print("math.pi:", math.pi)
