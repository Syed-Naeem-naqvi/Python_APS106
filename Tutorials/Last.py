class BNode:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


left = BNode(2)
right = BNode(4)
Tree = BNode(0, left, right)
left.left = BNode(6)
right.left = BNode(10)
right.right = BNode(12)
# _____________________________







