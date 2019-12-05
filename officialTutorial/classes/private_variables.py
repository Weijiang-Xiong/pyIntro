class Mapping:
    def __init__(self,iterable):
        self.items_list=[]
        self.__update(iterable)
    
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    
    __update = update

class MappingSubclass(Mapping):

    def update(self, keys,values):
        for item in zip(keys, values):
            self.items_list.append(item)

iteration=[1 , 2 , 3 , 4 , 5]
x = MappingSubclass(iteration)
keys = [123 , 456 , 789]
values = [10 , 11 , 12]
x.update(values,keys)
print(f'the items list in variable x is {x.items_list}')