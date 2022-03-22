# Elizabeth (Che Rin) Yu
# Assignment5: DataSearch.py
# This file takes values that must be searched for from a file and uses binary search to search those values at a different file. It then states whether those values were found at an empty file.
# Used the Runerstone online chapter 6.7(Bubble Sort),6.4(Binary Search), and code from lab5 for reference.

import sys
from copy import copy
"""
DOCSTRINGS
 This function takes a sorted list and searches for a value using the binary search algorithm.
 Paramenters: list and val
 list(argument1): a list of values
 val(argument2): the value that must be search for in that list
 Returns True if val was found in list, otherwise, returns False
"""
def binarySearch(list,val):
    copyList=copy(list)
    midIndex=(len(list)//2)
    #If value is the middle value of list return True
    if copyList[midIndex] == val:
        return True
    #If the length of the list is 1 and the one value is not the value we are looking for, return False
    elif len(copyList)==1 and copyList[0]!=val:
        return False
    #If the value we are looking for is greater than the middle value, search the right side of list
    elif val>list[midIndex]:
        rightList = copyList[midIndex:len(list)]
        copyList = rightList
        return binarySearch(copyList,val)
    #If the value we are looking for is less than the middle value, search the left side of list
    elif val<list[midIndex]:
        leftList=copyList[0:midIndex]
        copyList = leftList
        return binarySearch(copyList,val)
    #if val not in list, return False
    else:
        return False


"""
DOCSTRINGS
 This function takes a list and sorts the list using Bubble Sort algorithm.
 Paramenters: list
 list(argument1): a list of values
 Returns sorted list
"""
# Used code from lab5 and runerstone textbook.
def BubbleSort(list):
    for i in range(len(list) - 1, 0, -1):
          for j in range(i):
              if list[j] > list[j + 1]:
                  temp = list[j]
                  list[j] = list[j + 1]
                  list[j + 1] = temp
    return list


def main():
    seekList = []
    dataList = []
    foundList =[]

    # Read 2nd file from command line and append to seekList
    file1 = open(sys.argv[1],"r")
    line = file1.readline()
    line = line.split()
    for i in line:
        seekList.append(int(i))
    file1.close()

    # Read 3rd file from command line and append to dataList
    file2 = open(sys.argv[2],"r")
    line = file2.readline()
    line = line.split()
    for i in line:
        dataList.append(int(i))
    file2.close()

    # Sort the dataList using bubble Sort
    BubbleSort(dataList)

    # Search for every value in seekList and check if those values exist in dataList
    # If value exist, append 1, if not append 0 to foundList
    for i in seekList:
        result = binarySearch(dataList,i)
        if result == False:
            foundList.append(0)
        else:
            foundList.append(1)

    # In human readable form, open and write from 4rdfile in command line if a value in seekList exists in dataList in a file
    file3 = open(sys.argv[3],"w")
    for i in range(len(foundList)):
        if foundList[i]==1:
            file3.write(f"{seekList[i]}: Yes\n")
        elif foundList[i]==0:
            file3.write(f"{seekList[i]}: No\n")
    file3.close()


if __name__=="__main__":
    main()
