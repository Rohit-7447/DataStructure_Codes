class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key == root.key:
            print(f"{key}, Duplicate key can't insert. Ignored...")
            return root
        
        if key<root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root
    
    def find_min(self,root):
        current = root
        while current.left:
            current = current.left
        return current
    
    def delete(self,root,key):
        if root is None:
            return root
        if key<root.key:
            root.left = self.delete(root.left,key)
        elif key>root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
        #Node with two children: Get the inorder successor(smallest in the right subtree)
        temp = self.find_min(root.right)
        #copy the inorder successor's content to this node
        root.key = temp.key

        root.right = self.delete(root.right, temp.key)

        return root

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key,end =" ")
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.key,end =" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end = " ")

if __name__ == "__main__":
    bst = BinarySearchTree()

    nodes = [50,30,20,40,70,60,80,70]
    for key in nodes:
        bst.root = bst.insert(bst.root,key)
    
    print("Inorder Traversal: ")
    bst.inorder(bst.root)
    print("\n")

    print("Preorder Traversal: ")
    bst.preorder(bst.root)
    print("\n")

    # print("PostOrder Traversal: ")
    # bst.postorder(bst.root)
    # print("\n")

    bst.root = bst.delete(bst.root,50)
    bst.inorder(bst.root)
    print("\n")