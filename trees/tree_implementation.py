class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self.insert_util(self.root, key)

    def delete(self, value):
        self.root = self.delete_util(self.root, value)

    def search(self, key):
        return self.search_util(self.root, key)

    def inorder_traversal(self):
        self.inorder_traversal_util(self.root)
        print()
    
    def preorder_traversal(self):
        self.preorder_traversal_util(self.root)
        print()
    
    def postorder_traversal(self):
        self.postorder_traversal_util(self.root)
        print()

    def insert_util(self, current_node, key):
        if not current_node:
            return Node(key)
        elif key < current_node.value:
            current_node.left = self.insert_util(current_node.left, key)
        else:
            current_node.right = self.insert_util(current_node.right, key)
        
        return current_node

    def delete_util(self, current, key):
        if not current:
            return current
        elif key < current.value:
            current.left = self.delete_util(current.left, key)
        elif key > current.value:
            current.right = self.delete_util(current.right, key)
        else:
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp
 
            temp = self.get_min_node(current.right)
            current.value = temp.value
            current.right = self.delete_util(current.right, temp.value)
        return current

    def search_util(self, current_node, value):
        if current_node == None or current_node.value == value:
            return current_node
        elif value < current_node.value:
            return self.search_util(current_node.left, value)
        elif value > current_node.value:
            return self.search_util(current_node.right, value)

    def preorder_traversal_util(self, current_node):
        if current_node:
            print(current_node.value, end=" ")
            self.preorder_traversal_util(current_node.left)
            self.preorder_traversal_util(current_node.right)

    def inorder_traversal_util(self, current_node):
        if current_node:
            self.inorder_traversal_util(current_node.left)
            print(current_node.value, end=" ")
            self.inorder_traversal_util(current_node.right)

    def postorder_traversal_util(self, current_node):
        if current_node:
            self.postorder_traversal_util(current_node.left)
            self.postorder_traversal_util(current_node.right)
            print(current_node.value, end=" ")
    
    def get_min_node(self, current):
        if current is None or current.left is None:
            return current
 
        return self.get_min_node(current.left)

# Driver program to test above function
tree = BinaryTree()
 
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)
tree.inorder_traversal()
tree.preorder_traversal()
tree.postorder_traversal()
tree.delete(30)