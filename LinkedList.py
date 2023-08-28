# Write all functions without notes

class Node:

    def __init__(self, cargo=None, next_=None):
        self.cargo = cargo
        self.next = next_

    def __str__(self):
        return str(self.cargo)


class LinkedList:

    def __init__(self, head=None, length=0):
        self.head = head
        self.length = length

    # Add Note to front

    def add_to_front(self, cargo):
        node = self.head            # look at head
        new_node = Node(cargo)      # Turn the data you want to add into a Node

        new_node.next = node        # Say the new nodes next attribute is the current head
        self.head = new_node        # make the new node the new head

        self.length += 1            # Increment the length

    # Add Node to end

    def add_to_end(self, cargo):
        node = self.head            # Call the current head node
        new_node = Node(cargo)      # Turn the cargo you want to add a node
        while node.next is not None:
            node = node.next        # Go through the linked list while the current nodes next method is not none, when it is, it is the last node

        node.next = new_node        # now, make the last node's next method none (it's the new last)
        self.length += 1            # Increment length

    # Add a second linked list to the end

    def add_list_to_end(self, another_linked_list):
        # First, get to the last node
        node = self.head
        second_head = another_linked_list.head
        while node.next is not None:
            node = node.next
        node.next = second_head
        self.length += another_linked_list.length

    # Print The Lined List

    def __str__(self):
        n = self.head
        rep = ''
        while n is not None:
            rep += str(n) + ' '
            n = n.next
        return rep

    # Find cycles

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while slow.next is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                print('Contains cycle')
            else:
                print('No cycle found')


def print_list(node):
    while node is not None:
        print(node, end=' ')
        node = node.next


node1 = Node('B')
node2 = Node('A')
node3 = Node('C')

# print(node1)
# print_list(node1)
L1 = LinkedList(node1, 1)
L1.add_to_front(node2)
# print_list(L1.head)
L1.add_to_end(node3)
# print_list(L1.head)
# print(L1.length)
na = Node('a')
nb = Node('b')
nc = Node('c')

L2 = LinkedList(na, 1)
L2.add_to_end(nb)
L2.add_to_end(nc)
# print_list(L2.head)
L1.add_list_to_end(L2)
# print_list(L1.head)
# print(L1.length)
L1.add_to_end(2)
# print_list(L1.head)
# print(L1.length)
# print(L1)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
LL = LinkedList()
LL.add_to_front(n1)
LL.add_to_end(n2)
LL.add_to_end(n3)
print(LL)


class BNode:
    def __init__(self, cargo=None, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


a = BNode(1)
b = BNode(2)






