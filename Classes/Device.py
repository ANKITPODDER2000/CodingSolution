class Device(object):
    def __init__(self , name):
        self.name = name
        self.edge = set()
        
    # This will add the edge
    def addEdge(self , node):
        self.edge.add(node)
        
    # this method will help to debug
    def getDetails(self):
        print("Name : ", self.name)
        print("Connected with : ", end="")
        for i in self.edge:
            print(i.name , end = " ")
        print()
        