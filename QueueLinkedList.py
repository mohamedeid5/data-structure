# queue linked list

class Node():
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    
    def __init__(self):
        self.front = None
        self.tail = None
    
    def enqueue(self, data):
        
        node = Node(data)
        
        if self.isEmpty():
            self.front = self.tail = node
            return
        self.tail.next = node
        self.tail = node
        
    def dequeue(self):
        
        if self.isEmpty():
            return
        
        if self.front == self.tail:
            self.front = self.tail = None
            return

        temp = self.front

        self.front = temp.next
        del temp
        
    
    def isEmpty(self):
        if self.front == None and self.tail == None:
            return True
        else:
            return False
        
    def getFront(self):
        print(self.front.data)
        
    def getTail(self):
        print(self.tail.data)
        
    def dispaly(self):
        temp = self.front
        while not self.isEmpty():
            print(temp.data)
            temp = temp.next
            self.dequeue()
        



