class LinkedListNode:
    '''
    LinkedListNode

    Instance variables:
        data
        next
    '''

    def __init__(self, initialData):
        self.data = initialData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def length(self):
        if self.getNext()==None:
            return 1
        return 1+self.getNext().length()

    def nodeSearchR(self, value):
      if self.getData()==value:
        return True
      elif self.getNext() == None:
        return False
      else:
        return self.getNext().nodeSearchR(value)

    def indexAtNode(self,item):
        if self.getNext()==None:
            return 0
        return 1+self.getNext().indexAtNode()
