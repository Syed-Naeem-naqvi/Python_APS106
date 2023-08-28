class Node:
    def __init__(self, data=None, no=None, yes=None):
        self.data = data
        self.no = no
        self.yes = yes

    def __str__(self):
        return str(self.data)


question = input('Enter Qn: ')
root = Node(question)
yes_an = input('Enter the animal for which the answer is yes?: ')
root.yes = Node(yes_an)
no_an = input('Enter the animal for which the answer is no?: ')
root.no = Node(no_an)
play = 'y'

while play is 'yes':
    print('Think of animal')
    cur_node = root
    while cur_node.yes is not None and cur_node.no is not None:


