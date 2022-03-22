#Elizabeth (Che Rin) Yu
#Assignment 2
#Book.py:Class for Books

#imports Resource from Resource file
from Resource import Resource
#Book Class
#Book will be the child class for Resource
class Book(Resource):
    #7variables are passed when new Book class is created(title,author,publisher,pageNum,publicationYear,genre,isElectronic)
    #There are 4additional instance variables excluding those that already exist in parent class.
        #author, page number, publication Year, Genre.
    def __init__(self,title,author,publisher,pageNum,publicationYear,genre,isElectronic):
        super().__init__(title,publisher,type,isElectronic)
        #The type will always be set to Book
        self.type = "Book"
        self.author = author
        self.pageNum = pageNum
        self.publicationYear=publicationYear
        self.genre = genre
    #Method that returns the information of the resource in an easy to read way.
    def __str__(self):
        #The inherited information will be set to a variable called resourceString
        resourceString=super().__str__()
        #Return resourceString in addtion to the 4 new independent variables for Book
        #Required information will have a new line after every information
        return f"{resourceString}Author:{self.author}\nPage Count:{self.pageNum}\nYear Published:{self.publicationYear}\nGenre:{self.genre}\n"
