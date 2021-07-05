# main

class CircularQueue():
    
    front = rear = -1
    capcity = 5
    arr = [None] * capcity
    
    def enqueue(self, val):
        if self.isFull():
            print('queue is full')
            return
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capcity
        self.arr[self.rear] = val
        
    def dequeue(self):
        if self.isEmpty():
            print('queue is empty')
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capcity
    
    def isEmpty(self):
        if self.rear == -1 and self.rear == -1:
            return True
        else:
            return False
        
    def isFull(self):
        if (self.rear + 1) % self.capcity == self.front:
            return True
        else:
            return False
        
    def front_value(self):
        if self.isEmpty():
            return 'queue is empty'
        return self.arr[self.front]
    
    def print_queue(self):
        while not self.isEmpty():
            print(self.front_value())
            self.dequeue()

    

    
qu = CircularQueue()


qu.print_queue()

    
