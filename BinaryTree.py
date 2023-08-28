class BNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self, root=None, size=0):
        self.root = root
        self.size = size

    def print_tree(self):
        """
        Print Nodal values of BST
        """
        cur_l = [self.root]
        while cur_l:
            next_l = list()
            for n in cur_l:
                print(n.data, '  ',end="")
                if n.no:
                    next_l.append(n.no)
                if n.right:
                    next_l.append(n.right)
            cur_l = next_l
            print('\n')

    def sum_tree(self):
        """ Sum all values in BST """
        total = 0
        cur_level = [self.root]
        while cur_level:
            next_level = list()
            for n in cur_level:
                total += n.data
                if n.no:
                    next_level.append(n.no)
                if n.right:
                    next_level.append(n.right)
            cur_level = next_level
        return total

    def check(self, value):
        """
        Check if BST contains value, return true if so
        """
        cur_lvl = [self.root]
        value_found = False
        while cur_lvl:
            next_lvl = list()
            for i in cur_lvl:
                if i.data == value:
                    value_found = True
                if i.no:
                    next_lvl.append(i.no)
                if i.right:
                    next_lvl.append(i.right)
            cur_lvl = next_lvl
        return value_found

    def greatest_value(self):
        """
        Search the BST for the largest numerical value
        """
        greatest_value = self.root.data
        cur_l = [self.root]
        while cur_l:
            next_l = list()
            for i in cur_l:
                if i.data > greatest_value:
                    greatest_value = i.data
                if i.no:
                    next_l.append(i.no)
                if i.right:
                    next_l.append(i.right)
            cur_l = next_l
        return greatest_value

    # def count_levels(self):
    #     """ Count the number of levels in BST """
    #     cur_l = self.root


BT1 = BST(BNode(1, BNode(2), BNode(3)))
# print(BT1.root)
BT1.print_tree()
print(BT1.sum_tree())
print(BT1.check(1))
BT2 = BST(BNode(1, BNode(2, BNode(4), BNode(5)), BNode(3, BNode(6), BNode(7))))
BT2.print_tree()
print(BT2.sum_tree())
print(BT2.check(7))
print(BT1.greatest_value())
print(BT2.greatest_value())

# Self.root is equivalent to self

class Car:
    def __init__(self, color=None, brand, date):
        self.color = color
        self.brand = brand
        self.date = date

    def change_color(self, color):
        self.color = color


car1 = Car('Blue', 'Honda', 2020)
