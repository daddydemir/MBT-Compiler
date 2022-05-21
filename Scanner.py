
class Scanner:
    def __init__(self, allLines):
        self.allLines = allLines
        pass
    
    allLines = []
    listOfterm = []

    def getTerm(self):
        for i in self.allLines:
            self.listOfterm.append(i.split(' '))
        return self.listOfterm