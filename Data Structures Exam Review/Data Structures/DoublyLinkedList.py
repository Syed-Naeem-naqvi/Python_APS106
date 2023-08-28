class Node:
    def __init__(self, data=None, next=None, back=None):
        self.data = data
        self.next = next
        self.back = back

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    """         Supported Functionality:

                __str__ and print_list()-> Print list
                print_list_backwards() -> Print Backwards
                add_to_end() -> Add node to end
                add_to_front() -> Add node to front
                remove_node() -> Remove node at given index
                add_node() -> Add specified node at given index
                update_node() -> Update data of node at given index
                sum_nodes() -> Add all node values

    """
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def __str__(self):
        """ Traverse while the head is not None and print"""
        output = ''
        head = self.head
        if head is None:
            output += '[]'
        else:
            while head:
                output += '[' + str(head) + '] <-> '
                head = head.next
            output += 'None'
            output = 'None <-> ' + output
        return output

    def print_list_backwards(self):
        """ Start at tail, get to head """
        node = self.tail
        print('None <->', end='')
        while node is not None:
            print(' [' + str(node) + '] <->', end='')
            node = node.back
        print(' None')

    def add_to_end(self, data):
        """ Add data to end of list """
        to_add = Node(data)
        last_node = self.tail
        last_node.next = to_add
        to_add.back = last_node
        self.length += 1

    def add_to_front(self, data):
        """ Add data to front of list """
        to_add = Node(data)
        first_node = self.head
        to_add.next = first_node
        first_node.back = to_add
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
        to_add = Node(to_add)
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
        total = 0
        node = self.head
        if node is None:
            return total
        else:
            while node is not None:
                total += node.data
                node = node.next
            return total


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.back = n1
n2.next = n3
n3.back = n2
L1 = DoublyLinkedList(n1, n3, 3)
print(L1)                               # None <-> [1] <-> [2] <-> [3] <-> None
L1.print_list_backwards()               # None <-> [3] <-> [2] <-> [1] <-> None
L1.add_to_end(4)                        # Add node to end of list
print(L1)                               # None <-> [1] <-> [2] <-> [3] <-> [4] <-> None
L1.remove_node(2)                       # Remove node at index 2
print(L1)                               # None <-> [1] <-> [2] <-> [4] <-> None
L1.insert_node(2, 3)                    # Insert Node at index 2
print(L1)                               # None <-> [1] <-> [2] <-> [3] <-> [4] <-> None
L1.update_node(1, 10)                   # Update Node at index 1 to 10
print(L1)                               # None <-> [1] <-> [10] <-> [3] <-> [4] <-> None
print(L1.sum_nodes())                   # 18




