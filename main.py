from Tree import Binary_Tree

data = [20,6,17,5,2,19,7,13]
my_tree = Binary_Tree()

my_tree.create_tree(data)

print("Pre-Order")
my_tree.travers_preorder(my_tree.root)

print("\nPost-Order")
my_tree.travers_postorder(my_tree.root)

print("\nLevel-Order")
my_tree.travers_levelorder(my_tree.root)

print("\nContain node? ",my_tree.contain_node(5))

print("\nFind smallest value in the tree: ",my_tree.find_smallest(my_tree.root))

print("\nDelete a node ")
my_tree.delete_recursion(my_tree.root,13)

print("\nLevel-Order - After deleting a node")
my_tree.travers_levelorder(my_tree.root)


# ©Zairul Mazwan©