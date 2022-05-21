# stack : type > variable > assign > value
# a = 10 + 20
class Parser:
    def __init__(self, all):
        self.all = all
    
    reserved = ["ts","os","dy","ise","kd","bas"]
    
    tsl = "0123456789"
    detectedVarialbes = []

    def check(self):
        for i in range(len(self.all)):
            # line based check : i = line number
            for k in self.reserved:
                for m in range(len(self.all[i])):
                    if(k == self.all[i][m]):
                        self.assignCheck(self.all[i])
    
    def assignCheck(self,line):
        # satirin syntaxini kontrol ediyor
        isLineTrue = False
        isTs = False
        isOs = False
        isDy = False
        variable = {}
        for i in range(len(line)):
            match line[i]:
                case "ts":
                    if(i == 0):
                        isLineTrue = True
                        isTs = True
                    else:
                        isLineTrue = False
                    
                case "os":
                    if(i == 0):
                        isLineTrue = True
                        isOs = True
                    else:
                        isLineTrue = False

                case "dy":
                    if(i == 0):
                        isLineTrue = True
                        isDy = True
                    else:
                        isLineTrue = False

                case "=":
                    if(i == 2):
                        isLineTrue = True
                    else:
                        isLineTrue = False

                case default:
                    if(i == 1):
                        variable[default] = ""
                    elif(i == 3):
                        if(isTs):
                            gelen = self.tsCheck(default[0:-1])
                            if(gelen):
                                variable[line[1]] = default[0:-1]
                            else:
                                error = ""
                                for x in line:
                                    error += x+" "
                                print("Syntax Error :" , error , "HANDLE [",default[0:-1],"]")
                        elif(isOs):
                            self.osCheck(default)
                        elif(isDy):
                            self.dyCheck(default)
                    elif(i >= 4):
                        print("Sytax Error :" )
                    
        
    def tsCheck(self,variable):
        isTrue = False
        for i in variable:
            if(-1 != self.tsl.find(i)):
                isTrue = True
            else:
                isTrue = False
                return isTrue
        return isTrue
                
    def osCheck(self,variable):
        pass

    def dyCheck(self,variable):
        pass