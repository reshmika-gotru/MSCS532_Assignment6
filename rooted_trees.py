class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def add_child(self, parent_value, child_value):
        """Adds a child to the specified parent node."""
        parent = self.find_node(self.root, parent_value)
        if parent:
            parent.children.append(TreeNode(child_value))
        else:
            print(f"Parent node with value {parent_value} not found.")

    def find_node(self, node, value):
        """Finds and returns the node with the specified value."""
        if node.value == value:
            return node
        for child in node.children:
            found_node = self.find_node(child, value)
            if found_node:
                return found_node
        return None

    def display(self, node=None, level=0):
        """Displays the tree starting from the given node."""
        if node is None:
            node = self.root
        print(" " * (level * 4) + str(node.value))
        for child in node.children:
            self.display(child, level + 1)


# Create a tree with root value 1
tree = Tree(1)

# Add children to the tree
tree.add_child(1, 2)
tree.add_child(1, 3)
tree.add_child(2, 4)
tree.add_child(2, 5)
tree.add_child(3, 6)

# Display the tree
tree.display()