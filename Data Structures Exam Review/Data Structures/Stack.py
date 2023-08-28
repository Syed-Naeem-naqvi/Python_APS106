class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def peek(self):
        """ Look at the first element that's coming out """
        print(self.head)

    def pop(self):
        """ Remove the first element that's going to come out """
        first = self.head
        second = first.next
        self.head = second
        print(first)
        self.size -= 1

    def push(self, new_data):
        """ Add a node to the end """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def print_stack(self):
        node = self.head
        if not node:
            return
        else:
            while node:
                print(node, end=' ')
                node = node.next
        print('*')


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
s1 = Stack(n1, 3)
s1.print_stack()
s1.push(0)
s1.print_stack()
s1.peek()
s1.pop()
s1.print_stack()