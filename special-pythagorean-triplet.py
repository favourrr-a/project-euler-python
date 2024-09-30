for i in range(1, 1000):
    x = i
    for j in range(i + 1, int((1000 - i)/2) + 1):
        y = j
        z = 1000 - x - y
        if (x * x) + (y * y) == (z * z) and x + y + z == 1000:
            print(x, y, z, x * y * z)
            break