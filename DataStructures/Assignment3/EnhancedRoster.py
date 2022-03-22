#Elizabeth Yu
#Assignment 3
#EnhancedRoster.py: A more advanced program that handles the addition and removal of students to a Roster Class.

#Import OrderedLinkedList
from OrderedLinkedList import OrderedLinkedList
#Import UnorderedLinkedList
from UnorderedLinkedList import UnorderedLinkedList
#Create an instance of OrderedLinkedList called Roster.
#Make it universally available to all methods
roster=OrderedLinkedList()
#Create an instance of UnorderedLinkedList called waitlist
#Make it universally available to all methods
waitList=UnorderedLinkedList()

#Function that adds students to the Roster
#Does not return Anything
def add1():
    studentName=input("Enter student name in LastName, FirstName format: ")
    #If the name is already on Roster, do not add and notify the users.
    if roster.search(studentName):
        print("Student has already been added to the Roster")
    #Otherwise, add the name to Roster
    else:
        roster.add(studentName)

#Function that is called when the user tries to add students to the Roster when the Roster is full.
#Does not return Anything
def add2():
    studentName=input("Enter student name in LastName, FirstName format: ")
    waitlistedStudent=studentName
    #If the name of the student is already on the Roster, do not do anyting and nofify the users.
    if roster.search(studentName):
        print("\n"+"Student has already been added to the Roster")
    #If the student name is already on the waitlist, no not do anything and notify the users.
    elif waitList.search(waitlistedStudent):
        print("\n"+"Student has already been added to the Waitlist")
    #otherwise, add the student to the waitlist.
    else:
        waitList.append(waitlistedStudent)

#Function that removes student from list.
#Does not return anything
def remove():
    studentName=input("Enter student name in LastName, FirstName format: ")
    #If the student name exists in the roster:
    if roster.search(studentName):
        #remove the student from roster
        roster.remove(studentName)
        #If there are people on the waitlist
        if not waitList.isEmpty():
            #Take the first student from the waitlist and add the student to the Roster.
            enrollStudent = waitList.pop(0)
            roster.add(enrollStudent)
    #if the student is on the waitlist:
    elif waitList.search(studentName):
        #Remove the student off the waitlist.
        waitList.remove(studentName)
    #Otherwise:The student was not found on neither the waitlist nor the Roster so student cannot be removed.
    else:
        print("Student name was not found on neither the Roster or Waitlist, please try adding the student")

#Function that displays the class Roster based on Alphabetical Order.
#Does not return anything
def display():
    #print the Roster
    print("\n"+"Current Class Roster:")
    print(roster)
    #If there are people on the waitlist:
    #Print the waitlist
    if not waitList.isEmpty():
        print("\n"+"Current Class Waitlist:")
        print(waitList)

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
        elif command =="a" and roster.size()>=classSize:
            #call add2() to add student on the waitlist or to notify them that the student has already been added to either the waitlist or Roster.
            add2()
        #When "r" is executed
        elif command =="r":
            #If roster is empty, dont do anything
            if roster.isEmpty():
                pass
            #Otherwise,
            else:
                #Call remove() to remove the name from roster
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
            #Tell users that command is illegal\
            print("\n"+"The command is illegal, Try again:")
        #while the while loop is running, continously ask users execute program after desired execution has been accomplished.
        command=input("\n"+"Enter [a/r/d/q]: ")


if __name__=="__main__":
    main()
