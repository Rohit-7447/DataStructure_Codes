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
            print(f"{key}: Duplicate value can't insert, Ignored.....")

        if key<root.key:
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def mirror_image(self,root):
        if root is None:
            return None

        #Swap the right and left subtrees
        root.left, root.right = root.right, root.left

        #Repeat the process for the left subtree and right subtree
        self.mirror_image(root.left)
        self.mirror_image(root.right)

    def copy_tree(self, root):
        if root is None:
            return None
        
        temp = root
        
        temp.left = self.copy_tree(root.left)
        temp.right = self.copy_tree(root.right)
        return temp
    
    def display_level_wise(self,root):
        if root is None:
            print("Tree is empty")
            return
        
        queue = [root]
        while queue:
            current = queue.pop(0)
            print(current.key, end = " ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
        print()

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

if __name__ == "__main__":
    bst = BinarySearchTree()

    nodes1 = [50,20,30,40,60,70,80]
    nodes = list(map(int,input("Enter nodes to insert in BST: ").split()))
    for key in nodes:
        bst.root = bst.insert(bst.root,key)

    print("Inorder Traversal of Original Tree: ")
    bst.inorder(bst.root)
    
    print("Tree Level-Wise:")
    bst.display_level_wise(bst.root)

    # Create a mirror image of the BST
    print("\nCreating Mirror Image of the Tree...")
    bst.mirror_image(bst.root)

    print("Inorder Traversal of Mirror Image:")
    bst.inorder(bst.root)
    print("\n")

    print("Tree Level-Wise After Mirroring:")
    bst.display_level_wise(bst.root)

    # Create a copy of the BST
    print("\nCreating a Copy of the Tree...")
    copied_tree = bst.copy_tree(bst.root)

    print("Inorder Traversal of Copied Tree:")
    bst.inorder(copied_tree)
    print("\n")

    print("Tree Level-Wise of Copied Tree:")
    bst.display_level_wise(copied_tree)