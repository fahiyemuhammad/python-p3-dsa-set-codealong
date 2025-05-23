class MySet():

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self,value):
        return value in self.dictionary
    
    def add(self,value):
        self.dictionary[value] = True
        return self
    
    def delete(self,value):
        self.dictionary.pop(value,None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
        return self
    def __str__(self):
        keys = list(self.dictionary.keys())
        keys_str = ",".join(str(k) for k in keys)
        return f"MySet: {{{keys_str}}}"
    
set = MySet([1,2,3])
print(set)



    

                




    

    
