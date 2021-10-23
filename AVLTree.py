class Node():
    
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1
        

class AVlTree():
    
    def __init__(self):
        self.root = None
    
    def addHelper(self, root, val):
        
        if not root:
            return Node(val)
        if val < root.data:
            root.left = self.addHelper(root.left, val)
        else:
            root.right = self.addHelper(root.right, val)
            
        # update hight
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        balance = self.getBalance(root)
        
        # case 1 left left 
        if balance > 1 and val < root.left.data:
            return self.rightRotate(root)
        
        # case 2 right right 
        if balance < -1 and val > root.right.data:
            return self.leftRotate(root)
        
        # case 3 left right
        if balance > 1 and val > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
                    
        # case 4 right left
        if balance < -1 and val < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def add(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        else:
            self.addHelper(self.root, val)
            
    def leftRotate(self, z):
        
        y = z.right
        T2 = y.left
        
        # Perform rotation
        y.left  = z
        z.right = T2
        
        # update heights
        z.height = 1 + max(self.getHeight(z.left, z.right))
        y.height = 1 + max(self.getHeight(y.left, y.right))
        
        return y
    
        
    def rightRotate(self, z):
        
        y = z.left
        T2 = y.right
        
        # Perform rotation
        y.right = z
        z.left  = T2
        
        # update heights
        z.height = 1 + max(self.getHeight(z.left, z.right))
        y.height = 1 + max(self.getHeight(y.left, y.right))
        
        return y
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    


