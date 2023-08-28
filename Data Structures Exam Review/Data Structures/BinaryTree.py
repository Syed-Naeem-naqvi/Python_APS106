class BNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    """         Supported Functionality

                print() -> __str__ print
                print_tree() -> Print binary tree level by level
                sum_tree() -> Ass up all nodes
                max_node() -> Returns the largest node
                min_node() -> Returns the smallest node
                replace() -> Replaces specified node with new data
                add_node() -> Adds node to specified location
                #############################################
                merge_trees() -> Adds two trees together with a new root

    """
    def __init__(self, root=None, size=0):
        self.root = root
        self.size = size

    def __str__(self):
        output = ''
        current_level = [self.root]
        while current_level:
            next_level = []
            for node in current_level:
                output += str(node.data) + '  '
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            output += '\n'
            current_level = next_level
            output += '\n'
        return output

    def print_tree(self):
        """ Print tree level by level """
        current_level = [self.root]
        while current_level:
            next_level = []
            for node in current_level:
                print(node.data,' ', end='')
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            print('\n')
            current_level = next_level

    def sum_tree(self):
        """ Find the sum of all nodes """
        total = 0
        current_level = [self.root]
        while current_level:
            next_level = []
            for node in current_level:
                total += node.data
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
        return total

    def max_node(self):
        """ Finds and returns the largest node value """
        current_level = [self.root]
        max_node = self.root
        while current_level:
            next_level = []
            for node in current_level:
                if node.data > max_node.data:
                    max_node = node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
        return max_node.data

    def min_node(self):
        """ Finds and returns the smallest node value """
        current_level = [self.root]
        min_node = self.root
        while current_level:
            next_level = []
            for node in current_level:
                if node.data < min_node.data:
                    min_node = node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
        return min_node.data

    def replace(self, num, new_data):
        """ Replace node number num with new data """
        current_level = [self.root]
        while current_level:
            next_level = []
            for node in current_level:
                if node.data is num:
                    node.data = new_data
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level

    def add_node(self, num, data, side):
        """ Add node at specified location """
        current_level = [self.root]
        while current_level:
            next_level = []
            for node in current_level:
                if node.data == num and side == 'left':
                    node.left = BNode(data)
                elif node.data == num and side == 'right':
                    node.right = BNode(data)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level


def merge_trees(new_root, tree1, tree2):
    new_root.left = tree1.root
    new_root.right = tree2.root
    total_size = tree1.size
    total_size += tree2.size
    new_tree = BinaryTree(new_root, total_size)
    return new_tree


n1 = BNode(1, BNode(2, BNode(4), BNode(5)), BNode(3, BNode(6), BNode(7)))
B1 = BinaryTree(n1, 7)
B1.print_tree()
                                #       1
                                #
                                #      2  3
                                #
                                #   4  5  6  7

print(B1.sum_tree())            # 28
print(B1)
                                #       1
                                #
                                #      2  3
                                #
                                #   4  5  6  7

print(B1.max_node())            # 7
print(B1.min_node())            # 1
print(B1.replace(5, 15))
print(B1)
                                #       1
                                #
                                #      2  3
                                #
                                #   4  15  6  7

B1.add_node(4, 20, 'left')
B1.add_node(4, 21, 'right')
print(B1)
                                #        1
                                #
                                #       2  3
                                #
                                #    4  15  6  7
                                #
                                #  20  21


B2 = BinaryTree(BNode(10, BNode(50), BNode(60)), 3)
new = merge_trees(BNode(0), B1, B2)
print(new)
                                #             0
                                #
                                #          1     10
                                #
                                #       2    3  50  60
                                #
                                #     4   15 6  7
                                #
                                #   20  21

