class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def peek(self):
        """ Look at the first element that's coming out """
        node = self.head
        if not node:
            return
        else:
            while node.next:
                node = node.next
        print(node)

    def pop(self):
        """ Remove the first element that's going to come out """
        node = self.head
        if not node:
            return
        else:
            while node.next.next:
                node = node.next
                node2 = node.next
            to_pop = node
            node.next = None
            print(to_pop)
        self.size -= 1

    def push(self, new_data):
        """ Add a node to the end """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def print_queue(self):
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
q1 = Queue(n1, 3)
# q1.print_queue()
q1.push(4)
# q1.print_queue()
q1.peek()
q1.pop()
q1.print_queue()
q1.pop()
q1.print_queue()
q1.pop()
q1.print_queue()

