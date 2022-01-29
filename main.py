from Classes.Read import *
from Classes.Write import *
from Classes.Computer import *
from Classes.Repeater import *
from Function.Func import *

devices = []

while(True):
    Write.writeOutput("Enter 1 : Add\nEnter 2 : Set Strength\nEnter 3 : Connect\nEnter 4 : Info Route\nEnter 5 : Exit")
    # Option will store the user input,
    # on the basis of user input user will be able to perform opration
    op = Read.readInput("Enter your option : " , int)
    # If op is 1 then user can add device in the system
    if op == 1:
        addDevice(devices)
    # If op is 2 then user can update the strength
    elif op == 2:
        setStrength(devices)
    # If op is 3 then user will able to add an edge between two devices
    elif op == 3:
        connectDevices(devices)
    # If op is 4 then user can check path between two nodes
    elif op == 4:
        infoRoute(devices)
    # Handle wrong input
    elif op == 5:
        break
    else:
        showError("Error : Wrong operation ...")
    
    Read.readInput("Press enter to clear console : ")
    clearConsole()