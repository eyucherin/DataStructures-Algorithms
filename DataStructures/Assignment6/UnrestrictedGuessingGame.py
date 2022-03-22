# Elizabeth (Che Rin) Yu
# Assignment6: UnrestrictedGuessingGame.py
# This file imports executes the same Guessing game from Guessing game but allows users to input data into the dataset
from GuessingGame import GuessingGame
from GuessingGame import playGame
from GameTreeReader import GameTreeReader
from TreeNode import TreeNode
from copy import copy

#Class UnrestrictedGuessingGame, inherits from GuessingGame
class UnrestrictedGuessingGame(GuessingGame):
    #Takes parameter: tree
    #Tree: a txt file that is read in by the program and made into a tree
    def __init__(self,tree):
        super().__init__(tree)
    #Takes parameter thing,question,yesOrNo
        #Thing: The thing that the user was thinking about
        #question: The question that would have distingueshed the computer's answer to the thing
        #yesOrNo: the answer to the question that would yield thing
    def setWrongData(self,thing,question,yesOrNo):
        #Create a copy of currentData so that this item is independent from what is happening in playGame function, set equal to previous. 
        previous=copy(self.getData())
        #set the current data to become a treeNode where the parent is the question and the children are the thing and previous thing depending on yesOrNo
        self.currentData.setData(TreeNode(question))
        #If yes, the thing is the left child and previous is the right child, they are both TreeNodes as well
        if yesOrNo =="yes":
            self.currentData.setLeftChild(TreeNode(thing))
            self.currentData.setRightChild(TreeNode(previous))
        #If no,the thing is the right child and previous is the left child, they are both TreeNodes as well
        elif yesOrNo =="no":
            self.currentData.setRightChild(TreeNode(thing))
            self.currentData.setLeftChild(TreeNode(previous))

def main():
    #Take in tree.txt file and convert to tree
    newTree = GameTreeReader("tree.txt").getTree()
    #create an object of GuessingGame with newTree
    game = UnrestrictedGuessingGame(newTree)
    playGame(game,"Unrestricted")

if __name__=="__main__":
    main()
