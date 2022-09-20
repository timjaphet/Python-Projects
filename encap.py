class Protected: # created class 
    def __init__(self): 
        self._protectedVar = 0 #set a protected variable with a value of 0
        self.__privateVar = 23 

    def getPrivate(self): 
        print(self.__privateVar) 

    
        
obj = Protected()
obj._protectedVar = 22 
print(obj._protectedVar) # used print method to display new value of protected variable
obj.getPrivate()
