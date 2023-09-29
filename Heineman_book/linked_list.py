

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        # первый элемент переданного списка передается в объект узла, который назначается head`ом, затем удаляется
        if nodes:
            node = Node(val=nodes.pop(0))
            self.head = node
            # проход по оставшимся элементам - создание объекта следующего узла с передачей ссылки на него в .next
            for elem in nodes:
                node.next = Node(val=elem)
                # перед следующей итерацией переходим в следующий объект узла, который только что вписали в ссылку
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise RuntimeError("List is empty")

        for node in self:
            if node.value == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise RuntimeError(f'Node with data {target_node_data} not found')

    def add_before(self, target_node_data, new_node):

        if self.head is None:
            raise RuntimeError("List is empty")

        if self.head.value == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head

        for node in self:
            if node.value == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise RuntimeError("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):

        if self.head is None:
            raise Exception("List is empty")

        if self.head.value == target_node_data:
            self.head = self.head.next
            return
        previous_node = self.head

        for node in self:
            if node.value == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise RuntimeError("Node with data '%s' not found" % target_node_data)

# init linked list
llist = LinkedList(["a", "b", "c"])
print(llist)

# iter linked list
for node in llist:
    print(node)

# add the first node
llist.add_first(Node("aa"))
print(llist)

# add the last node
llist.add_last(Node("d"))
print(llist)

# add after
llist.add_after("b", Node("bb"))
print(llist)

# add before
llist.add_before("b", Node("aa"))
print(llist)

# remove
llist.remove_node("c")
print(llist)