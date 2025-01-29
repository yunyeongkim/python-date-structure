# Key: value 
# With hash function , hash(key) -> get key,value fair and Address
"""
Hash 
1. One Way  : key - hash - pair & address
2. Demerministic : everytime we put key to hash , same value come
"""

#Seperate Chaining
"""
  ## Set as List.
index 1: ['one': 1] 
index 2: ['two': 1] , ['four': 1] 
index 3: ['three': 1] 

  ## Linked List 
index 1: ['one': 1] 
index 2: ['two': 1] -> next -> ['four': 1] 
index 3: ['three': 1] 
"""

# Linear Probing / Open Probing
"""
  ## Literate and find empty address
index 1: ['one': 1] 
index 2: ['two': 1]
index 4: ['three': 1] 
index 3: ['four': 1] 
"""

# Big O
"""
Hash method is O(1)
But if there is lots of in one hash index:
and Memory is really small ? O(n)
"""
class HashTable:
    def __init__(self , size =7):
        self.data_map = [None] * size
    
    def __hash(self , key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) *23 ) % len (self.data_map)
        return my_hash
    
    def print_table(self):
        for i , val in enumerate(self.data_map):
            print(i , " : ", val)
    
    def set_item(self, key , value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            # initializing
            self.data_map[index] = []
        self.data_map[index].append([key,value])
    
    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def get_keys(self):
        key_list = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    key_list.append(self.data_map[i][j][0])
        return key_list
    
    def item_in_common(self, list1,list2):
        my_dict ={}
        for i in list1:
            my_dict[i] = True
        for j in list2:
            if j in my_dict:
                return True
        return False


my_table = HashTable()
my_table.set_item('bolts',1400)
my_table.set_item('washers',2400)
my_table.set_item('lumber',400)
print(my_table.get_item('washers'))
print(my_table.get_keys())


list1 = [1,2,3]
list2 = [1,3,4]
print(my_table.item_in_common(list1, list2))
# my_table.print_table()

