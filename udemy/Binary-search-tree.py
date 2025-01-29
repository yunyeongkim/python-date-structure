
# Binary Tree
"""
Full : Every node point to 0 or 2 nodes.
Perfect Tree: Any level on the tree that has any nodes is 
              completed filled all the way across 
Complete Tree: filling the tree from left to right with no gaps
                Left to right !!!

# Every children node can have one parent node.
"""

#Binary Search Tree Big(O)
"""
 2^n  = O(log(n)) ->  prefect Tree
 ** But if in linked list shape -> O(n)
 ##           LinkedList  BinaryTree
 ##  lookup()    O(n)     @ O(log n)
 ##  remove()    O(n)     @ O(log n)
 ##  insert()  @ O(1)       O(log n)
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
            
    
    def insert(self, value):
        new_node = Node(value)
        temp = self.root

        if temp is None:
            self.root = new_node
            return True
        
        while (True):
            if new_node.value == temp.value:
                return False
            
            # If value is less than root to left.
            if new_node.value < temp.value :
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            # if value is bigger than to right.
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self,value):
        if self.root == None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else :
                return True
        return False
        
    



my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.contains(52))
print(my_tree.root)