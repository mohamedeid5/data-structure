class Queue:
    front = -1
    rear = -1
    capacity = 5
    arr = []

    def enqueue(self, val):
        if self.isFull():
            return
        self.arr.append(val)
        self.rear += 1

    def dequeue(self):
        if self.isEmpty():
            return
        elif self.front == self.rear:
            self.front = self.rear = -1
        self.front += 1

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True

    def isFull(self):
        if self.rear == self.capacity - 1:
            return True
        else:
            return False

    def front_val(self):
        return self.arr[self.front]

    def printQueue(self):
        for i in range(self.front, self.rear):
            print(self.arr[i])


queue = Queue()
queue.enqueue(1)
queue.enqueue(4)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(2)

queue.dequeue()
queue.dequeue()


queue.printQueue()
