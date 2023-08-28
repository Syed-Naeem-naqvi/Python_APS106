class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        exp = '[' + str(self.data) + ']' + '->'
        return exp


def print_contents(node):
    while node is not None:
        print(node, end=' ')
        node = node.next


n1 = Node(1)
n2 = Node(2)
n1.next = n2
print(n1.next)

print_contents(n1)


# Infinite loop
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node2



