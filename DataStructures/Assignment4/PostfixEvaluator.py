#Elizabeth(Che Rin) Yu
#Assignment 4
#PostfixEvaluator: This file reads the postfix arithmetic  in testdata.txt and evaluates the expression.

import sys
from Stack import Stack

def main():
    #open and read testdata.txt
    fi = open("testdata.txt","r")
    #read one line from testdata.txt, name this line
    line = fi.readline()
    #while the EOF char is an empty string.
    while line!="":
        #Create a stack for the operands.
        operands=Stack()
        #iterate through the line.
        for i in line:
            #if the element in line is an operand, it will not the following properties:
                #+,-,*,/, space, and newline
            if i!="+" and i!="-" and i!="*" and i!="/" and i!=" " and i!="\n":
                #if line is an operand push into the operands stack
                operands.push(i)
            #else, if the element is an operator,
            elif i=="+" or i=="-" or i=="*" or i=="/":
                #pop the most recent operand, and name it first
                first=int(operands.pop())
                #pop the second most recent operand, and name it second
                second=int(operands.pop())
                #if the element is +
                if i=="+":
                    #add second to first, name it val
                    val=second+first
                #if the element is -
                elif i=="-":
                    #subtract second to first, name it val
                    val=second-first
                #if the element is *
                elif i=="*":
                    #multiply second to first, name it val
                    val=second*first
                #if the element is /
                elif i=="/":
                    #multiply second to first, name it val
                    val=second//first
                #Push val into operands stack
                operands.push(val)
        #print the postfix arithmetic along with the answer, which is the last val
        print(line[:len(line)-1],f"results in {operands.peek()}")
        #get the next line in testdata.txt
        line=fi.readline()
    #close the file after it has all been read
    fi.close()

if __name__=="__main__":
    main()
