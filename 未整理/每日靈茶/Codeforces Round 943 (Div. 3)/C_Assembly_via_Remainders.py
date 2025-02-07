import sys
input = sys.stdin.readline
from bisect import bisect_left

def solve():
    a = [xs[0] + 1]
    for x in xs:
        r = x
        while r % a[-1] == 1:
            r += x
        a.append(r)
    print(*a)
               
for _ in range(int(input())):
    n = int(input())
    xs = list(map(int, input().split()))
    solve()