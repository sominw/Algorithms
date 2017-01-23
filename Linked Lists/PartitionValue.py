"""
Created on Mon Jan 23 15:48:26 2017

@author: sominwadhwa

Paritioning around a given value
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
    def removeDups(self):
        if (self.head is None):
            print ("Fasle")
        else:
            p1 = self.head
            while (p1.next != None):
                p2 = p1
                while (p2.next != None):
                    if (p1.data == p2.next.data):
                        p2.next = p2.next.next
                    else:
                        p2 = p2.next
                p1 = p1.next
        
    def printList(self):
        node = self.head
        while (node):
            print (str(node))
            node = node.next

newList = LinkedList()
newList.append(1)
newList.append(2)
newList.append(3)
newList.append(4)
newList.append(5)
newList.append(6)
newList.append(3)
newList.printList()
newList.removeDups()
print ("--------------")
newList.printList()

