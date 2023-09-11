

class utils():
    def reversed(self,input):
        if (type(input) != int):
            return None # must be int
        else:
            reversedNumber = str(input)[::-1]
            return int(reversedNumber) 
        
    def formatter(self,input):
        if (type(input) != int):
            return None,None #must be int
        else:
            return bin(input),oct(input)
            