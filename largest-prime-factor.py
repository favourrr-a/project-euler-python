# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143?

def findFactors(number):
    listOfFactors = []
    for i in range (1, int(number**0.5) + 1):
        if number%i==0:
            listOfFactors.append(i)
            if i != number // i:
                listOfFactors.append(number // i)
    print(listOfFactors)
    
    def isPrime(n):
        if n <= 1:
                return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primeFactors = [factor for factor in listOfFactors if isPrime(factor)]
    return max(primeFactors) if primeFactors else None
    
print(findFactors(13195))
print(findFactors(600851475143))

