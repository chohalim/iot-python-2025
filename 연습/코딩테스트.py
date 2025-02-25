def isQueueFull():
    global SIZE, queue, front, rear 
    while (rear == SIZE-1):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear 
    while (front == rear):
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear 
    while (isQueueFull()):
        print('큐가 꽉 찼습니다.')
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear 
    while (isQueueEmpty()):
        print('큐가 비었습니다.')
        return None
    front += 1
    data = queue[front]
    queue[front] = None

    for i in range(front+1, rear+1):
        queue[i-1]=queue[i]
        queue[i] = None
    front = -1
    rear -= 1

    return data

def peek():
    global SIZE, queue, front, rear 
    while (isQueueEmpty()):
        print('큐가 비었습니다.')
        return None
    return queue[front+1]

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__=='__main__':
    enQueue=[]
    