class TreeNode: 
    def __init__(self, value): 
         self.value = value 
         self.left = None 
         self.right = None 
class ExpressionTree: 
    def __init__(self): 
        self.root = None 
    def construct_from_postfix(self, postfix): 
        stack = [] 
        for char in postfix: 
            if char.isalnum(): 
                stack.append(TreeNode(char)) 
            else: 
                node = TreeNode(char) 
                node.right = stack.pop() 
                node.left = stack.pop() 
                stack.append(node) 
        self.root = stack.pop() 
    def construct_from_prefix(self, prefix): 
        stack = [] 
        for char in reversed(prefix): 
            if char.isalnum(): 
                stack.append(TreeNode(char)) 
            else: 
                node = TreeNode(char) 
                node.left = stack.pop() 
                node.right = stack.pop() 
                stack.append(node) 
        self.root = stack.pop() 
 
    # Recursive Traversals 
    def recursive_in_order(self, node): 
        if node: 
            self.recursive_in_order(node.left) 
            print(node.value, end=" ") 
            self.recursive_in_order(node.right) 
 
    def recursive_pre_order(self, node): 
        if node: 
            print(node.value, end=" ") 
            self.recursive_pre_order(node.left) 
            self.recursive_pre_order(node.right) 
 
    def recursive_post_order(self, node): 
        if node: 
            self.recursive_post_order(node.left) 
            self.recursive_post_order(node.right) 
            print(node.value, end=" ") 
 
    # Non-Recursive Traversals 
    def non_recursive_in_order(self): 
        stack, node = [], self.root 
        while stack or node: 
            if node: 
                stack.append(node) 
                node = node.left 
            else: 
                node = stack.pop() 
                print(node.value, end=" ") 
                node = node.right 
 
    def non_recursive_pre_order(self): 
        if not self.root: 
            return 
        stack = [self.root] 
        while stack: 
            node = stack.pop() 
            print(node.value, end=" ") 
            if node.right: 
                stack.append(node.right) 
            if node.left: 
                stack.append(node.left) 
 
    def non_recursive_post_order(self): 
        if not self.root: 
            return 
        stack1, stack2 = [self.root], [] 
        while stack1: 
            node = stack1.pop() 
            stack2.append(node) 
            if node.left: 
                stack1.append(node.left) 
            if node.right: 
                stack1.append(node.right) 
        while stack2: 
            print(stack2.pop().value, end=" ") 
 
# Example Usage 
if __name__ == "__main__": 
    expr_tree = ExpressionTree() 
    postfix_expr = "AB+CDE+**"  # Example postfix expression 
    print("\nConstructing Expression Tree from Postfix Expression:", 
          postfix_expr) 
    prefix_expr = "*+AB*+CDE"  # Example prefix expression 
    print("\nConstructing Expression Tree from Prefix Expression:", 
          prefix_expr) 
    expr_tree.construct_from_postfix(postfix_expr) 
    print("\nRecursive In-order Traversal: ", end="") 
    expr_tree.recursive_in_order(expr_tree.root) 
    print("\nRecursive Pre-order Traversal: ", end="") 
    expr_tree.recursive_pre_order(expr_tree.root) 
    print("\nRecursive Post-order Traversal: ", end="") 
    expr_tree.recursive_post_order(expr_tree.root) 
    print() 
    print("\nNon-Recursive In-order Traversal: ", end="") 
    expr_tree.non_recursive_in_order() 
    print("\nNon-Recursive Pre-order Traversal: ", end="") 
    expr_tree.non_recursive_pre_order() 
    print("\nNon-Recursive Post-order Traversal: ", end="") 
    expr_tree.non_recursive_post_order()