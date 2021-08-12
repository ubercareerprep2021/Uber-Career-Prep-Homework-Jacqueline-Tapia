#Implement a Singly Linked List class with the following methods:
#void push(<Node> node) → Adds the node to the end of the list
#<Node> pop() → Removes the last node at the end of the linked list, returns that data
#void insert(uint index,<Node> node) → Adds a single node containing data to a chosen location in the list. If the index is above the size of the list, do nothing
#void remove(uint index) → remove/delete a single node at the index location in the list. If the node doesn’t exist at the index, do nothing
#<Node> elementAt(uint index) → Returns a pointer to the node at the index location in the list. If the node doesn’t exist at the index, return nil/null
#uint size() → Returns the length of the list.
#void printList() → Returns a string representation of the linked list
#Tips:
#First define your Node (contains a data element of integer type, and a next-node element that is a node-pointer).
#Then define a Linked List that links the nodes as per the above methods.

#Node class 
class Node():
    def __init__(self,node):
        self.node = node
        self.nextNode = None

    def setNext(self,node):
        self.nextNode = node

    def getNext(self):
        return self.nextNode

    def getData(self):
        return self.node
    
# Linked List class
class LinkedList():
    def __init__(self,node):
        self.head = Node(node)

    def push(self,node):
        newNode = Node(node)
        curr = self.head
        while curr.getNext() != None:
            curr = curr.getNext()
        curr.setNext(newNode)

    def pop(self):
        curr = self.head
        while curr.getNext() != None:
            prev = curr
            temp = curr
            curr = temp.getNext()
        prev.setNext(None)
        return curr

    def insert(self,unit,node):
        location = unit - 1
        count = 0
        curr = self.head
        while curr != None and count != location:
            prev = curr
            temp = curr
            curr = temp.getNext()
        if count == location:
            temp = curr.getNext()
            curr.setNext(node)
            curr = curr.getNext()
            curr.setNext(temp)
        else:
            return None

    def remove(self, index):
        location = 0
        curr = self.head 
        prevInd = index - 1
        while curr != None:
            if location == prevInd and curr.getNext():
                prev = curr
                temp = curr.getNext().getNext()
                prev.setNext(temp)
                break
            else:
                location += 1
                curr = curr.getNext()

    def elementAt(self, index):
        location = 0 
        curr = self.head
        while curr != None: 
            curr = curr.getNext()
            location += 1
            if location == index:
                return curr.getData()
        return None

    def size (self):
        len = 0
        curr = self.head 
        while curr != None:
            len += 1
            curr = curr.getNext()
        return len 

    def printList(self):
        stringList = ""
        curr = self.head
        while curr != None:
            stringList += str(curr.getData()) + " "
            curr = curr.getNext()
        return stringList

#Testing 
def main():
    #create linked list
    LinkedL = LinkedList(1)

    #Test push method 
    LinkedL.push(2)
    print("Linked List: "+LinkedL.printList() + "\nExpected: 1 2")

    print("\n")

    # Test pop method 
    LinkedL.pop()
    print("Linked List: " +LinkedL.printList() + "\nExpected: 1")

    print("\n")

    #Test remove method
    LinkedL.push(2)
    LinkedL.push(3)
    LinkedL.remove(1)
    print("Linked List: " + LinkedL.printList() + "\nExpected: 1 3")

    print("\n")

    #Test remove when the node doesn't exist
    LinkedL.remove(6)
    print("Linked List: " + LinkedL.printList() + "\nExpected: 1 3")

    print("\n")

    #Test elementAt
    print("Element at 0: "+ str(LinkedL.elementAt(0)) + "\nExpected: 1")

    print("\n")

    #Test elementAt when the node doesn't exist
    print("Element at 4: "+ str(LinkedL.elementAt(0)) + "\nExpected: None")

    print("\n")

    #Test size
    print("Size: " + str(LinkedL.size()) + "\nExpected: 2")

    print("\n")

    #Test insert 
    LinkedL2 = LinkedList(1)
    LinkedL2.push(2)
    LinkedL2.push(4)
    LinkedL2.push(5)
    LinkedL2.push(6)
    LinkedL2.insert(2,3)
    print("Result: "+LinkedL2.printList()+"\nExpected: 1 2 3 4 5 6 ")

    
main()
    



