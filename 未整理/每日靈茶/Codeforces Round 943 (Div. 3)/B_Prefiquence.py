import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    t = ' ' + b  
    f = [[-1] * 2 for _ in range(len(t))]
    for c in range(2):
        nxt = -1
        for i in range(len(t) - 1, -1, -1):
            f[i][c] = nxt
            if t[i] == str(c):
                nxt = i
                
    def isSubseq(s): # s是否為t之子序列
        idx = 0
        for c in s:
            idx = f[idx][int(c)]
            if idx == -1:
                return False
        return True
    
    l, r = -1, n + 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if not isSubseq(a[:mid]):
            r = mid
        else:
            l = mid 
    print(r)
        
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = str(input())
    b = str(input())
    solve()