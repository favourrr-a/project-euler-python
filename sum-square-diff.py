def sumOfSquares(num):
    sumOfSquares = 0
    for i in range(0, num + 1):
        sumOfSquares += i * i
    return sumOfSquares

def squareOfSum(num):
    squareOfSum = 0
    for i in range(0, num + 1):
        squareOfSum += i
    return squareOfSum * squareOfSum


print(squareOfSum(100) - sumOfSquares(100))