# Elizabeth (Che Rin) Yu
# Assignment6: GuessingGame.py
# This file reads from tree.txt, creates a binary tree out of the data, and executes a restricted Guessing Game out of it (Users are not allowed to input data)
from BinaryTree import BinaryTree
from GameTreeReader import GameTreeReader

#Class GuessingGame, inherits from BinaryTree class
class GuessingGame(BinaryTree):
    #Takes parameter: tree
    #Tree: a txt file that is read in by the program and made into a tree.
    def __init__(self,tree):
        super().__init__()
        # Binary representation of Tree
        self.tree = tree
        # Where the current data is pointing at
        self.currentData = self.tree.getRoot()
    #getData get the current data that is being pointed at
    def getData(self):
        return self.currentData
    #Takes parameters yesOrNo
    #This function gets the next data to be self.currentData according to yesOrNo
    def setNextData(self,yesOrNo):
        #If yes, move to left Child
        if yesOrNo == "yes":
            self.currentData=self.currentData.getLeftChild()
        #If no, move to right Child
        elif yesOrNo =="no":
             self.currentData=self.currentData.getRightChild()
    #sets self.currentData to root of tree
    def setToRoot(self):
        self.currentData=self.tree.getRoot()
    #Determines if self.currentData is a leaf in the tree
    def isThisLeaf(self):
        return self.currentData.isLeaf()

"""
DOCSTRINGS
    This function executes the 20 question game
    Parameters: game,version
        game(object): specified object of desired game
        version(String): If it it Restricted or Unrestricted
    Returns Nothing
"""
def playGame(game,version):
    #List of leaves items inside of tree,--> items that can be guessed by computer.
    sportList=["Soccer","Tennis","Squah","Surfing","Snowboarding","Football","Basketball","Beach Volleyball","Volleyball","Ice hockey","Floor hockey","Boxing","Taekwondo","Swimming","Frisbee","Badminton","Speed Skating","Sprinting","Weightlifting"]
    #Start game by asking whether user wants to play game, keep asking until the answer is either yes or no
    startQuestion=input("Do you want to play a Guessing Game?[yes/no] ")
    while startQuestion!="yes" and startQuestion!="no":
        startQuestion=input("Do you want to play a Guessing Game?[yes/no] ")
    #while startQuestion is yes, start executing the game.
    while startQuestion=="yes":
        #Print out the list of elements and ask if users are ready(readyQuestion)
        print("\nOkay!Here is a list of sports:")
        for i in sportList:
            print(f"{i}")
        readyQuestion=input("\nChoose one and I will try to guess it. Are you ready to begin?[yes/no]: ")
        if readyQuestion=="yes":
            print("\nOKAY, Lets Begin, Please Answer all yes/no questions by typing \"yes\" or \"no\" ")
        #While readyQuestion is yes and the currentData of the game is not a leaf, execute setNextData until it reaches to the leaf
        while readyQuestion=="yes" and game.isThisLeaf()==False:
            answer1=input(game.getData())
            game.setNextData(answer1)
        #If the currentData reaches a leaf, ask if users were thinking of the currentData.
        if game.isThisLeaf()==True:
            answer2=input(f"Were you thinking of {game.getData()}? ")
            #If the user was thinking of the same data, celebrate
            if answer2=="yes":
                print("Yay I guessed it!")
            #else, sound confused
            elif answer2=="no":
                print(f"Oh, I was wrong?it wasn't {game.getData()}? ")
                #IF game is Unrestricted add Data to tree if the users want to.
                if version=="Unrestricted":
                    shouldAdd=input("\nWould you like to add to dataset? ")
                    #If uesrs say that they want to add data to the current dataset, execute setWrongData from UnrestrictedGuessingGame class and change data.
                    if shouldAdd=="yes":
                        thing = input("What is the sport you were thinking of? ")
                        sportList.append(thing)
                        question = input(f"Please give me a yes or no question that would have distinguished it from {game.getData()}: ")
                        answer = input(f"Is the answer to {thing} yes or no? ")
                        game.setWrongData(thing,question,answer)
            #Once a round has been complete, ask users if they want to play again, set this equal to startQuestion so that first while loop can be manipulated and game can end when directed to do so.
            startQuestion=input("\nDo you want to play again? ")
            #Set the currentData to root
            currentNode=game.setToRoot()

        #If startQuestion is no, do not play game
        if startQuestion=="no":
            print("Okay!Bye!")

def main():
    #Take in tree.txt file and convert to tree
    newTree = GameTreeReader("tree.txt").getTree()
    #create an object of GuessingGame with newTree
    game = GuessingGame(newTree)
    playGame(game,"Restricted")

if __name__=="__main__":
    main()
