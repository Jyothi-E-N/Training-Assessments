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
        
    # append the node to the SLL
    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    # insert the node with given value at the given position
    def insert(self, val, index):
        new_node = Node(val)
        current_node = self.head
        position = 0
        if position == index:
            self.append(val)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
             
            if current_node != None:
                 
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                return "Index not present"

    # get value from a given position
    def get(self, pos):
        if(pos == 1) return self.head
        ref = self.head
        count = 1
        while(count<pos and ref!=None):
            ref = ref.next
            count += 1
            
        if(count == pos):
            return ref
        else:
            return "Invalid Position"

    # set value at a given position
    def set(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.val = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.val = val
            else:
                return "Index not present"

    # return the size of linkedlist
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
    
            
    def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            rem_val = self.head.val
            self.head = current_node.next
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                rem_val = current_node.next.val
                current_node.next = current_node.next.next
                
            else:
                return "Index not present"
        return rem_val
            
    # get list info
    def info(self):
        current_node = self.head
        while(current_node):
            print(current_node.val, end = '-->')
            current_node = current_node.next
        print()

    # clear all the items in the linked list
    def clear(self):
        self.head = None
        return "All the elements in the SLL are cleared."
       
def test_SLL():
    sll = SLL()
    sll.info()
    sll.append(1)
    sll.info()

    print()

    sll.append(12)
    sll.info()

    print()
    print(sll.insert(2, 3))
    sll.info()

    print()
    print(sll.insert(2,1))
    sll.info()

    print()
    print(sll.sizeOfLL())

    print()
    print(sll.remove_at_index(0))
    sll.info()

    print()
    print(sll.clear())
    sll.sizeOfLL()
    sll.info()

test_SLL()
