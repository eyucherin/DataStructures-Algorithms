#Elizabeth Yu
#Assignment 3
#Roster.py: Basic program that handles the addition and removal of students to a Roster Class.

#Import OrderedLinkedList
from OrderedLinkedList import OrderedLinkedList
#Create an instance of OrderedLinkedList called Roster.
#Make it universally available to all methods
roster=OrderedLinkedList()

#Function that adds students to the Roster
#Does not return Anything
def add1():
    studentName=input("Enter student name in LastName, FirstName format: ")
    roster.add(studentName)

#Function that is called when the user tries to add students to the Roster when the Roster is full.
#Does not return anything
def add2():
    print("\n"+"Class capacity has been reached, Program will end.")
    print("Current Class Roster:")
    print(roster)

#Function that removes student from list.
#Does not return anything
def remove():
    studentName=input("Enter student name in LastName, FirstName format: ")
    roster.remove(studentName)

#Function that displays the class Roster based on Alphabetical Order.
#Does not return anything
def display():
    print("\n"+"Current class roster:")
    print(roster)

#Function that quits the program once it is called.
#Does not return anything
def quit():
    print("\n"+"Thank you for using this program to manage class roster")

#main function is called when the prgram is being executed.
def main():
    print("""
Allowed Commands are
a: to add a student to the class
r: to remove a student to the class
d: to display the roster
q: to quit the progam
    """)
    #Asks users for an integer value of the maximum size of the class.
    classSize=int(input("Please specify the maximum size for the class roster: "))
    #Asks users to execute a command
    command=input("\n"+"Enter [a/r/d/q]: ")
    #Implement a while loop for the program to keep running until conditions fail, or until users tell the prgram to stop.
    #While program is running..
    while roster:
        #When "a" is executed and when the roster is less than the indicated maximum class size.
        if command =="a" and roster.size()<classSize:
            #call add1() to add student on roster
            add1()
            #If after the student is added, and the roster is the as long as the indicated maximum class size.
            if roster.size()==classSize:
                #Print the roster
                add2()
                #End program
                break
        #When "r" is executed
        elif command =="r":
            #call remove() to remove a student
            remove()
        #When "d" is executed
        elif command =="d":
            #call display() to display class roster.
            display()
        #When "q" is executed
        elif command =="q":
            #call quit()
            quit()
            #end program
            break
        #Otherwise if executed command is neither "a","r","d","q":
        else:
            #Tell users that command is illegal
            print("\n"+"The command is illegal, Try again")
        #while the while loop is running, continously ask users execute program after desired execution has been accomplished.
        command=input("\n"+"Enter [a/r/d/q]: ")

if __name__ == "__main__":
    main()
