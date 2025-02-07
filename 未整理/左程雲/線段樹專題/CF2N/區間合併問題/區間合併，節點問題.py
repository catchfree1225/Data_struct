class SegTree:
    def __init__(self, init):
        self.n = 1 << init.bit_length()
        self.tr = [0] * (self.n << 1)
        self.upd = [None] * self.n
    
    def lazy(self, i, p, val):
        self.tr[i] = val << p
        if i < self.n:
            self.upd[i] = val
    
    def pull(self, i):
        p = 0
        while i > 1:
            i >>= 1
            p += 1
            if self.upd[i] is not None:
                self.tr[i] = self.upd[i] << p   
            else:     
                self.tr[i] = self.tr[i << 1] + self.tr[i << 1 | 1]
                
    def push(self, i):        
        for p in range(i.bit_length() - 1, 0, -1):
            j = i >> p
            if self.upd[j] is not None: # 先修改再增加
                self.lazy(j << 1, p - 1, self.upd[j])
                self.lazy(j << 1 | 1, p - 1, self.upd[j])
                self.upd[j] = None  
    
    def modify(self, l, r, val):
        l += self.n
        r += self.n
        self.push(l), self.push(r)
        l0, r0 = l, r
        p = 0
        while l <= r:
            if l & 1:
                self.lazy(l, p, val) 
                l += 1
            if not r & 1:
                self.lazy(r, p, val)
                r -= 1
            l >>= 1
            r >>= 1
            p += 1
        self.pull(l0), self.pull(r0)
    
    def query(self, l, r): #[l, r]
        l += self.n
        r += self.n
        self.push(l), self.push(r)
        res_l = res_r = 0
        while l <= r:
            if l & 1: # 左子樹
                res_l += self.tr[l]
                l += 1
            if not r & 1: # 右子樹
                res_r += self.tr[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res_l + res_r

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        n = max(r for _, r in paint) + 2
        tr = SegTree(n)
        ans = []
        # [l, r]區間，可以用[l, r)點維護: 節點紀錄右一段之info
        for l, r in paint:
            l += 1
            add = r - l + 1 - tr.query(l, r)
            ans.append(add)
            tr.modify(l, r, 1)
        return ans


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
    
    def find(self, u):
        rt = u
        while self.p[rt] != rt:
            rt = self.p[rt]
        while self.p[u] != rt:
            u, self.p[u] = self.p[u], rt
        return rt

    def join(self, u, v):
        u, v = self.find(u), self.find(v)
        if u != v:
            self.p[v] = u

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        n = max(r for _, r in paint) + 2
        uf = UnionFind(n)
        ans = []
        for l, r in paint:
            s, e = uf.find(l), uf.find(r)
            cnt = 0
            while s != e:
                cnt += 1
                uf.join(e - 1, e)
                e = uf.find(e)
            ans.append(cnt)
        return ans


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
    
    def find(self, u):
        rt = u
        while self.p[rt] != rt:
            rt = self.p[rt]
        while self.p[u] != rt:
            u, self.p[u] = self.p[u], rt
        return rt

    def join(self, u, v):
        u, v = self.find(u), self.find(v)
        if u != v:
            self.p[v] = u

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        n = max(r for _, r in paint) + 2
        uf = UnionFind(n)
        ans = []
        for l, r in paint:
            s, e = uf.find(l), uf.find(r)
            cnt = 0
            while s != e:
                cnt += 1
                uf.join(e - 1, e)
                e = uf.find(e)
            ans.append(cnt)
        return ans

from sortedcontainers import SortedList, SortedDict
class CountIntervals:
    def __init__(self):
        self.sm, self.cnt = SortedDict(), 0

    def add(self, left: int, right: int) -> None:
        sm, cnt = self.sm, self.cnt
        i = sm.bisect_left(right + 1) - 1
        while i >= 0:
            s, e = sm.peekitem(i)
            if e < left:
                break
            left = min(left, s)
            right = max(right, e)
            cnt -= e - s + 1
            sm.popitem(i)
            i -= 1
        cnt += right - left + 1
        self.cnt = cnt
        sm[left] = right

    def count(self) -> int:
        return self.cnt

from sortedcontainers import SortedList, SortedDict
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        a = list(s)
        sm, sl = SortedDict(), SortedList(key=lambda x: -x)
        def split(i):
            pos = sm.bisect_left(i + 1) - 1
            s, e = sm.peekitem(pos)
            if s == i:
                return
            sm.popitem(pos)
            sm[s] = i - 1
            sm[i] = e
            sl.remove(e - s + 1)
            sl.add(i - s)
            sl.add(e - i + 1)
        
        def union(i):
            split(i)
            curPos = sm.bisect_left(i + 1) - 1
            prePos = curPos - 1
            if prePos < 0:
                return
            (s1, e1), (s2, e2) = sm.peekitem(prePos), sm.peekitem(curPos)
            if a[s1] == a[s2]:
                sm.popitem(curPos)
                sm[s1] = e2
                sl.remove(e2 - s2 + 1)
                sl.remove(e1 - s1 + 1)
                sl.add(e2 - s1 + 1)

        i = 0
        for _, group in groupby(s):
            lan = len(list(group))
            sm[i] = i + lan - 1
            sl.add(lan)
            i += lan

        ans = []
        for c, i in zip(queryCharacters, queryIndices):
            if a[i] != c:
                a[i] = c
                union(i)
                if i < len(a) - 1: 
                    union(i + 1)
            ans.append(sl[0])
        return ans