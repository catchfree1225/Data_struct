import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
inf = int(1e18)
def max(a, b): return a if a > b else b

class SegTree:
    def __init__(self, init):
        self.n = len(init)
        m = 2 << self.n.bit_length()
        self.sum = [0] * m
        self.max = [-inf] * m
        self.maxCnt = [0] * m
        self.sem = [-inf] * m
        self.maxHistory = [-inf] * m
        # 懶信息
        self.maxAdd = [0] * m
        self.otherAdd = [0] * m
        self.maxUp = [0] * m
        self.otherUp = [0] * m
        self.build(init)
    
    def apply(self, i, n, maxAddv, otherAddv, maxUpv, otherUpv):
        self.maxHistory[i] = max(self.maxHistory[i], self.max[i] + maxUpv)
        self.maxUp[i] = max(self.maxUp[i], self.maxAdd[i] + maxUpv)
        self.otherUp[i] = max(self.otherUp[i], self.otherAdd[i] + otherUpv)
        self.sum[i] += maxAddv * self.maxCnt[i] + otherAddv * (n - self.maxCnt[i])
        self.max[i] += maxAddv
        if self.sem[i] != -inf:
            self.sem[i] += otherAddv
        self.maxAdd[i] += maxAddv
        self.otherAdd[i] += otherAddv

    def pull(self, order):
        for i in reversed(order):
            l, r = i << 1, i << 1 | 1
            self.maxHistory[i] = max(self.maxHistory[l], self.maxHistory[r])
            self.sum[i] = self.sum[l] + self.sum[r]
            self.max[i] = max(self.max[l], self.max[r])
            if self.max[l] > self.max[r]:
                self.maxCnt[i] = self.maxCnt[l]
                self.sem[i] = max(self.sem[l], self.max[r])
            elif self.max[l] < self.max[r]:
                self.maxCnt[i] = self.maxCnt[r]
                self.sem[i] = max(self.max[l], self.sem[r])
            else:
                self.maxCnt[i] = self.maxCnt[l] + self.maxCnt[r]
                self.sem[i] = max(self.sem[l], self.sem[r])
            
    def push(self, i, l, r):
        m = (l + r) >> 1
        ln, rn = m - l + 1, r - m
        l, r = i << 1, i << 1 | 1
        mx = max(self.max[l], self.max[r])
        if self.max[l] == mx:
            self.apply(l, ln, self.maxAdd[i], self.otherAdd[i], self.maxUp[i], self.otherUp[i])
        else:
            self.apply(l, ln, self.otherAdd[i], self.otherAdd[i], self.otherUp[i], self.otherUp[i])
        if self.max[r] == mx:
            self.apply(r, rn, self.maxAdd[i], self.otherAdd[i], self.maxUp[i], self.otherUp[i])
        else:
            self.apply(r, rn, self.otherAdd[i], self.otherAdd[i], self.otherUp[i], self.otherUp[i])
        self.maxAdd[i] = self.otherAdd[i] = self.maxUp[i] = self.otherUp[i] = 0

    def build(self, init):
        st = [(1, 1, self.n)]
        order = []
        while st:
            i, l, r = st.pop()
            if l == r:
                self.sum[i] = self.max[i] = self.maxHistory[i] = init[l - 1]
                self.maxCnt[i] = 1
            else:
                m = (l + r) >> 1
                st.append((i << 1, l, m))
                st.append((i << 1 | 1, m + 1, r))
                order.append(i)
        self.pull(order)
    
    def updateAdd(self, s, e, val):
        st = [(1, 1, self.n)]
        order = []
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                self.apply(i, r - l + 1, val, val, val, val)
                continue
            m = (l + r) >> 1
            self.push(i, l, r)
            if s <= m: st.append((i << 1, l, m))
            if m < e: st.append((i << 1 | 1, m + 1, r))
            order.append(i)
        self.pull(order)
    
    def updateMin(self, s, e, val):
        st = [(1, 1, self.n)]
        order = []
        while st:
            i, l, r = st.pop()
            if val >= self.max[i]:
                continue
            if s <= l and r <= e and self.sem[i] < val:
                self.apply(i, r - l + 1, val - self.max[i], 0, val - self.max[i], 0)
                continue
            m = (l + r) >> 1
            self.push(i, l, r)
            if s <= m: st.append((i << 1, l, m))
            if m < e: st.append((i << 1 | 1, m + 1, r))
            order.append(i)
        self.pull(order)
    
    def queryMax(self, s, e, tp):
        st = [(1, 1, self.n)]
        res = -inf
        arr = self.maxHistory if tp == 'History' else self.max
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                res = max(res, arr[i])
                continue
            m = (l + r) >> 1
            self.push(i, l, r)
            if s <= m: st.append((i << 1, l, m))
            if m < e: st.append((i << 1 | 1, m + 1, r))
        return res
    
    def querySum(self, s, e):
        st = [(1, 1, self.n)]
        res = 0
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                res += self.sum[i]
                continue
            m = (l + r) >> 1
            self.push(i, l, r)
            if s <= m: st.append((i << 1, l, m))
            if m < e: st.append((i << 1 | 1, m + 1, r))
        return res

def solve():
    tr = SegTree(a)
    for _ in range(m):
        q = tuple(MII())
        if q[0] == 1:  # 範圍增加
            tr.updateAdd(q[1], q[2], q[3])
        elif q[0] == 2:  # 範圍修改成較小值(剪枝)
            tr.updateMin(q[1], q[2], q[3])
        elif q[0] == 3:  # 範圍求和
            print(tr.querySum(q[1], q[2]))
        elif q[0] == 4:  # [l, r]目前的最大值
            print(tr.queryMax(q[1], q[2], 'Current'))
        else:  # [l, r]历史最大值的最大值
            print(tr.queryMax(q[1], q[2], 'History'))

for _ in range(1):
    n, m = MII()
    a = list(MII())
    solve()