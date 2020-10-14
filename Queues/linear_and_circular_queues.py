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
                print("From now on, you can no longer enQueue to this queue as it has reached its maximum size.")
        else: print("Unable to enQueue. The queue is full.")

        

    def deQueue(self):
        if self.isEmpty() == False:
            value = self.queue[self.front]
            self.front +=1
            if self.front > self.rear:
                self.queueEmptyIndex = self.front
                self.rear = None
                self.front = None
            return value
        else: return "Unable to deQueue. The queue is empty."


    def showQueue(self):
        if self.isEmpty() == False:
            for i in range(self.queueSize()):
                print(self.queue[self.front + i])
        else: print("Queue Is Empty.")
        return ''

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
        return ("="*20)

def end():
    exit()

def list_of_commands():
    print('''List Of Commands:

enqueue value ==> adds value to queue
dequeue ==> removes item at the front of the queue, and returns its value
isempty ==> returns if queue is full or not
isfull ==> returns if queue is empty or not
showqueue ==> returns queue
size ==> returns current size of queue
debug ==> returns information about queue and the array it is in
end ==> ends the program
commands ==> shows this list of commands''')
    return ''
    
print("\nQUEUES v1, Type 'commands' For List Of Commands")

queue1 = linearQueue(int(input("\nInitialise Queue Length:")))

commands_dic = {
    "enqueue": queue1.enQueue,
    "dequeue": queue1.deQueue,
    "isempty": queue1.isEmpty,
    "isfull": queue1.isFull,
    "showqueue": queue1.showQueue,
    "size": queue1.queueSize,
    "debug": queue1.debugQueue,
    "end": end,
    "commands":list_of_commands,
    }

valid = True
while valid:
    try:
        user_input = input("\n>")
        print("")
        user_input = user_input.split()
        command = user_input[0]
        if len(user_input)>1:
            value = user_input[1]
            commands_dic[command](value)
        else:
            print(commands_dic[command]())
    except:
        print("Invalid Input.")
        

