# stack linked list

class Node():
    
    def __init__(self, data):
        self.data = data 
        self.next = None  
        
        
class Stack():
    
    def __init__(self):
        self.head = None
        
    def push(self, val):
        
        node = Node(val)
        
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def pop(self):
        
        if self.isEmpty():
            return
        else:
            temp = self.head
            self.head = self.head.next
            del temp
        
    def topVal(self):
        if self.isEmpty():
            return
        return self.head.data
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
