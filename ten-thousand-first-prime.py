def getPrime(location):
    currentPrimeLoc = 2
    currentNum = 2
    while(currentPrimeLoc <= location):
        currentNum += 1
        if currentNum % 2 == 0 and currentNum != 2:
            continue

        isPrime = False
        for i in range(1, int(currentNum/2) + 1):
            if currentNum % i == 0 and i != 1:
                isPrime = False
                break
            else: 
                isPrime = True

        if isPrime == True:
            currentPrimeLoc += 1
            
    return currentNum 

print(getPrime(10001))
        
