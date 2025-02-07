import sys
input = sys.stdin.readline

def solve():
    g = [[] for _ in range(n)]
    ind = [0] * n
    for _ in range(n - 1):
        y, x = map(int, input().split())
        g[x - 1].append(y - 1)
        ind[y - 1] += 1
    rt = next(i for i, x in enumerate(ind) if x == 0)
    
    # def dfs(x: int):
    #     res_join = r[x]
    #     res_pass = 0  
    #     for y in g[x]:
    #         rj, rp = dfs(y)
    #         res_join += rp
    #         res_pass += max(rj, rp)
    #     return res_join, res_pass
    # print(max(dfs(rt)))      
    
    vis, info = [False] * n, [(-1, -1)] * n
    st = [rt]
    while st:
        x = st[-1]
        if vis[x]:
            st.pop()
            res_join = r[x]
            res_pass = 0
            for y in g[x]:
                rj, rp = info[y]
                res_join += rp
                res_pass += max(rj, rp)
            info[x] = res_join, res_pass
        else:
            vis[x] = True
            st += g[x]  
    print(max(info[rt]))
               
for _ in range(1):
    n = int(input())
    r = [int(input()) for _ in range(n)]
    solve()
    