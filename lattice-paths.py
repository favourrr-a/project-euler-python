import math
def findNoPaths(dimensions):
    '''
    Given an n by n grid, this function returns the number of unique paths we could have if we were to move only right and down 

    To solve this, we can think of this as a combinatorics problem, where we need to calculate 
    the number of ways to arrange n right moves and n down moves in a sequence of 2n total moves

    this is basically 2n combination n, or (2n C n), or C(2n, n)

    which is (2n)! / (n! * n!)
    '''
    n = dimensions[0]
    return int((math.factorial(2 * n)) / (math.factorial(n) * (math.factorial(n))))

print(findNoPaths([20, 20]))