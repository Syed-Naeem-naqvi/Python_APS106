class BNode:
    def __init__(self, cargo=None, l=None, r=None):
        self.cargo = cargo
        self.left = l
        self.right = r

    def __str__(self):
        return str(self.cargo)


class BinaryTree:
    def __init__(self):
        self.size = 0
        self.root = None
    
    def min(self):
        min_node = self.root
        
        # TODO #
        # Hint: Utilize the code for the sum function!
        counter = 0
        this_level = [self.root]
        while this_level:
            next_level = []
            min_nodes = {}
            for node in this_level:
                min_nodes[node] = counter
                if node.cargo < min_node.cargo:
                    min_node = node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                counter += 1
            this_level = next_level

        node_vals = []
        levels = []
        for node in min_nodes.keys():
            node_vals.append(node.cargo)
        for val in min_nodes.values():
            levels.append(val)

        for node, value in min_nodes.items():
            if node.cargo == min(node_vals) and value == min(node_vals):
                min_node = node
        return min_node

    def sum(self):
        '''sums up the cargos of the elements in the tree'''
        
        acc = 0
        this_level= [self.root]

        while this_level:
            next_level= list()
                
            for n in this_level:
                acc += n.cargo                   
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
               
            this_level = next_level
                
        return(acc)

    def print_tree(self):
        '''prints tree level by level'''
        
        this_level= [self.root]

        while this_level:
            next_level= list()

            for n in this_level:
                print (n.cargo, " ", end = " ")
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
                    
            print("\n")
            this_level = next_level


n1 = BNode(0)
# TODO #
# Add nodes and connect them!


t = BinaryTree()
t.root = n1
t.size = 6
t.root.left = BNode(1, BNode(-8), BNode(4))
t.root.right = BNode(2, BNode(-5), BNode(6))
t.print_tree()

# Works
print(t.min())

