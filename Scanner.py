
class Scanner:
    def __init__(self, allLines):
        self.allLines = allLines
        pass
    
    allLines = []
    listOfterm = []

    def analysis(self):
        lastindex = 0
        liste = []        
        for line in self.allLines:
            for i in range(len(line)):
                if(line[i] == " " or line[i] == "\n"):
                    liste.append(line[lastindex:i])
                    lastindex = i+1
            self.listOfterm.append(liste)
            lastindex = 0
            liste = []
        return self.detailedAnalysis()

    def detailedAnalysis(self):
        liste = []
        lastindex = 0
        for index in range(len(self.listOfterm)):
            if(len(self.listOfterm[index]) == 1):            
                for i in range(len(self.listOfterm[index][0])):            
                    if(self.listOfterm[index][0][i] == "("):
                        temp = self.listOfterm[index][0][lastindex:i]                        
                        lastindex = i
                        liste.append(temp)
                    elif(self.listOfterm[index][0][i] == ")"):
                        temp = self.listOfterm[index][0][lastindex:i+1]
                        lastindex = i
                        liste.append(temp)                
                self.listOfterm[index] = liste
                lastindex = 0                 
                liste = []  
        return self.listOfterm
    
    def printList(self):
        for line in self.listOfterm:
            print(line)
