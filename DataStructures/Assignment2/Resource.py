#Elizabeth (Che Rin) Yu
#Assignment 2
#Resource.py: Class for Resource (The parent class for the four kinds of materials).

#Resource Class
class Resource:
    # Constructor for Resource Class.
    # Four variables are passed when new Resource class is made (title, publisher, type, if it’s electronic or not)
    # There are instance variables for whether it is electronic or not, tile, publisher, type, whether it is checked out, and who checked it out to.
    def __init__(self,title,publisher,type,isElectronic):
        # If it is true that a  specific resource is electronic, indicate that it is Electronic.
        if isElectronic==True:
            self.isElectronic = "Electronic"
        # Otherwise, indicate that it is Physical.
        else:
            self.isElectronic = "Physical"
        self.title = title
        self.publisher = publisher
        self.type = type
        # Resource must always start out as not checked out
        self.isCheckedOut = False
        # Since nobody has checked the resource out, who it is checked out to is an empty string
        self.whoCheckedOut = " "

    #Getter for title
    def getTitle(self):
        #Returns the tile of the resource
        return self.title

    #Getter for type
    def getType(self):
        #Returns the type of the resource
        return self.type

    #Getter for whether it is checked out
    def getisCheckedOut(self):
        #Returns a boolean to indicate whether it is checked out of not
        return self.isCheckedOut

    #Getter for who it is checked out to
    def getwhoCheckedOut(self):
        #Returns the name of the person it is checked out to(whoCheckedOut)
        return self.whoCheckedOut

    #This method checks in a resource
    def checkIn(self):
        #If a resource is checked in, isCheckedOut vaiable is set to False .
        self.isCheckedOut = False
        #Since the resource is not checked out whoCheckedOut is set to an empty string.
        self.whoCheckedOut = " "

    #This method checks out a resource
    #The name of the borrower must be passed in order to check out a book
    def checkOut(self,borrower):
        #If a resource is checked out, isCheckedOut variable is set to True  .
        self.isCheckedOut = True
        #Since the resource is checked in, whoCheckedOut is set to the name of the borrower.
        self.whoCheckedOut = borrower

    #Method that returns the information of the resource in an easy to read way.
    #Indication of resource differs for whether the book is checked out or not.
    def __str__(self):
        #All the information will be written out in a form of a string.
        string= ""
        #If book is checked out, then we all include all the instance variables exept for isCheckedOut.
        #Instead, we indicate that it is checked out to whoCheckedOut
        if self.isCheckedOut:
            #The string will be a combination of all the required information with a new line after every information.
            string+=f"Title: {self.title}\nType: {self.type}\nPublisher: {self.publisher}\n{self.isElectronic}\nChecked out to {self.whoCheckedOut}\n"
        #Otherwise, we exclude both isCheckedOut and whoCheckedOut and indicate that it is available.
        else:
            #The string will be a combination of all the required information with a new line after every information.
            string+=f"Title: {self.title}\nType: {self.type}\nPublisher: {self.publisher}\n{self.isElectronic}\nAvailable\n"
        return string
