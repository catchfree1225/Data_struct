import sys
input = sys.stdin.readline
MOD = int(1e9 + 7)

def solve():
    lt = gt = False
    res_same = 1
    for x, y in zip(s, w):
        if x == '?' and y == '?':
            res_same = res_same * 10 % MOD
        elif x != '?' and y != '?':
            if x < y:
                lt = True
            elif x > y:
                gt = True
    res = pow(10, s.count('?') + w.count('?'), MOD)
    if lt and gt:
        print(res)
        return
    
    res_lt = res_gt = 1
    for x, y in zip(s, w):
        if x == '?' and y == '?':
            res_lt = res_lt * 55 % MOD
            res_gt = res_gt * 55 % MOD
        elif x == '?':
            res_lt = res_lt * (int(y) + 1) % MOD
            res_gt = res_gt * (10 - int(y)) % MOD
        elif y == '?':
            res_lt = res_lt * (10 - int(x)) % MOD
            res_gt = res_gt * (int(x) + 1) % MOD
    if not lt:
        res -= res_gt
    if not gt:
        res -= res_lt
    if not lt and not gt:
        res += res_same
    print(res % MOD)
    
n = int(input())
s = input()
w = input()
solve()