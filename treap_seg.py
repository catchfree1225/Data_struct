from random import random as rnd
class TNode:
    __slots__ = 'k', 'l', 'r', 'sz', 'p', 'sum', 'add_tag'
    def __init__(self, k):
        self.k = k
        self.l = self.r = None
        self.sz = 1
        self.p = rnd()
        self.sum = k
        self.add_tag = 0
    
    def mark(self, val):
        self.k += val
        self.sum += val * self.sz
        self.add_tag += val
    
    def pull(self):
        self.sz = 1
        self.sum = self.k
        if self.l: 
            self.sz += self.l.sz
            self.sum += self.l.sum
        if self.r: 
            self.sz += self.r.sz
            self.sum += self.r.sum
    
    def push(self):
        if not self.add_tag: 
            return
        if self.l: self.l.mark(self.add_tag)
        if self.r: self.r.mark(self.add_tag)
        self.add_tag = 0

def split(root, k): # <=k, >k
    st, cur = [], root
    while cur:
        lsz = cur.l.sz if cur.l else 0
        st.append((cur, go_right := k > lsz))
        cur.push()
        if go_right:
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
            l.push()      
            l = l.r
        else:
            r.push()
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
    def __init__(self, arr=[]):
        self.root = self.build(arr)
    
    def build(self, arr):
        st = []
        for x in arr:
            node = TNode(x)
            while st and st[-1].p > node.p:
                node.l = st.pop()
                node.l.pull()
            if st:
                st[-1].r = node
            st.append(node)

        root = st[0] if st else None
        while st:
            st.pop().pull()
        return root
    
    def add(self, s, e, x):
        l, r = split(self.root, e)
        ll, lr = split(l, s - 1)
        if lr: lr.mark(x)   
        self.root = merge(merge(ll, lr), r)
    
    def sum(self, s, e):
        l, r = split(self.root, e)
        ll, lr = split(l, s - 1)
        ans = lr.sum if lr else 0
        self.root = merge(merge(ll, lr), r)
        return ans