import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    cnt = Counter()      
    for ki in k:
        cnt.update(ki) 
       
    for ki in k:
        if all(cnt[d] > 1 for d in ki):
            print('Yes')
            return
    print('No')

for _ in range(int(input())):
    n = int(input()) # 下面先切片會增增加效能
    k = [tuple(map(int, input().split()))[1:] for _ in range(n)]
    solve()