class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True 
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True 
                temp = temp.left
            else: 
                if temp.right is None: 
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def min_value(self, current_node):
        if current_node == None:
            return None
        while current_node.left is not None:
            print(f"current Node = {current_node.value}")
            current_node = current_node.left
        return current_node.value

    def __delete_node(self,current_node, value):
        if current_node == None:
            return None
        if current_node.value > value:
            current_node.right = self.__delete_node(current_node.left,value)
        if current_node.value < value:
            current_node.left = self.__delete_node(current_node.right,value)
        if current_node.value == value:
            #if left_child
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.right == None:
                current_node.value = self.min_value(current_node.left)
            elif current_node.left == None:
                current_node.value = self.min_value(current_node.right)
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self,value):
        self.root = self.__delete_node(self.root , value)

    

