
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
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value) 
        if value > current_node.value:
            return self.__r_contains(current_node.right , value)

    # This parts return , stack will be removed.
    def r_contains(self, value):
        return self.__r_contains(self.root , value)
        

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left , value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right , value)
        return current_node

    # return statement is not here , So stack will only removed.
    def r_inserts(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value) 
     

    def __delete_node(self,current_node,value):
        ###------  if left or right is None --------------###
        if current_node == None:
            return None
        ###----------------------------------------------###

        ###-----------Find value to delete -----------------------------###
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        ###-------------------------------------------------------------###

        ###----------- if you find value check children ----------------###
        else:
            ### ------------ 1. LEAF Status ------------------- ###
            if current_node.left == None and current_node.right == None:
                return None

            ### ------------ 2. ONLY RIGHT CHILD EXIST ---------###
            elif current_node.left == None:
                current_node = current_node.right

            ### ------------ 3. ONLY LEFT CHILD EXIST ----------###
            elif current_node.right == None:
                current_node = current_node.left

            ### ------------ 4. BOTH CHILD EXIST ------------------- ###
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    
    def delete_node(self,value):
        if self.root == None:
            return None
        self.root = self.__delete_node(self.root , value)
    
    def min_value(self,current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

my_tree = BinarySearchTree()
my_tree.r_inserts(47)
my_tree.r_inserts(21)
my_tree.r_inserts(76)
my_tree.r_inserts(18)
my_tree.r_inserts(27)
my_tree.r_inserts(52)
my_tree.r_inserts(82)
my_tree.r_inserts(25)
my_tree.r_inserts(29)

print(my_tree)
my_tree.delete_node(28)
# my_tree = BinarySearchTree()
# my_tree.r_inserts(47)
# my_tree.r_inserts(21)
# my_tree.r_inserts(18)
"""
     THE LINES ABOVE CREATE THIS TREE:
                42
                / \
              21   
             /
          18
"""
"""
✅ 스택 쌓이는 과정
__r_insert(47, 18) 호출 → current_node = 47
__r_insert(21, 18) 호출 → current_node = 21
__r_insert(None, 18) 호출 → current_node == None, Node(18) 생성
스택이 3개 쌓임 (__r_insert(47, 18), __r_insert(21, 18), __r_insert(None, 18))
✅ 스택 빠지는 과정
__r_insert(None, 18)이 Node(18)을 반환하면서 pop됨.
__r_insert(21, 18)이 실행되면서 current_node.left = Node(18) 적용 후 pop됨.
__r_insert(47, 18)이 실행되면서 current_node.left = Node(21) (변화 없음) 후 pop됨.
최종적으로 r_inserts(18) 실행이 끝나고, 트리 갱신이 완료됨.
print(f"Root : {my_tree.root.value}")
print(f"Root -> Left: {my_tree.root.left.value}")
print(f"Root -> Right: {my_tree.root.right.value}")
"""