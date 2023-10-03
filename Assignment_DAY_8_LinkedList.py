class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
        
class LinkedList:
    def __init__(self):
        self._first = None
        self._last = None

    def append(self, value):
        new_node = Node(value)
        if self._first==None: # list is empty
            self._first  = new_node
            self._last = new_node
        
        ## add to the last node of the linkedlist
        ## optimized append function to take O(1) time 
        else:
            self._last._next = new_node
            new_node._previous = self._last
            self._last = new_node
        
    def get_first_last(self):
        first = self._first._value if self._first else None
        last = self._last._value if self._last else None
        print(f'first : {first}, last: {last}')

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c
    
    def node_at_pos(list, pos):
        n=list._first
        for i in range(pos):
            n=n._next
            if n==None:
                break
        return n
    
    def get(list,index):
        node = list.node_at_pos(index)
        return node._value

    def set(list,index,value):
        node = list.node_at_pos(index)
        node._value=value
        
    def traverse_till_index(list, index):
        y=list._first
        for i in range(index):
            y=y._next
            if y==None:
                return
        return y

    def insert(list, index, value):
        
        y = list.node_at_pos(index)
        print(y._value)
        x=y._previous

        new_node=Node(value,previous=x,next=y)
        
        if x:
            x._next=new_node
        else:
            list._first = new_node

        y._previous=new_node
        
    def remove(list, index):
        
        n = list.node_at_pos(index)
        x = n._previous
        y = n._next

        if x:
            x._next=y
        else:
            list._first = y
        if y:
            y._previous=x
        else:
            list._last = x
        return n._value
    
    def is_node_in_list(self, value):
        # traverse each node to check if it's value is given value
        
        n = self._first 
        while(n is not None):
            if(n._value == value):
                return True
            n = n._next
        return False
    
    def count(self, value):
        # traverse each node to check if it's value is given value
        
        n = self._first 
        count = 0
        while(n is not None):
            if(n._value == value):
                count += 1
            n = n._next
        return count

def check_if_node_present():
    l1 = LinkedList()
    l1.append(11)
    l1.append(22)
    l1.append(33)
    
    print(l1.is_node_in_list(11))
    print(l1.is_node_in_list(1))

check_if_node_present()

def get_count_value():
    l2 = LinkedList()
    l2.append(1)
    l2.append(3)
    l2.append(8)
    l2.append(1)
    
    print(l2.count(1))
    print(l2.count(3))

get_count_value()

