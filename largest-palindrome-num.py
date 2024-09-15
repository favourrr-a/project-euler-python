def isPalindrome(num):
    isPalindrome = False
    numL = [int(num) for num in str(num)]

    for i in range(0, int(len(numL)/2)):
        if numL[i] == numL[len(numL) - 1 - i]:
            isPalindrome = True
        else: 
            return False
    return isPalindrome

largest = [100, 200]
for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(i * j) and i * j > largest[0] * largest[1]:
            largest[0], largest[1] = i, j

print(largest[0] * largest[1])