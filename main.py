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
                         


tree = Tree()
tree.add(2)
tree.add(5)
tree.add(10)
tree.add(15)
tree.add(34)
tree.add(1)
tree.add(29)
tree.add(290)
tree.add(1000)
tree.add(23)
tree.add(0)


print(tree.max())
print(tree.min())
