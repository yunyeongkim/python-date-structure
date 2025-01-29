class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value , end="")
            temp = temp.next
        print('\n')
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail # Origin tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            # self.tail is now self.tail.prev
            # disconnect next for prev since it is last node.
            self.tail.next = None
            # disconnect prev for origin. 
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # Move head to next.
            self.head = self.head.next
            # next node' prev should be None
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self,index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index): # if 3 , 4 have to be shown
                temp = temp.next # like plus  + 1
        else:
            temp = self.tail
            for _ in range(self.length -1 , index , -1): # if 3 , 4 have to be shown
                #  start value , index , how to plus or decrease
                temp = temp.prev # like plus  + 1
        return temp
    
    def set_value(self , index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    


    def insert(self,index,value):
        if index == 0:
            return self.prepend(value)
        if index == self.length-1:
            return self.append
        
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        # remind to change 4 of arrow.
        # before's next -> new_node
        before.next = new_node
        # new_node's prev -> before
        new_node.prev = before
        # new node's next -> after
        new_node.next = after
        # after's prev -> new node
        after.prev = new_node
        # in this monent, what after have? 
        return True
            
            




    



my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(9)
my_doubly_linked_list.append(10)


print(my_doubly_linked_list.insert(4,3))
print(my_doubly_linked_list.get(3).value)

my_doubly_linked_list.print_list()
