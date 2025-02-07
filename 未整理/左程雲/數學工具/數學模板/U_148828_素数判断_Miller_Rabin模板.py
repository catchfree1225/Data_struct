import random
import sys
input = sys.stdin.readline

def millerRabin(n, k):
    if n <= 4 or n % 2 == 0:
        return n in (2, 3)
    
    u, e = n - 1, 0
    while u % 2 == 0:
        u //= 2
        e += 1
        
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, u, n)
        if x in (1, n - 1):
            continue
        for _ in range(e - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False   
    return True
               
for _ in range(1):
    n = int(input())
    for _ in range(n):
        x = int(input())
        print('Yes' if millerRabin(x, 20) else 'No')
            