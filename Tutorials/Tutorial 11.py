# Tutorial 11

class Node:
    def __init__(self,cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class LinkedList:
    def __init__ (self, length=0, head=None):
        self.length = length         # attribute to keep track of length
        self.head = head        # attribute to keep track of head node

    def add_first(self, cargo):
        """
        Add item to first item of linked list
        """
        node = self.head                # Call the current head 'node'
        new_node = Node(cargo, node)    # call the new head a Node with data = input and next = current head
        self.head = new_node            # make new node the head
        self.length += 1                # Increment length by one

    def add_last(self, cargo):
        node = self.head                # Make current head 'node'
        new_node = Node(cargo)          # Make input a new node with data=cargo and no next
        while node.next is not None:    # Go through the linked list
            node = node.next            # Traverse
        node.next = new_node            # After reaching last node, call its next the ast node
        self.length += 1                # Increment length by one


# create three nodes and assign them to variables
node1 = Node('Node 1')
node2 = Node('Node 2')
node3 = Node('Node 3')
# link the nodes together
node1.next = node2
node2.next = node3


def print_nodes(node):
    while node is not None:
        print(node, end=' -> ')
        node = node.next
    print('None')


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

print_nodes(node1)
l1 = LinkedList(1, n2)
l1.add_first(n1)
l1.add_last(n3)
l1.add_last(n4)
print_nodes(l1.head)
print(l1.length)





