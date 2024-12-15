class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,root,key):
        if root is None:
            return Node(key)
        if root.key == key:
            return f"{key}: Duplicate key can't Insert, Ignored..."
        if key<root.key:
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)

        return root
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    def parent_child_nodes(self,root):
        if root:
            if root.left:
                print(f"Parent: {root.key}, Left Child: {root.left.key}")
            if root.right:
                print(f"Parent: {root.key}, Right childe: {root.right.key}")

            self.parent_child_nodes(root.left)
            self.parent_child_nodes(root.right)

    def display_leaf_nodes(self,root):
        if root:
            if root.left is None and root.right is None:
                print(root.key, end=" ")
            self.display_leaf_nodes(root.left)
            self.display_leaf_nodes(root.right)
    
if __name__ == "__main__":

    bst = BinarySearchTree()
    nodes = list(map(int,input("Enter the nodes to insert in BST :(Space Seperated)").split()))
    for key in nodes:
        bst.root = bst.insert(bst.root,key)

    print("Inorder Traversal: ")
    bst.inorder(bst.root)
    print("\n")
    
    print("Preorder Traversal: ")
    bst.preorder(bst.root)
    print("\n")
    
    print("Postorder Traversal: ")
    bst.postorder(bst.root)
    print("\n")

    print("Parent and child Nodes:")
    bst.parent_child_nodes(bst.root)
    print("\n")

    print("Leaf nodes: ")
    bst.display_leaf_nodes(bst.root)
    print("\n")