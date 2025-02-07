from math import isqrt
import sys
input = sys.stdin.readline
from collections import Counter

def factorize(x):
    ct = Counter()
    for i in range(2, isqrt(x) + 1):
        if x % i: 
            continue
        e = 0
        while x and x % i == 0:
            x //= i
            e += 1
        ct[i] = e
    if x > 1:
        ct[x] = 1
    return ct


def solve():
    ct = factorize(n0)
    for _ in range(m):
        q = list(map(int, input().split()))
        if q[0] == 2:
            ct = factorize(n0)
            continue
        
        # 不管是否合法，必須先更新值
        for p, e in factorize(q[1]).items():
            ct[p] += e  
        
        # 確認結果是否合法, dn必須是n的因數
        dn = 1
        for e in ct.values():
            dn *= e + 1
        for p, e in factorize(dn).items():
            if e > ct[p]:
                print('NO')
                break
        else:
            print('YES')
               
for _ in range(int(input())):
    n0, m = map(int, input().split())
    solve()
    print()
    