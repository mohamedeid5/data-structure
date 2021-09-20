from Queue import Queue
    

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
    
    def getHeightHelper(self, temp):
        
        if temp == None:
            return -1
        
        leftSubTree = self.getHeightHelper(temp.left)
        rightSubTree = self.getHeightHelper(temp.right)
    
        return max(leftSubTree, rightSubTree) + 1
    
    def getHeight(self):
        
        if self.root == None:
            return -1
        else:
            return self.getHeightHelper(self.root)
        
    def display_level_order(self):
        
        if self.root == None:
            return
        
        
        queue = Queue()
        
        queue.enqueue(self.root)
                
        while not queue.isEmpty():
            
            current = queue.front_value()
           
            queue.dequeue()
            
            print(current.data)
            
            if current.left != None:
                queue.enqueue(current.left)
            if current.right != None:
                queue.enqueue(current.right)
                
    def preorderHelper(self, temp):
        
        if temp == None:
            return
        
        #preorder
        print(temp.data)
        
        self.preorderHelper(temp.left)
        
        #inorder
        #print(temp.data)
        
        self.preorderHelper(temp.right)
        
        #postorder
       # print(temp.data)
        
                
    def preorder(self):
        
        if self.root == None:
            return
        
        return self.preorderHelper(self.root)

    def removeHelper(self, root, data):
        
        if root == None:
            return root
        
        elif data < root.data:
            root.left = self.removeHelper(root.left, data)
            
        elif data > root.data:
            root.right = self.removeHelper(root.right, data)
        
        else:
            if root.left == None:
                temp = root.right
                del root
                return temp
            elif root.right == None:
                temp = root.left
                del root
                return temp
            else:
                maxValue = self.maxHelper(root.left)
                root.data = maxValue
                root.left = self.removeHelper(root.left, maxValue)
        return root
    
    def remove(self, data):
        self.root = self.removeHelper(self.root, data)
        
        