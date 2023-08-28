# Linked lists

class Node:
    def __init__(self, cargo=None, next=None):  # store data and a link
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)



n1 = Node(0)
n2 = Node('abc')
n1.cargo = 1        # Can change data
print(n1)           # Can print the node
print(n2)

n1 = Node(1)
n2 = Node(2)
n1.next = n2
print(n1)           # Node 2 is connected to Node 1 now
print(n1.next)      # Now, looking up Node 1's .next attribute sends us to Node 2, creating a link

# Second Node doesn't know its being linked to

node1 = Node(1)     # This one is the head
node2 = Node(2)
node3 = Node(3)     # This one is the tail (last)
node1.next = node2
node2.next = node3

print(node1, node1.next, node1.next.next)

# All you need to access the list is the address of the head
# We can define any linked data structure now
# Ignore the node to kill it
# Check if the node we are visiting is pointing to another node or not

n1 = Node(10)
n2 = Node(11)
n3 = Node(12)
n1.next = n2
n2.next = n3


def print_node(node):
    while node is not None:
        print(node, end= " ")
        node = node.next


print_node(n2)  # Calling the function on a non-header still traverses.











