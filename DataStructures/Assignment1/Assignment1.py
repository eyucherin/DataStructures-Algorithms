#Elizabeth(Che Rin) Yu
#Assignment 1
#Game of Life: This file is a one dimensional simulation of biological cells

from copy import copy
import random

#This function is called shouldDie and takes list and index as its parameters.
#It will return True if the cell in list of the indicated index is Alive(1) and has live neighbors.
#It will return True if the cell in the list of the indicated index is Dead(0) and has dead neighbors(0).
#Otherwise, it will return False, indicating that the cell should live.
#This function will determine whether the cell should die or live.
def shouldDie(list,index):
    #The first cell has only one neighboring cell.
    #Edge Cells can never die once they are alive.
    if index == 0:
        #If the cell is dead and the neighboring cell is dead, the cell should remain dead on the next round.
        if list[index] == 0 and list[index+1] == 0:
            #Return True to indicate that the cell should reamain dead.
            return True
        #However,if the neighboring cell is alive, the cell should live on the next round regardless of wheter the cell itself is dead or alive.
        else:
            #Return False to indicate that the cell should live on the next round.
            return False
    #Similarly, the last cell only has one neighboring cell.
    #Edge Cells can never die once they are alive.
    elif index == len(list)-1:
        #If the cell is dead and the neighboring cell is dead, the cell should remain dead on the next round.
        if list[index] == 0 and list[index-1] == 0:
            #Return True to indicate that the cell should reamain dead.
            return True
        #However,if the neighboring cell is alive, the cell should live on the next round regardless of wheter the cell itself is dead or alive.
        else:
            #Return False to indicate that the cell should live on the next round.
            return False
    #The cells excluding the edge cells have a neighbor to the right and to the left.
    #conditions differ from edge cells.
    else:
        #If the cell is alive and the two neighboring cells are alive, then the cell should die on the next round.
        if list[index] == 1 and list[index+1] == 1 and list[index-1] == 1:
            #Return True to indicate that the cell should die
            return True
        #However, if the cell is dead and the two neighboring cells are dead, then the cell should reamin dead.
        elif list[index] == 0 and list[index+1] == 0 and list[index-1] == 0:
            #Return True to indicate that the cell should remain dead.
            return True
        #Otherwise, the cell stays or becomes alive on the next round
        else:
            #Return False to indicate that the cell should Live on the next round.
            return False


#This function is called isZero and takes list and index as its parameters.
#It will return True if the element in the list at the given index is 0(Dead).
#It will return False if the element in the list at the given index is 1(Alive).
#This function determines whether the element is currently Dead(0) or Alive(1).
def isZero(list,index):
    #If the element on the list at the given index is 0 then the cell is Dead.
    if list[index] == 0:
        #We should therefore return True
        return True
    #Otherwise, if the element on the list at the given index is 1, then the cell is Alive
    else:
        #Therefore, we should return False
        return False

#This function is called advanceTime and takes list as its parameters.
#It will return a new list of cells who have died or survived after the occuring generation.
#This function takes a list of cells and returns a new list that determines whether the cells have lived or died.
def advanceTime(list):
    #Create a variable called newList and set it equal to a copied version of list given in the parameter.
    newList = copy(list)
    #Loop through every index value of the list.
    for i in range(len(list)):
        #If the cell should die in the upcomming round but it is currently alive.
        if shouldDie(list,i)==True and isZero(list,i)==False:
            #Indicate that the cell has died(0) on the given index on the new list.
            newList[i]=0
        #Conversely, if the cell should live in the upcomming round but it is currently dead.
        elif shouldDie(list,i)==False and isZero(list,i)==True:
            #Indicate that the cell has lived(0) on the given index on the new list.
            newList[i]=1
        #If the cell should die in the upcomming round and it is currently dead.
        #If the cell should live in the upcomming round and it is currently alive.
        else:
            #Do not do anything.
            pass
    #Return the new list.
    return newList

#This is the main function, takes no parameters.
#Does not return anything.
#Our desired programs will be executed here.
def main():
    #Set a variable called NUM_TIME_STEPS equal to 10.
    #This is the number of generations the simulation will execute
    #The simulation will generate 10 executions.
    NUM_TIME_STEPS=10
    #Set a variable called NUM_ELEMENTS equal to 10.
    #This is the number of cells the list will contain
    #The list will contain 10 cells
    NUM_ELEMENTS=10
    #Create an empty list called myList
    myList=[]
    #Create a For loop to add random cells to myList
    #Since the length my mylist should be equal to NUM_ELEMENTS.
    #Create a For Loop that is being looped by the range of NUM_ELEMENTS
    for i in range(NUM_ELEMENTS):
        #Add random cells that are either dead or alive
        myList.append(random.randint(0,1))
    #Print myList
    print(myList)
    #Create a variable called loopNum and set it equal to 0.
    #This will keep track of when to end the While Loop below.
    loopNum=0
    #Create a While Loop
    #as long as loopNum is less than the desired number of generations (NUM_TIME_STEPS),loop will execute.
    while loopNum<NUM_TIME_STEPS:
        #Start of with the random list that was made.
        #Execute the function advanceTime on this list
        #Create a variable for this function
        newList=advanceTime(myList)
        #Print the executed list
        print(newList)
        #The executed list now becomes the list that should be executed next
        myList=newList
        #Add 1 to loopNum
        loopNum+=1

if __name__=="__main__":
    main()
