from random import sample
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return self.data

class Stack(object):
    def __init__(self):
        self.top = None
    def push(self,data):
        if (self.top == None):
            node = Node(data)
            self.top = node
        else:
            node = Node(data)
            node.next = self.top
            self.top = node
    def pop(self):
        if (self.top == None):
            return ("Underflow")
        else:
            item = self.top.data
            self.top = self.top.next
            return item
    def isEmpty(self):
        if (self.top == None):
            return True
        else:
            return False
    def peek(self):
        return self.top.data

if __name__=='__main__':
    stack1 = Stack()
    li = sample((range(0,50)),10)
    for i in li:
        stack1.push(i)
    stack2 = Stack()
    while(stack1.isEmpty() == False):
        item = stack1.pop()
        while(stack2.isEmpty() == False and stack2.peek() > item):
            stack1.push(stack2.pop())
        stack2.push(item)
    while (stack2.isEmpty() == False):
                stack1.push(stack2.pop())
    while (stack1.isEmpty() == False):
        print (stack1.pop())


