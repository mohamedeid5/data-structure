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
            
    
    def display(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
                
        
linkedlist = LinkedList()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)

linkedlist.remove(1)


linkedlist.display()