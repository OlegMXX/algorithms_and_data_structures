class Entry:
    def __init__(self, v, p):
        self.value = v
        self.priority = p

    def __repr__(self):
        return self.value


class PQ:
    def less(self, i, j):
        return self.storage[i].priority < self.storage[j].priority

    def swap(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def __init__(self, size):
        self.size = size
        self.storage = [None] * (size + 1)
        self.N = 0

    def __repr__(self):
        storage_list = ["",]
        for entry in range(self.N + 1):
            if self.storage[entry]:
                storage_list.append(f"[{self.storage[entry].value}, {self.storage[entry].priority}]")
                if entry in [1, 3, 7, 15]:
                    storage_list.append("\n")
        return " ".join(storage_list)

    def enqueue(self, v, p):
        if self.N == self.size:
            raise RuntimeError('Priority Queue is Full!')
        self.N += 1
        self.storage[self.N] = Entry(v, p)
        self.swim(self.N)

    def swim(self, child):
        while child > 1 and self.less(child // 2, child):
            self.swap(child, child // 2)
            child = child // 2

    def dequeue(self):
        if self.N == 0:
            raise RuntimeError('Priority Queue is empty!')
        max_entry = self.storage[1]
        self.storage[1] = self.storage[self.N]
        self.storage[self.N] = None
        self.N -= 1
        self.sink(1)
        return max_entry.value

    def sink(self, parent):
        while 2 * parent <= self.N:
            child = 2 * parent
            if child < self.N and self.less(child, child + 1):
                child += 1
            if not self.less(parent, child):
                break
            self.swap(child, parent)
            parent = child





pq = PQ(15)

pq.enqueue("d", 4)
print("start", pq)
pq.enqueue("l", 12)
print(pq)
pq.enqueue("b", 2)
print(pq)
pq.enqueue("a", 1)
print(pq)
pq.enqueue("z", 26)
print(pq)
pq.enqueue("i", 9)
print(pq)
pq.enqueue("r", 18)
print(pq)
pq.enqueue("v", 22)
print(pq)
pq.enqueue("t", 20)
print(pq)
pq.enqueue("g", 7)
print(pq)
print(pq.dequeue())
print(pq)
