class linearQueue():
    def __init__(self,maxSize):
        self.maxSize = int(maxSize)
        self.queue = []
        self.front = None
        self.rear = None
        self.queueEmptyIndex = 0
        self.size = 0

    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    def isFull(self):
        if len(self.queue) == self.maxSize:
            return True
        else:
            return False

    def enQueue(self,item):
        if self.isFull() == False:
            if self.front == None:
                self.front = self.queueEmptyIndex
                self.rear = self.queueEmptyIndex - 1
            self.rear+=1
            self.queue.append(item)
            if len(self.queue) == self.maxSize:
                print("The list can no longer enQueue from now as its maximum size has been reached.")
        else: print("Unable to enQueue. The queue is full.")

        

    def deQueue(self):
        if self.isEmpty() == False:
            self.front +=1
            if self.front > self.rear:
                self.queueEmptyIndex = self.front
                self.rear = None
                self.front = None
        else: print("Unable to deQueue. The queue is empty.")


    def showQueue(self):
        if self.isEmpty() == False:
            for i in range(self.queueSize()):
                print(self.queue[self.front + i])
        else: print("Queue Is Empty.")

    def queueSize(self):
        if self.isEmpty()==True:
            self.size = 0
        else:
            self.size = self.rear - self.front + 1
        return self.size

    def debugQueue(self):
        print("="*20)
        print("INFO:")
        print("The Array:",self.queue)
        print("Front Pointer:",self.front)
        print("Rear Pointer:", self.rear)
        tempQueue = []
        if self.isEmpty()==False:
            for i in range(self.rear - self.front + 1):
                tempQueue.append(self.queue[self.front + i])
        print("The Queue:",tempQueue)
        print("Size:",self.queueSize())
        print("isEmpty():",self.isEmpty())
        print("isFull():",self.isFull())
        print("="*20)

    

test = linearQueue(5)
test.enQueue("One")
test.enQueue("2")
test.deQueue()
test.deQueue()
test.enQueue("1")
test.enQueue("2")
test.debugQueue()
print(test.queue)
test.showQueue()

