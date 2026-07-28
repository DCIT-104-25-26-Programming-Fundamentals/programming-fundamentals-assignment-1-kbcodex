# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calc_sum(nums):
    total = 0
    for n in nums:
        total = total + n
    return total


def calc_avg(nums):
    total = calc_sum(nums)
    return total / len(nums)

def calc_max(nums):
    highest = nums[0]
    for n in nums:
        if n > highest:
            highest = n
    return highest

def calc_min(nums):
    lowest = nums[0]
    for n in nums:
        if n < lowest:
            lowest = n
    return lowest



count = int(input("How many numbers? "))

if count <= 0:
    print("Error: Number must be a positive integer.")
else:
    numbers = []
 
    for i in range(1, count + 1):
        val = int(input(f"Enter number {i}: "))
        numbers.append(val)
    
    print("\nResults:")
    print("Sum:    ", calc_sum(numbers))
    print("Average:", calc_avg(numbers))
    print("Maximum:", calc_max(numbers))
    print("Minimum:", calc_min(numbers))