#Elizabeth (Che Rin) Yu
#Assignment 2
#additionalFunctions.py: This file includes several functions that performs tasks on a list of Resources

#imports Resource from Resource file
from Resource import Resource

#Function that takes a list of Resource objects and returns another list of resources that have been checked out.
def getAllCheckedOut(list):
    checkedOutList = []
    #Go through every resource in list and if it is checked out, it should add it to checkedOutList
    for i in list:
        if i.isCheckedOut==True:
            checkedOutList.append(i)
    #returns checkedOutList
    return checkedOutList

#Function that takes a person's name as the parameter and returns a list of resources that the person has checked out.
def getAllUserHasCheckedOut(list,name):
    checkedOutList = []
    #Go through every resource in list and if the name of the person exists in a Resource, then add that resource into checkedOutList
    for i in list:
        if i.whoCheckedOut==name:
            checkedOutList.append(i)
    #return checkedOutList
    return checkedOutList

#Function that takes a type as the parameter and returns a list of resources that the correspond to that type in another list of resources.
def getAllOfType(list,type):
    listofType=[]
    #Go through every resource in list and if the type exists in a Resource, then add that resource into listofType
    for i in list:
        if i.type == type:
            listofType.append(i)
    #Return listoftype
    return listofType
