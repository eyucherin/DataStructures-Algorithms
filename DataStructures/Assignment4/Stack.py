from UnorderedLinkedList import UnorderedLinkedList as LinkedList
from LinkedListNode import LinkedListNode

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, new_item):
        self.ll.add(new_item)

    def pop(self):
        popped_item = self.ll.head.getData()
        self.ll.head = self.ll.head.getNext()
        return popped_item

    def peek(self):
        return self.ll.head.getData()

    def __str__(self):
        return self.ll.__str__()
