import math

print("The power of 2 is :", math.pow(2, 3))
print(f"The Rounding and Absolute Value is: {math.ceil(4.6)}")
print(f"The Floor (Approx value) of 6.8 is: {math.floor(6.8)}")
print(f"The square root of the 16 is: {math.sqrt(16)}")



# print(math.sqrt(16))
# print(math.fabs(-3))
# print(math.sin(45))


# print(math.pi)

# radius=25

# area=(math.pi)*(math.pow(radius,2))

# print("Area: ",area)

# print(math.exp(10))

# fact=math.factorial(5)
# print("The factorial of 5 is : ",fact)

# remainder=23%2
# remainder=math.fmod(23,2)

# print(remainder)



#==============================================================================================================================================

# BASIC (Brain-storming) – 15 Questions
# 1. Without using %, how can you check if a number is even using only math functions?

# (Hint: use math.floor() or math.ceil())

# 2. Using math.sqrt(), how can you check if a number is a perfect square?

# (No loops needed)

# 3. If math.floor(x) == math.ceil(x), what can you conclude about x?

# Explain logically.

# 4. How can you use math.fabs() to compare two numbers and check if they are “almost equal”?

# (e.g., difference < 0.0001)

# 5. Using math.pi, calculate the area difference between two circles whose radii differ by exactly 1 unit — without writing a formula directly.

# (Think: area2 – area1)

# 6. Without using rounding functions, how can you round a number to 2 decimals using math.floor() only?
# 7. If a value x increases by 10% each day, use math.pow() to compute the value after n days.

# Explain why pow() is better than loops.

# 8. Using math.factorial(), check if a number is in the factorial series (1, 2, 6, 24…).

# (Logical reasoning required)

# 9. Using only math.log(x, 10) or base conversions, detect if a number is a power of 10.
# 10. Using math.sqrt(), compute the distance between two points without importing any distance library.

# (Think Pythagoras)

# 11. Using math.pi, estimate the length of a circle arc with radius R and angle θ in degrees.

# (Force yourself to convert degrees → radians)

# 12. Use math.ceil() to calculate the number of boxes needed to pack N items if each box holds K items.
# 13. How do you generate the next Fibonacci number using only:

# previous number

# ratio approximation using math.sqrt(5) (Golden ratio trick)

# 14. Using math.fabs(), detect if a number is exactly at the midpoint between two integers.
# 15. Using only math.pow(), compare growth rates:

# 1.02^365

# 1.10^52
# Which grows faster and why?

# 🔥 INTERMEDIATE (Brain-storming) – 15 Questions
# 1. Using math.log(), determine how many digits a number has without converting it to a string.

# (Hint: digits = floor(log10(n)) + 1)

# 2. Use math.gcd() to find if three numbers can form the sides of a similar triangle.
# 3. Create a pseudo-random number generator using only:

# math.sin()

# math.pi
# Explain how the logic works.

# 4. Using math.sqrt(), detect if a triangle is right-angled without using Pythagoras directly.

# (Think rearrangement)

# 5. Use math.log() to compute compound interest realistically without loops.
# 6. Use math.factorial() to approximate e (Euler’s constant) by series expansion.
# 7. Using only math.floor() and math.sqrt(), check if a number is prime.

# (Hint: trial division until sqrt)

# 8. Find the largest integer X such that X^X <= N using only:

# math.log()

# reasoning about monotonic functions

# (No loops or brute force)

# 9. Using math.pow(), compare exponential and polynomial growth rates for given numbers logically.
# 10. Using math.atan(), calculate the angle between two vectors in 2D.
# 11. Using math.log(), estimate how long it takes for a value growing at 7% per year to double.

# (Hint: log(2)/log(1.07))

# 12. Using only math.ceil() and math.log2(), determine memory blocks needed for data storage.
# 13. Using math.sin() and math.cos(), determine if two rotating points will ever align again.
# 14. With only math.sqrt() and basic operators, find the inscribed circle radius of a triangle (requires logic).
# 15. Use math.log() to find the maximum layers you can fold a paper (thickness doubles each fold) before exceeding a given height.

#==============================================================================================================================================================