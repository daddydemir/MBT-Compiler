import Reader,Scanner,Parser
class Main:
    
    reader = Reader.Reader("myCode.mbt")

    fileLines = reader.getAllLines()

    scanner = Scanner.Scanner(fileLines)
    
    terms = scanner.getTerm()
    print(terms)

    parser = Parser.Parser(terms)

    parser.check()

    print("is run")

Main()