
class Reader:

    def __init__(self,filepath):
        self.file = open(filepath , 'r')
        
    def getAllLines(self):
        return self.file.readlines()