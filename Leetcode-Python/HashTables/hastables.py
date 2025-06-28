class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
        
    def __hash(self, key):
        my_hash = 0
        for char in key:
            my_hash = (my_hash + ord(char) * 23) % len(self.data_map) # 7
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])): # inner list
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)): # outer list
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])): # inner list
                    all_keys.append(self.data_map[i][j][0])
        return all_keys         
        
        
    def print_table(self):
        for key,val in enumerate(self.data_map):
            print(str(key) + ": ", val)
        
my_has_table = HashTable()

my_has_table.set_item('John',200)   
my_has_table.set_item('Martha',1600)
my_has_table.set_item('Luke',1130)
my_has_table.set_item('Jonathan',6781)
my_has_table.set_item('Mark',782)

print(my_has_table.get_item('Mark'))

# print(my_has_table.keys())
my_has_table.print_table()


        
        