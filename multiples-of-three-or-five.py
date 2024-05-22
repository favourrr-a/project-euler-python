# Problem #1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.

def check_if_multiple_of_five_or_three(number):
    multiples_three_or_five = []
    for x in range(number):
        if x%3 == 0 or x%5 == 0:
            multiples_three_or_five.append(x)
    print((sum(multiples_three_or_five)))

check_if_multiple_of_five_or_three(1000)
