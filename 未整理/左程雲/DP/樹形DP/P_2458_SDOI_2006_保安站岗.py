from math import inf
import sys
input = sys.stdin.readline

def solve():
    g = [[] for _ in range(n + 1)] 
    cost = [0] * (n + 1)
    ind = [0] * (n + 1)
    for _ in range(n):
        t = list(map(int, input().split()))
        cost[t[0]] = t[1]
        g[t[0]] = t[3:]
        for y in g[t[0]]:
            ind[y] += 1
    rt = next(i for i in range(1, n + 1) if ind[i] == 0)
    
    # def dfs(x: int):
    #     put = cost[x]
    #     by_fa, min_diff = 0, inf
    #     for y in g[x]:
    #         y_put, y_bf, y_bc = dfs(y)
    #         put += min(y_put, y_bf)
    #         by_fa += min(y_put, y_bc)
    #         min_diff = min(min_diff, y_put - y_bc)
    #     return put, by_fa, by_fa + max(min_diff, 0)
    # ans = dfs(rt)
    # print(min(ans[0], ans[2]))
    
    vis, info = [False] * (n + 1), [(-1, -1, -1)] * (n + 1)
    st = [rt]
    while st:
        x = st[-1]
        if vis[x]:
            st.pop()
            put = cost[x]
            by_fa, min_diff = 0, inf
            for y in g[x]:
                y_put, y_bf, y_bc = info[y]
                put += min(y_put, y_bf)
                by_fa += min(y_put, y_bc)
                min_diff = min(min_diff, y_put - y_bc)
            info[x] = put, by_fa, by_fa + max(min_diff, 0)
        else:
            vis[x] = True
            st += g[x]  
    print(min(info[rt][0], info[rt][2]))
                  
                  
for _ in range(1):
    n = int(input())
    solve()
    