"""
Created on Mon Jan 23 15:48:26 2017

@author: sominwadhwa

Palindrome or NOT
"""

class Node(object):
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.data)
        

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def append(self,data):
        if not self.head:
            node = Node(data)
            self.head = node
        else:
            node = self.head
            while (node.next != None):
                node = node.next
            new_node = Node(data)
            node.next = new_node
            new_node.prev = node
            return
    def delete(self, d):
        if (self.head.data == d):
            self.head = self.head.next
        else:
            current = self.head
            while (current.next != None and current.data != d):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
    def checkPalindrome(self):
        if self.head.next == None:
            print ("True")
            return
        else:
            start = self.head
            end = self.head
            flag = 0
            while (end.next != None):
                end = end.next
            while (start.next != None):
                if (start.data != end.data):
                    flag = 1
                    break
                else:
                    pass
                start = start.next
                end = end.prev
            if (flag==0):
                print ("PALINDROME!!")
                return
            elif (flag == 1):
                print("NOT A PALINDROME!!!")
                return
    def printList(self):
        node = self.head
        while (node):
            print (str(node))
            node = node.next

newList = LinkedList()
newList.append(1)
newList.append(2)
newList.append(3)
newList.append(2)
newList.append(1)
newList.printList()
print ("--------------")
newList.checkPalindrome()

