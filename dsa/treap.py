from random import random as rnd
class TNode:
    __slots__ = 'k', 'l', 'r', 'sz', 'p'
    def __init__(self, k):
        self.k = k
        self.l = self.r = None
        self.sz = 1
        self.p = rnd()
    
    def __contains__(self, x):
        cur = self
        while cur:
            if cur.k == x:
                return True
            cur = cur.r if cur.k <= x else cur.l
        return False
    
    def __getitem__(self, k):
        cur = self
        while cur:
            lsz = cur.l.sz if cur.l else 0
            if lsz + 1 == k:
                return cur
            if k <= lsz:
                cur = cur.l
            else:
                k -= lsz + 1
                cur = cur.r
        return None
    
    def __iter__(self):
        st, cur = [], self
        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.l
            else:
                cur = st.pop()
                yield cur.k
                cur = cur.r
    
    def prev(self, x):
        ans, cur = None, self
        while cur:
            if cur.k >= x:
                cur = cur.l
            else:
                ans = cur
                cur = cur.r
        return ans
    
    def next(self, x):
        ans, cur = None, self
        while cur:
            if cur.k <= x:
                cur = cur.r
            else:
                ans = cur
                cur = cur.l
        return ans
    
    def pull(self):
        self.sz = 1
        if self.l: self.sz += self.l.sz
        if self.r: self.sz += self.r.sz

def split(root, k, by_key=True): # <=key, >key
    st, cur = [], root
    while cur:
        lsz = cur.l.sz if cur.l else 0
        go_right = cur.k <= k if by_key else k > lsz
        st.append((cur, go_right))
        if go_right:
            if not by_key:
                k -= lsz + 1
            cur = cur.r
        else:
            cur = cur.l     
    
    t1 = t2 = None
    while st:
        cur, go_right = st.pop()
        if go_right:
            cur.r, t1 = t1, cur 
        else:
            cur.l, t2 = t2, cur
        cur.pull()
    return t1, t2
    
def merge(l, r):
    st = []
    while l and r:
        st.append((l, r))
        if l.p < r.p:         
            l = l.r
        else:
            r = r.l
    
    cur = l or r
    while st:
        l, r = st.pop()
        if l.p < r.p:
            cur, l.r = l, cur
        else:
            cur, r.l = r, cur
        cur.pull()
    return cur

class Treap:
    def __init__(self):
        self.root = None  
        self.bin = []
    
    def _get_node(self, x):
        if self.bin:
            node = self.bin.pop()
            node.k = x
            node.l = node.r = None
            node.sz = 1
            return node
        return TNode(x)
    
    def __len__(self):
        return self.root.sz if self.root else 0
    
    def __contains__(self, x):
        return x in self.root if self.root else False
    
    def __iter__(self):
        if self.root:
            yield from iter(self.root)
    
    def add(self, x):
        l, r = split(self.root, x)
        self.root = merge(merge(l, self._get_node(x)), r)
    
    def remove(self, x):
        l, r = split(self.root, x)
        ll, lr = split(l, x - 1)
        if lr: 
            self.bin.append(lr)
            lr = merge(lr.l, lr.r)
        self.root = merge(merge(ll, lr), r)
    
    def prev(self, x):
        return self.root.prev(x).k if self.root and self.root.prev(x) else None
    
    def next(self, x):
        return self.root.next(x).k if self.root and self.root.next(x) else None
    
    def rank(self, x):
        ans, cur = 0, self.root
        while cur:
            lsz = cur.l.sz if cur.l else 0
            if x <= cur.k:
                cur = cur.l
            else:
                ans += lsz + 1
                cur = cur.r
        return ans + 1
            
    def kth(self, k):
        return self.root[k].k if self.root and self.root[k] else None