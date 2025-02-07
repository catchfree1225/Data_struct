import sys
input = sys.stdin.readline
from math import inf

# When you color a letter in red again, it stays red.
def solve():
    n = len(t)
    f = [0] + [inf] * n # fi:染色長度i的最少次數
    pos = [(-1, -1)] * (n + 1) # 染色長度i(不一定貼滿)的字串pre_i,wj
    for i in range(n):
        for j in range(m):
            q = len(w[j])
            if i + q <= n and t[i:i+q] == w[j]:
                for k in range(q): # 可重疊，枚舉貼的長度
                    if f[i + k + 1] > f[i] + 1: # 統一更新後側
                        f[i + k + 1] = f[i] + 1
                        pos[i + k + 1] = (i, j) # 貼長度k, pre從長度i開始
    if f[n] == inf:
        print(-1)
    else:
        print(f[n])
        i = n # 已經貼了n
        while i: # 要貼的長度為0結束
            pre, j = pos[i] 
            print(j + 1, pre + 1)
            i = pre 
              
# 注意: 沒strip會多換行符號==
for _ in range(int(input())):
    t = input().strip()
    m = int(input())
    w = [input().strip() for _ in range(m)]
    solve()