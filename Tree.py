from collections import deque

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class Binary_Tree:

    def __init__(self):
        self.root = None

    def add_recursive(self, current, value):
        if current == None:
            return Node(value)

        if value<current.value:
            current.left = self.add_recursive(current.left, value)
        elif value>current.value:
            current.right = self.add_recursive(current.right,value)
        else:
            return current

        return current

    def add(self, value):
        self.root = self.add_recursive(self.root, value)

    def create_tree(self, data):
        for x in data:
            self.add(x)

    # Root -> Left -> Right
    def travers_preorder(self, node):
        if node != None:
            self.visit(node.value)
            self.travers_preorder(node.left)
            self.travers_preorder(node.right)


    # Left -> Right -> Root
    def travers_postorder(self, node):
        if node != None:
            self.travers_postorder(node.left)
            self.travers_postorder(node.right)
            self.visit(node.value)


    # Visit all not at the same level from left to right
    def travers_levelorder(self, node):
        if node != None:
            Q = []
            Q.append(node)

            while len(Q) != 0:
                n = Q.pop(0)
                self.visit(n.value)

                if n.left != None:
                    Q.append(n.left)

                if n.right != None:
                    Q.append(n.right)


    def search_node(self, current_node, value):
        if current_node == None:
            return False

        if value == current_node.value:
            return True

        res  = self.search_node(current_node.left, value) if value < current_node.value else self.search_node(current_node.right, value)
        return res

    def contain_node(self, value):
        return self.search_node(self.root,value)

    def find_smallest(self, root):
        res = root.value if root.left == None else self.find_smallest(root.left)
        return res

    def delete_recursion(self, current_node, value):
        if current_node == None:
            return None

        if value == current_node.value:
            if (current_node.left == None and current_node.right == None):
                return None

            if current_node.right == None:
                return current_node.left

            if current_node.left == None:
                return current_node.right

            smallest_value = self.find_smallest(current_node.right)
            current_node.value = smallest_value
            current_node.right = self.delete_recursion(current_node.right, smallest_value)
            return current_node

        if value < current_node.value:
            current_node.left = self.delete_recursion(current_node.left, value)
            return current_node

        current_node.right = self.delete_recursion(current_node.right, value)
        return current_node


    def delete_node(self, value):
        self.root = self.delete_recursion(self, self.root, value)

    def visit(self, value):
        print(value, end=" ")




# ©Zairul Mazwan©





