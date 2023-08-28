class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    """     Supported Functionality:

            __str__ and print_list()-> Print list
            print_list_backwards() -> Print Backwards
            add_to_end() -> Add node to end
            add_to_front() -> Add node to front
            remove_node() -> Remove node at given index
            add_node() -> Add specified node at given index
            update_node() -> Update data of node at given index
            sum_nodes() -> Add all node values
            detect_cycle() -> Returns True if the linked list has a cycle

    """
    def __init__(self, head=None, length=0):
        self.head = head
        self.length = length

    def __str__(self):
        """ Traverse while the head is not None and print"""
        output = ''
        head = self.head
        if head is None:
            output += '[]'
        else:
            while head:
                output += '[' + str(head) + '] -> '
                head = head.next
            output += 'None'
        return output

    def print_list(self):
        """ Traverse while the head is not None and print"""
        head = self.head
        if head is None:
            print('[]')
        else:
            while head:
                print('[' + str(head) + '] ->', end=' ')
                head = head.next
            print('None')

    def print_list_backwards(self):
        """ Save Nodes to a list, print them"""
        backwards = []
        head = self.head
        if head is None:
            print('[]')
        else:
            while head:
                backwards = [head] + backwards
                head = head.next
            for node in backwards:
                print('[' + str(node) + '] ->', end=' ')
                node = node.next
            print('None')

    def add_to_end(self, node_to_add):
        """ Add a specified Node to the end"""
        node = self.head
        if node is None:
            self.head = node
        else:
            while node.next is not None:
                node = node.next
            node.next = node_to_add
        self.length += 1

    def add_to_front(self, node_to_add):
        """ Make specified Node the new head """
        old_head = self.head
        node_to_add.next = old_head
        self.head = node_to_add
        self.length += 1

    def remove_node(self, position):
        """ Remove the node at the index = position"""
        node = self.head
        list_index = 0
        while node is not None and list_index + 1 < position:
            node = node.next
            list_index += 1

        one_before = node
        one_after = node.next.next
        one_before.next = one_after
        self.length -= 1

    def insert_node(self, position, to_add):
        """ Remove the node at the index = position"""
        node = self.head
        list_index = 0
        while node is not None and list_index + 1 < position:
            node = node.next
            list_index += 1

        one_before = node
        one_after = node.next
        one_before.next = to_add
        to_add.next = one_after
        self.length += 1

    def update_node(self, position, new_data):
        """ Remove the node at the index = position"""
        node = self.head
        list_index = 0
        while node is not None and list_index < position:
            node = node.next
            list_index += 1
        node.data = new_data

    def sum_nodes(self):
        """ Add up all node values """
        total = 0
        node = self.head
        if node is None:
            return total
        else:
            while node is not None:
                total += node.data
                node = node.next
            return total

    def detect_cycle(self):
        """ Returns True if List has cycle(s) """
        slow = self.head
        fast = self.head
        if self.head is None:
            return False
        else:
            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return True
            else:
                return False



def print_nodes(node):
    """ Basic print, nothing fancy """
    while node:
        print(node, end=' ')
        node = node.next


n1 = Node(1, Node(2, Node(3, Node(4))))
# print_nodes(n1)                       # 1 2 3 4, ugly print
L1 = LinkedList(n1, 4)
L1.print_list()                         # [1] -> [2] -> [3] -> [4] -> None
print(L1.length)                        # 4
L2 = LinkedList()                       # Empty, head is None
L2.print_list()                         # []

L1.print_list_backwards()               # [4] -> [3] -> [2] -> [1] -> None
L1.add_to_end(Node(5))                  # Add the node [5] to end and update length
L1.print_list()                         # [1] -> [2] -> [3] -> [4] -> [5] -> None
print(L1.length)                        # 5

L1.add_to_front(Node(0))
L1.print_list()                         # [0] -> [1] -> [2] -> [3] -> [4] -> [5] -> None
print(L1)                               # [0] -> [1] -> [2] -> [3] -> [4] -> [5] -> None
L1.remove_node(3)                       # Remove node at index = 3
print(L1)                               # [0] -> [1] -> [2] -> [4] -> [5] -> None
L1.remove_node(4)
print(L1)                               # [0] -> [1] -> [2] -> [4] -> None

L1.add_to_end(Node(5))
print(L1)                               # [0] -> [1] -> [2] -> [4] -> [5] -> None
L1.insert_node(3, Node(3))              # Insert a Node with 3 at position 3
print(L1)                               # [0] -> [1] -> [2] -> [3] -> [4] -> [5] -> None
L1.update_node(1, 10)                   # Update data of Node at index 1 to 10
print(L1)                               # [0] -> [10] -> [2] -> [3] -> [4] -> [5] -> None
print(L1.length)                        # 6

print(L1.sum_nodes())                   # 24

# Make a cyclic list
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node3
L3 = LinkedList(node1, 4)
print(L3.detect_cycle())                # True






