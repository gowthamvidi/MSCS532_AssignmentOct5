import random

class HashTable:
    def __init__(self, size=8):
        self.size, self.t = size, [[] for _ in range(size)]
        p = (1 << 61) - 1
        self.a, self.b, self.p = random.randint(1,p-1), random.randint(0,p-1), p

    def _i(self, k): return ((self.a*(hash(k)&((1<<64)-1))+self.b)%self.p)%self.size
    def insert(self, k, v):
        i = self._i(k)
        for idx,(x,_) in enumerate(self.t[i]):
            if x==k: self.t[i][idx]=(k,v); return
        self.t[i].append((k,v))
    def search(self, k):
        for x,v in self.t[self._i(k)]:
            if x==k: return v
    def delete(self, k):
        i=self._i(k)
        for idx,(x,_) in enumerate(self.t[i]):
            if x==k: del self.t[i][idx]; return True

h=HashTable()
print("Commands: insert <k> <v> | search <k> | delete <k> | exit")
while True:
    c=input(">> ").split()
    if not c: continue
    if c[0]=="insert": h.insert(c[1],c[2]);print("Inserted")
    elif c[0]=="search": print("Value:",h.search(c[1]))
    elif c[0]=="delete": print("Deleted" if h.delete(c[1]) else "Not found")
    elif c[0]=="exit": break
    else: print("Invalid")
