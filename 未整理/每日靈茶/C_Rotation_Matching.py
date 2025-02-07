import sys
input = sys.stdin.readline

def solve():
    m = {x: i for i, x in enumerate(a)}
    cnt = {}
    for j, x in enumerate(b):
        i = m[x]
        sft = (j - i + n) % n
        cnt[sft] = cnt.get(sft, 0) + 1
    print(max(cnt.values())) 

for _ in range(1):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solve()