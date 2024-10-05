def collatz(n, count):
    if n == 1:
        count += 1
        return count
    elif n % 2 == 0:
        count += 1
        return collatz(int(n / 2), count)
    else:
        count += 1
        return collatz((3 * n) + 1, count)

max = 0
maxCount = 0
for i in range(1, 1000001):
    countI = collatz(i, 0)
    if countI > maxCount:
        max = i
        maxCount = countI
    print("number:", i, "count to zero", countI)
    print("max:", max, "maxCount:", maxCount)

