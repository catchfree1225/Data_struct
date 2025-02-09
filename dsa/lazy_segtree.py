class SegTree:
    def __init__(self, n, arr=[]):
        self.n = n
        self.sum = [0] * (n * 2)
        self.add_tag = [0] * (n * 2)
        if arr: self.build(list(arr))
        
    @staticmethod
    def pos(i, l, r):
        ln = (r - l + 2) >> 1
        return i + 1, i + ln * 2, l + ln - 1
    
    def mark(self, i, sz, val):
        self.sum[i] += val * sz
        self.add_tag[i] += val
    
    def pull(self, order):
        while order:
            i, ln = order.pop()
            self.sum[i] = self.sum[i + 1] + self.sum[i + ln * 2]

    def push(self, i, l, r):
        if self.add_tag[i]:
            lc, rc, m = self.pos(i, l, r)
            self.mark(lc, m - l + 1, self.add_tag[i])
            self.mark(rc, r - m, self.add_tag[i])
            self.add_tag[i] = 0
            
    def build(self, arr):
        st = [(0, 1, self.n)]
        order = []
        while st:
            i, l, r = st.pop()
            if l == r:
                self.sum[i] = arr[l - 1]
                continue
            lc, rc, m = self.pos(i, l, r)
            order.append((i, m - l + 1))
            st.append((lc, l, m))
            st.append((rc, m + 1, r))
        self.pull(order)
    
    def add(self, s, e, val):
        st = [(0, 1, self.n)]
        order = []
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                self.mark(i, r - l + 1, val)
                continue
            self.push(i, l, r)
            lc, rc, m = self.pos(i, l, r)
            order.append((i, m - l + 1))
            if s <= m: st.append((lc, l, m))
            if m < e: st.append((rc, m + 1, r))
        self.pull(order)
    
    def query(self, s, e):
        st = [(0, 1, self.n)]
        res = 0
        while st:
            i, l, r = st.pop()
            if s <= l and r <= e:
                res += self.sum[i]
                continue
            self.push(i, l, r)
            lc, rc, m = self.pos(i, l, r)
            if s <= m: st.append((lc, l, m))
            if m < e: st.append((rc, m + 1, r))
        return res