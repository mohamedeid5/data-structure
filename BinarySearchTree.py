#main

class Node():
    
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class Tree():
    
    def __init__(self):
        self.root = None
        
    def addHelper(self, temp, val):
                    
        if val > temp.data:
            if temp.right is None:
                temp.right = Node(val)
            else:
                self.addHelper(temp.right, val)
        else:
            if temp.left is None:
                temp.left = Node(val)
            else:
                self.addHelper(temp.left, val)
    
    def add(self, val):
        
        if self.root is None:
            self.root = Node(val)
            return
        else:
            self.addHelper(self.root, val)
            
    def maxHelper(self, temp):
        
        if temp.right is None:
            return temp.data
        else:
            return self.maxHelper(temp.right)
            
    def max(self):
        
        return self.maxHelper(self.root)
    
    def minHelper(self, temp):
        if temp.left is None:
            return temp.data
        else:
            return self.minHelper(temp.left)
        
        
    def min(self):
        
        return self.minHelper(self.root)
                         

