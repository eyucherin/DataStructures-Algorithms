from UnorderedLinkedList import UnorderedLinkedList
#from LinkedListNode import LinkedListNode as Node

def main():
    L = UnorderedLinkedList()
    L.add(1)
    L.add(2)
    L.add(3)
    L.add(4)
    L.add(5)
    print(L.sizeR()) ## output 5
    print(L.searchR(3)) ## output True
    print(L.searchR(17))  ## output False
    #print(L.indexOf(3))  ## output 2
    #print(L.indexOf(6))  ## output -1

main()
