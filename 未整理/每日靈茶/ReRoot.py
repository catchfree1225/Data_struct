import sys
input = sys.stdin.readline
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def solve(n: int, edges: list):
    g = [[] for _ in range(n + 1)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)
        
    size = [0] * (n + 1)
    @bootstrap
    def dfs(x: int, fa: int):
        sum_, size[x] = 0, 1
        for y in g[x]:
            if y != fa:
                sum_ += yield dfs(y, x)
                size[x] += size[y]
        yield sum_ + size[x]
    
    ans = 0
    @bootstrap
    def reroot(x: int, fa: int, res: int):
        nonlocal ans
        ans = max(ans, res)
        for y in g[x]:
            if y != fa:
                yield reroot(y, x, res + n - size[y] * 2)
        yield
    reroot(1, 0, dfs(1, 0))
    print(ans)
            
n = int(input())
a = []
for _ in range(n - 1):
    a.append(tuple(map(int, input().split())))
solve(n, a)