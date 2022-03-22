from LinkedListNode import LinkedListNode as Node

class UnorderedLinkedList:
    def __init__(self):
        self.head = None

    def add(self,item):
        # add new item at list head
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def append(self, item):
        # add new item at end of list
        temp = Node(item)
        current = self.head
        if current == None:
            self.head = temp # list was empty, add element
        else:
            previous = None
            while current != None:
                previous = current
                current = current.getNext()
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head

        while current != None:
            if current.getData() == item:
                return True
            current = current.getNext()

        return False

    def remove(self,item):
        # remove item that has specified value
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # if current == None, then item was not found
        if current == None:
            return
        if previous == None:  # removing first list item
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return

    def pop(self, index):
        if self.head == None:
            return None
        current = self.head
        count = 0
        while count < index:
            current = current.getNext()
            count += 1
        name = current.getData()
        self.remove(name)
        return name

    def __str__(self):
        outString = ''
        current = self.head
        while current != None:
            outString += str(current.getData()) + "\n"
            current = current.getNext()
        return outString
