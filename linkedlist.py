# linked list

class Node():
    
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList():
    
    def __init__(self):
        self.head = None
        
    def append(self, val):
        
        node = Node(val)
        
        if not self.head:
            self.head = node
        else:
            
            temp = self.head
            
            while temp.next != None:
                temp = temp.next
            
            temp.next = node
            
            
    def insert_at_pos(self, val, pos):
        
        node = Node(val)
        
        if pos == 0:
            node.next = self.head
            self.head = node
            return
        
        temp = self.head
        
        for i in range(0, pos-1):
            if temp.next == None:
                return
            temp = temp.next
        
        node.next = temp.next
        temp.next = node
        
            
    def remove(self, val):
        
        temp = self.head
        prev = None
        
        if temp == None:
            return
        
        # If head node itself holds the key to be deleted
        if temp.data == val:
            self.head = temp.next
            del temp
            return
        
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp.data != val and temp != None:
            prev = temp
            temp = temp.next
            
        # if key was not present in linked list    
        if temp == None:
            return
           
        # Unlink the node from linked list    
        prev.next = temp.next
        del temp
        
    def remove_at_pos(self, pos):
        
        if self.head == None:
            return
        
        if pos == 0:
            temp = self.head
            self.head = self.head.next
            del temp
            return
        
        temp = self.head
        
        for i in range(0, pos-1):
           temp = temp.next
        
        #  
        if temp.next == None:
               return
       
        temp2 = temp.next
        
        temp.next = temp.next.next
        
        del temp2
        
    def reverse(self):
        
        if self.head == None:
            return
        
        prev  = None
        curr  = self.head
        nextt = None
            
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
            
        self.head = prev
            
            
    def display(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
                
