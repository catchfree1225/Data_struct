import sys
input = sys.stdin.readline
from math import inf
class IPQ:
    __slots__ = 'heap', 'vals', 'pm', 'sz'
    def __init__(self, n):
        self.heap = [0] * n
        self.vals = [inf] * n
        self.pm = [-1] * n
        self.sz = 0

    def _less(self, i, j):
        return self.vals[self.heap[i]] < self.vals[self.heap[j]]

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pm[self.heap[i]], self.pm[self.heap[j]] = i, j
        
    def _swim(self, i):
        while i > 0 and self._less(i, p := (i - 1) // 2):
            self._swap(i, p)
            i = p

    def _sink(self, i):
        while True:
            l, r = 2 * i + 1, 2 * i + 2
            smallest = i
            if l < self.sz and self._less(l, smallest):
                smallest = l
            if r < self.sz and self._less(r, smallest):
                smallest = r
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def addOrUpdate(self, ki, val):
        if self.pm[ki] == -2:
            return
        if self.pm[ki] == -1:
            self.heap[self.sz] = ki
            self.pm[ki] = self.sz
            self.sz += 1
        self.vals[ki] = val
        self._swim(self.pm[ki])

    def pop(self):
        tmp = self.heap[0]
        self.sz -= 1
        self._swap(0, self.sz)
        self._sink(0)
        self.pm[tmp] = -2
        return tmp
    
def solve():
    g = [[] for _ in range(n)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        g[x - 1].append((y - 1, w))
        
    q = IPQ(n)
    q.addOrUpdate(0, 0)
    dis = q.vals
    while q.sz:
        x = q.pop()
        for y, wt in g[x]:
            if dis[y] > dis[x] + wt:
                q.addOrUpdate(y, dis[x] + wt)
    print(*dis)     
               
for _ in range(1):
    n, m, s = map(int, input().split())
    solve()