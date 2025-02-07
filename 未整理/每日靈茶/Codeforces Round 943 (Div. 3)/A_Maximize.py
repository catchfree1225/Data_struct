from math import gcd
import sys
input = sys.stdin.readline

def solve():
    for x in a:
        ans = mx = 0
        for y in range(1, x):
            if mx < gcd(x, y) + y:
                ans, mx = y, gcd(x, y) + y
        print(ans)
               
for _ in range(1):
    n = int(input())
    a = [int(input()) for _ in range(n)]
    solve()