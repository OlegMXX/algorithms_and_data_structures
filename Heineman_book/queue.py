class Node:
    def __init__(self, val):
        self.value = val
        self.next = None



class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def __repr__(self):
        node = self.first
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def is_empty(self):
        return self.first is None

    def enqueue(self, val):
        if self.first is None:
            self.first = self.last = Node(val)
        else:
            self.last.next = Node(val)
            self.last = self.last.next

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError('Queue is empty')
        val = self.first.value
        self.first = self.first.next
        return val


my_queue = Queue()
print(my_queue.is_empty())

my_queue.enqueue("a")
my_queue.enqueue("b")
my_queue.enqueue("c")

print(my_queue)
print(my_queue.dequeue())
print(my_queue)
