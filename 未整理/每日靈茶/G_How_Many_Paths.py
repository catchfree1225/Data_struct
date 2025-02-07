import sys
input = sys.stdin.readline
from collections import deque
"""
0, if there are no paths from 1 to v
1, if there is only one path from 1 to v
2, if there is more than one path from 1 to v and the number of paths is finite
-1, if the number of paths from 1 to v is infinite
"""
def solve_dfs():
    ans = [0] * n
    onPath = [False] * n
    def dfs(x: int, inCycle: bool):
        if inCycle:
            ans[x] = -1
        else:
            ans[x] += 1
        
        onPath[x] = True
        for y in g[x]:
            if ans[y] < 0: continue
            if inCycle or onPath[y]:
                dfs(y, True)
            elif ans[y] < 2:
                dfs(y, False)
        onPath[x] = False     
         
    dfs(0, False)
    print(*ans)
    
    
def solve_bfs(): # 計算way，不直接找父親
    reach = [False] * n # 檢查連通點
    reach[0] = True
    q = deque([0])
    while q:
        x = q.popleft()
        for y in g[x]:
            if not reach[y]:
                reach[y] = True
                q.append(y)
                
    ind = [0] * n
    for i in range(n): # 拓撲排序，計算連通點的入度
        if not reach[i]: continue
        for j in g[i]:
            ind[j] += 1
    
    ans, way = [0] * n, [0] * n  
    way[0] = 1
    q = deque([i for i in range(n) if ind[i] == 0 and reach[i]])     
    while q:
        x = q.popleft()       
        ans[x] = way[x] # 進入queue才會被assign
        for y in g[x]:
            ind[y] -= 1
            way[y] = min(way[x] + way[y], 2)
            if ind[y] == 0:
                q.append(y)  
                                    
    for i in range(n): # 成環不會進入queue 
        if reach[i] and ans[i] == 0:
            ans[i] = -1
    print(*ans)
    
    
def solve(): # stack+fa, 可直接找到父節點
    ans = [0] * n
    ans[0] = -1
    ind = [0] * n  
    st = [0]
    while st:
        x = st.pop()
        for y in g[x]:
            ind[y] += 1
            if ans[y] >= 0:
                ans[y] = -1
                st.append(y)
                
    if ind[0] == 0: # 起始點入度為0，無環
        ans[0] = 1
        fa = [-1] * n 
        st = [0]
        while st:
            x = st.pop()
            for y in g[x]:
                fa[y] = x if fa[y] == -1 else n
                ind[y] -= 1
                if ind[y] == 0: # 搜索完畢，使用父親Val
                    st.append(y)
                    ans[y] = ans[fa[y]] if fa[y] != n else 2
    print(*ans)

for _ in range(int(input())):
    _ = input()
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x - 1].append(y - 1)
    solve()
    