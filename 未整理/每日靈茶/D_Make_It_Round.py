import sys
input = sys.stdin.readline

def solve():
    c2 = c5 = 0
    x = n
    while x % 2 == 0:
        c2 += 1
        x /= 2
    x = n
    while x % 5 == 0:
        c5 += 1
        x /= 5
    
    k = 1
    while c2 < c5 and k * 2 <= m:
        c2 += 1
        k *= 2
    while c5 < c2 and k * 5 <= m:
        c5 += 1
        k *= 5
    while k * 10 <= m:
        k *= 10
    print(n * (m - m % k))
               
for _ in range(int(input())):
    n, m = map(int, input().split())
    solve()