class checker:
    def __init__(self,list):
        self.list = list

    def check(self):        
        return (self.list[0] == self.list[1] == self.list[2] 
             or self.list[3] == self.list[4] == self.list[5] 
             or self.list[6] == self.list[7] == self.list[8] 
             or self.list[0] == self.list[3] == self.list[6]
             or self.list[1] == self.list[4] == self.list[7]
             or self.list[2] == self.list[5] == self.list[8]
             or self.list[0] == self.list[4] == self.list[8]
             or self.list[2] == self.list[4] == self.list[6])
    
    