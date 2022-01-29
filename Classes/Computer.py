from soupsieve import select
from Classes.Device import *
class Computer(Device):
    def __init__(self , name):
        Device.__init__(self , name)
        self.strength = 5
        
    # this method update the strength
    def setStrength(self , strength):
        self.strength = strength
    
    # this method will help to debug
    def getDetails(self):
        Device.getDetails(self)
        print("Strength : ",self.strength)