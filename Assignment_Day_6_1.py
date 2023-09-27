# create a node class that represents the each node in a linkedlist

class Node():
    
    # node contains a value and next pointer 
    def __init__(self, val, next = None):
        
        self.val = val
        self.next = next 

class SLL():
    
    # creating the empty linkedlist that's head pointing to the None
    def __init__(self):
        self.head = None
        self.size = 0
        
    
    # append the node to the SLL
    def append(self, val):
        
        new_node = Node(val)
        
        if(self.size == 0):
            self.head = new_node
        else:
            ref = self.head
            
            while(ref.next != None):
                ref = ref.next
                
            # we get the tail of SLL in ref
            ref.next = new_node
        self.size += 1
        
    # check if given position is valid or not
    # if valid return node otherwise return -1
    def isValidPos(self, pos):
        
        return (pos<=self.size)
            
    # insert the node with given value at the given position
    def insert(self, val, pos):
        
        # check if the given position is valid or not
        if(self.size == 0 and pos == 1):
            new_node = Node(val)
            self.head = new_node
        
        print(self.isValidPos(pos))
        elif(isValidPos(pos) == False):
            print(self.isValidPos(pos))
            print("checked")
            return "Invalid Position"
        
        else: 
            # get the node at that position
            
            ref = self.head
            count = 1
            
            while(count != pos):
                ref = ref.next
                count += 1
            
            new_node = Node(val)
            new_node.next = ref.next
            ref.next = new_node
        
        self.size += 1
        return f'Given value {val} is successfully inserted at positon {pos}'
    
    # get value from a given position
    def get(self, pos):
        
        ref = self.head
        count = 1
        while(count<self.size and count< pos):
            ref = ref.next
            count += 1
            
        if(count == pos):
            return ref
        else:
            return "Invalid Position"
        
    # set value at a given position
    def set(self, new_val, pos):
        # assuming that given position is already valid
    
        ref = self.head
        count = 1
        while(count < pos):
            ref = ref.next
            count += 1
            
        ref.val = new_val
        return f"Given position Node's value is updated to {new_val} successfully"
    
    # return the size of linkedlist
    def size_sll(self):
        return self.size
    
    
    # get list info
    def info(self):
        ref = self.head
        
        if(self.size == 0):
            return "Single linked list is empty" 
        
        while(ref != None):
            print(ref.val, end = '-->')
            ref = ref.next
            
        print()
    
    # remove and return the element from the given position
    def remove(self, pos):
        
        if(isValidPos(pos) == False):
            return "Invalid position to remove the node"
        else:
            if(self.size == 1):
                rem_val = self.head.val
                self.head = None
            else:
                ref = self.head
                count = 1
            
                while(count<(pos - 1)):
                    ref  = ref.next
                    count += 1

                rem_val = ref.next.val
                ref.next = ref.next.next
            
            self.size -= 1
            return rem_val
        
    # clear all the items
    def clear(self):
        self.head = None
        self.size = 0
        return "All the elements in the SLL are cleared."

def test_SLL():
    
    # creating empty single linked list
    sll = SLL()
    
    print(sll.info())
    
    print(sll.size_sll())
    
    sll.append(1)
    sll.info()

test_SLL()
    
