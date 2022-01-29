from Classes.Repeater import *
from Classes.Computer import *
from Classes.Read import *
from Classes.Write import *
import os

def clearConsole(): # This function will clear the console
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def showError(error_msg):
    Write.writeOutput(error_msg)

# ------------------------ 1
# This function will check whether device is present in the system or not
def isNameExist(arr , nm): 
    for i in arr:
        if i.name == nm:
            return True
    return False

# This function will return the device index if device present in system,
# else return -1
def getDevice(arr , nm):
    n = len(arr)
    for i in range(n):
        if arr[i].name == nm:
            return i
    return -1

# This function will create an instance of computer class and append that
# it into device array 
def addComputer(devices):
    computer_name = Read.readInput("Enter computer name : ")
    # This condition check whether any defice is already exist in the 
    # system with the name which will be provide by user by creating a
    # new computer
    if isNameExist(devices , computer_name):
        Write.writeOutput("That name already exists.")
        return
    comp = Computer(computer_name)
    Write.writeOutput("Computer name : "+comp.name)
    devices.append(comp)

# This function will create an instance of Repeater class and append that
# it into device array 
def addRepeater(devices):
    router_name = Read.readInput("Enter router name : ")
    # This condition check whether any defice is already exist in the 
    # system with the name which will be provide by user by creating a
    # new Repeater
    if isNameExist(devices , router_name):
        Write.writeOutput("That name already exists.")
        return
    rou = Repeater(router_name)
    Write.writeOutput("Router name : "+rou.name)
    devices.append(rou)

# Ask user input, if user gives 1 it will add a computer in system
# if user give 2 it will add a Repeater in system
def addDevice(devices):
    Write.writeOutput("Enter 1 : Add Computer\nEnter 2 : Add Repeater")
    # Ask user for the choice
    op = Read.readInput("Enter your option : " , inputType=int)
    if op == 1:
        addComputer(devices)
    elif op == 2:
        addRepeater(devices)
    else:
        showError("Wrong Read.readInput")
        
# ----------------------  2
# This function will take the device name and updates its strength
# with the value which will be give by user
def setStrength(devices):
    deviceName = Read.readInput("Please enter device name : " , str)
    deviceIndex = getDevice(devices , deviceName)
    if deviceIndex == -1:
        showError("Device doesn't exist in the system.")
        return
    device = devices[deviceIndex]
    # This condition will confirm that given name is belong to a computer
    if isinstance(device , Computer):
        strength = Read.readInput("Enter device strength : " , int)
        if strength <= 0:
            showError("Error : Strength can't be negetive")
        device.setStrength(strength)
        
        
# -------------------------- 3
# This function is used to check whether devices are pre present in the system
def checkExistence(devices , dev1 , dev2):
    getDev1 = getDevice(devices , dev1)
    getDev2 = getDevice(devices , dev2)
    if getDev2 == -1 or getDev1 == -1 or getDev1 == getDev2:
        showError("Error : Node not found.")
        return None , None
    return getDev1 , getDev2
    
# This function will take device name from user
def getDeviceName():
    dev1 = Read.readInput("Enter device 1 name : ")
    dev2 = Read.readInput("Enter device 2 name : ")
    return dev1 , dev2

# This function will connect devices or nodes
def connectDevices(devices):
    dev1 , dev2 = getDeviceName()
    getDev1 , getDev2 = checkExistence(devices , dev1 , dev2)
    
    if getDev1 == None:
        return
    
    devices[getDev1].addEdge(devices[getDev2])
    devices[getDev2].addEdge(devices[getDev1])
    
    
# ---------------- 4

# Depth first search to find out the path
def dfs(sourceNode , targetNodeName , strength , isvisted , ans):
    if sourceNode.name == targetNodeName:
        ans.append(sourceNode.name)
        return True
    elif strength == 0 or sourceNode.name in isvisted:
        return False
    isvisted[sourceNode.name] = True
    
    if isinstance(sourceNode , Repeater):
        strength = strength * 2
    strength -= 1
    
    for neighbour in sourceNode.edge:
        if dfs(neighbour , targetNodeName , strength , isvisted , ans):
            ans.append(sourceNode.name)
            return True
    isvisted.pop(sourceNode.name)
    return False

# Utility function to write down path in console
def showPath(path):
    Write.writeOutput("Path is : " , endChar=" ")
    for node in reversed(path):
        Write.writeOutput(node , endChar=" ")
    Write.writeOutput(" ")

# To check path between two nodes
def infoRoute(devices):
    dev1 , dev2 = getDeviceName()
    getDev1 , getDev2 = checkExistence(devices , dev1 , dev2)
    if getDev1 == None:
        return
    device1 , device2 = devices[getDev1] , devices[getDev2]
    if isinstance(device1 , Repeater) or isinstance(device2 , Repeater):
        showError("Error: Route cannot be calculated with a repeater.")
        return
    isVisited = {}
    ans = []
    if dfs(device1 , device2.name , device1.strength , isVisited , ans):
        showPath(ans)
    else:
        showError("Error: Route not found!")
    