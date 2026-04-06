class Node:
    def __init__(self,data):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent_node = None
def insert(root,val):
    if root is None:
        return Node(val)
    else:
        if val <= root.data:
            root.left_node = insert(root.left_node, val)
        else:
            root.right_node = insert(root.right_node, val)
    return root
# root = None
# a = [10,40,15,24,8,7,52]
# print(root)
# root = Node(a[0])
# print(root)
# print(root.data)
# b = Node(a[2])
# print(b)
# print(b.data) 
