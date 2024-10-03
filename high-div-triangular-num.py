def findFactors(n):
    listOfFactors = []
    for i in range (1, int(n ** 0.5) + 1):
        if n % i == 0:
            listOfFactors.append(i)
            if i != n // i:
                listOfFactors.append(n // i)
    return listOfFactors

triangleNum = 0
for i in range (1, 999999999):
    triangleNum += i
    if len(findFactors(triangleNum)) >= 500:
        print("Triangle Number", i, ":", triangleNum)
        break