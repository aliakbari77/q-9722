import math

def checkPrime(n):
    if (n == 1):
        return False
    
    maxCheck = int(n/2) + 1
    for i in range(2, maxCheck):
        if (n%i == 0):
            return False
    return True
    
digitsNumber = int(input())

minimum = int(math.pow(10, digitsNumber - 1))
maximum = int(math.pow(10, digitsNumber))

for i in range(minimum, maximum + 1):
    n = i
    t = False
    while n:
        t = checkPrime(n)
        if (t):
            n = int(n/10)
        else:
            break
    if (t):
        print(i)

