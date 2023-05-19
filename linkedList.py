class node():
    def __init__(self):
        self.val = 0
        self.next = 0
    


if __name__ == "__main__":
    #create a linked list
    head = node()
    head.val = 1
    curr = head
    #make 4 more nodes:
    for x in range(4):
        newNode = node()
        newNode.val = x+2
        curr.next = newNode
        curr = curr.next


    #we have a lined list
    #how do we reverse it?
    #start with a brut force solution
    #make a reference to the next element in the list
    #set the current node's next pointer to

    #this is how I reverse a linked list 
    #the stack solution is o(n) runtime and o(n) space
    myStack = []
    curr = head
    while(curr.next):
        myStack.append(curr)
        curr = curr.next

    newHead = curr
    
    while(myStack):
        curr.next = myStack.pop()
        curr = curr.next    

    curr.next = 0#the tail of the linked list, set next to 0

    #another solution is to use three pointers, 
    #the solution to use three pointers is less complex in space or time than the solution with a stack?
    #the three pointer solution is o(n) time and o(1)space

    curr = newHead
    
    while(curr.next):
        print(curr.val)
        curr = curr.next
    print(curr.val)


    #reverse it again with the three pointers method
    #need three pointers
    curr = newHead
    prev = 0
    while(curr.next):
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    curr.next = prev
    
    print()
    while(curr.next):
        print(curr.val)
        curr = curr.next
    print(curr.val)

    #print(head)#object
    #print(head.val)#one
    #print(head.next)#object
    #print(head.next.val)#two


