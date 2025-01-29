class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
# Last In last Out
class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        # self.bottom = new_node

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self,value):
        new_node = Node(value)
        if self.height == 0 :
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    # Last in Last out
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    

my_stack_list = Stack(3)
my_stack_list.push(2)
my_stack_list.push(1)
my_stack_list.push(0)
my_stack_list.pop()

my_stack_list.print_stack()