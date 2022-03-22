#Elizabeth (Che Rin) Yu
#Assignment 2
#DVD.py:Class for DVD

#imports Resource from Resource file
from Resource import Resource
#DVD Class
#DVD will be the child class for Reousource.
class DVD(Resource):
    #6 variables are passed when new DVD class is created.(title,publisher,year,length,performers,genre)
    #There are 4 additional instance variables excluding those that already exist in the parent class.
        #Year, Length, Performers, and Genre.
    def __init__(self,title,publisher,year,length,performers,genre):
        #When inhereting constructor variables, isElectronic is always set to False becuase DVDs are not electronic.
        super().__init__(title,publisher,type,isElectronic=False)
        #The type will always be set to DVD
        self.type = "DVD"
        self.year = year
        self.length = length
        self.performers = performers
        self.genre = genre

    #Method that returns the information of the resource in an easy to read way.
    def __str__(self):
        #The inherited information will be set to a variable called resourceString
        resourceString=super().__str__()
        #Return resourceString in addtion to the 4 new independent variables for DVD
        #Required information will have a new line after every information
        return f"{resourceString}Performers: {self.performers}\nYear Published: {self.year}\nLength(min): {self.length}\nGenre: {self.genre}\n"
