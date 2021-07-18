# doubly linked list

class Node():
    
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None
        
        
class DoublyLinkedList():
    
    def __init__(self):
        self.head = None
        
    def append(self, val):
        
        node = Node(val)
        
        if self.head == None:
            self.head = node
        
        else:
            
            temp = self.head
        
            while temp.next != None:
                temp = temp.next

            temp.next = node
            node.prev = temp
    
    def insert_at_pos(self, val, pos):
        
        node = Node(val)   
        
        if self.head == None:
            self.head = node 
            return  
        
        if pos == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return
        
        temp = self.head
        
        for i in range(0, pos):
            # if user add big number then add it in the end of the linked list
            if temp.next == None:
                self.append(val)
                return
            temp = temp.next
            
        
        node.prev = temp.prev
        temp.prev.next = node
        temp.prev = node
        node.next = temp
        
    def remove(self, val):
        
        if self.head == None:
            return
        
        temp = self.head
        
        if temp.data == val:
            self.head = temp.next
            if self.head != None:
                self.head.prev = None
            del temp
            return
        
        while temp.data != val and temp != None:
            temp = temp.next
        
        if temp == None:
            return
        
        temp.prev.next = temp.next
        if temp.next != None:
            temp.next.prev = temp.prev
        del temp
        
    def remove_at_pos(self, pos):
        
        temp = self.head
        
        if pos == 0:
            self.head = temp.next
            if self.head != None:
                self.head.prev = None
            del temp
        
        for i in range(0, pos):
            temp = temp.next
        
        temp.prev.next = temp.next
        if temp.next != None:
            temp.next.prev = temp.prev
        
        del temp
        
    
    def display(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def reverse_display(self):
        
        temp = self.head
        
        if temp == None:
            return
        
        while temp.next != None:
            temp = temp.next
        
        while temp != None:
            print(temp.data)
            temp = temp.prev
            
                  
