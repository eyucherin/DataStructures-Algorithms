#Elizabeth (Che Rin) Yu
#Assignment 2
#CD.py: Class for CD.

#imports Resource from Resource file
from Resource import Resource
#CD class
#CD will be the child class for resource
class CD(Resource):
    #5 vairiables are passed when new CD class is created (title,publisher,artist,year,and length)
    #There are 3 additional instance variables excluding those that already exist in parent class
        #artist,year,length
    def __init__(self,title,publisher,artist,year,length):
        #When inhereting constructor variables, isElectronic is always set to False becuase DVDs are not electronic.
        super().__init__(title,publisher,type,isElectronic=False)
        #The type will always be set to DVD
        self.type = "CD"
        self.artist = artist
        self.year = year
        self.length = length
    #Method that returns the information of the resource in an easy to read way.
    def __str__(self):
        #The inherited information will be set to a variable called resourceString
        resourceString=super().__str__()
        #Return resourceString in addtion to the 3 new independent variables for CD
        #Required information will have a new line after every information
        return f"{resourceString}Artist:{self.artist}\nYear Published: {self.year}\nLength(min): {self.length}\n"
