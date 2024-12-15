class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Fix 1: Corrected the insert function to handle `None` cases properly and avoid overwriting the root.
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key == root.key:
            print(f"{key} is a duplicate key and can't be inserted. Ignored....")
            return root

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    # Fix 2: Corrected the search function to handle search properly without recursion returning `None`.
    def search(self, root, key):
        if root is None:
            return False  # Key not found

        if root.key == key:
            return True  # Key found

        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Inorder traversal (Left, Root, Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # Preorder traversal (Root, Left, Right)
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal (Left, Right, Root)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    # Find the depth of the BST
    def tree_depth(self, root):
        if root is None:
            return 0
        left_depth = self.tree_depth(root.left)
        right_depth = self.tree_depth(root.right)
        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    bst = BinarySearchTree()

    # Fix 3: Corrected prompt and ensured inputs are properly handled.
    nodes = list(map(int, input("Enter the elements to insert into the binary tree (space-separated): ").split()))
    for key in nodes:
        bst.root = bst.insert(bst.root, key)

    # Inorder traversal
    print("\nInorder Traversal:")
    bst.inorder(bst.root)
    print("\n")

    # Preorder traversal
    print("Preorder Traversal:")
    bst.preorder(bst.root)
    print("\n")

    # Postorder traversal
    print("Postorder Traversal:")
    bst.postorder(bst.root)
    print("\n")

    # Search for a key
    nodetoSearch = int(input("Enter the key to search in the BST: "))
    if bst.search(bst.root, nodetoSearch):
        print(f"Key {nodetoSearch} found in the BST.")
    else:
        print(f"Key {nodetoSearch} not found in the BST.")

    # Depth of the BST
    depth = bst.tree_depth(bst.root)
    print(f"\nThe depth of the BST is: {depth}")
