import sys
input = sys.stdin.readline
from math import inf

MX = int(1e5)
divs = [[] for _ in range(MX + 1)]
for i in range(1, MX + 1):
    for j in range(i, MX + 1, i):
        divs[j].append(i)
        
def solve():
    a = sorted(set(arr))
    cnt = [n] + [0] * m
    ans = inf
    tot = l = 0
    for x in a:
        for d in divs[x]:
            if d > m: break
            if cnt[d] == 0:
                tot += 1
            cnt[d] += 1
        while tot == m:
            ans = min(ans, x - a[l])
            for d in divs[a[l]]:
                if d > m: break
                cnt[d] -= 1
                if cnt[d] == 0:
                    tot -= 1
            l += 1
    print(ans if ans != inf else -1)
               
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    solve()