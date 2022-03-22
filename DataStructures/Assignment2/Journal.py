#Elizabeth (Che Rin) Yu
#Assignment 2
#Journal.py:Class for Journals

#imports Resource from Resource file
from Resource import Resource
#Journal Class
#Journall will be the child class for Resource
class Journal(Resource):
    #4 variables are passed when new Journal class is created (title,publisher,yearRange,publishingFreq)
    #There are 2 additional instance variables excluding those that already exist in the parent class
        #The range of Years and publishing frequency
    def __init__(self,title,publisher,yearRange,publishingFreq):
        #When inhereting constructor variables, isElectronic is always set to True becuase Journals are electronic.
        super().__init__(title,publisher,type,isElectronic=True)
        #The type will always be set to Journal
        self.type = "Journal"
        self.yearRange = yearRange
        self.publishingFreq = publishingFreq
    #Method that returns the information of the resource in an easy to read way.
    def __str__(self):
        #The inherited information will be set to a variable called resourceString
        resourceString=super().__str__()
        #Return resourceString in addtion to the 2 new independent variables for Journal
        #Required information will have a new line after every information
        return f"{resourceString}Year Range:{self.yearRange}\nFrequency: {self.publishingFreq}\n"
