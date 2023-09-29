class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
        
class LinkedList:
    def __init__(self):
        self._first=None

    def append(self, value):
        if self._first==None: # list is empty
            self._first=Node(value)
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)

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
        else:
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
        
        y = list.traverse_till_index(index)
        x=y._previous

        new_node=Node(value,previous=x,next=y)
        
        if x:
            x._next=new_node
        else:
            list._first=new_node

        y._previous=new_node
        
    def remove(list, index):
        
        n = list.traverse_till_index(index)
        x= n._previous
        y= n._next

        if x:
            x._next=y
        else:
            list._first=y

        if y:
            y._previous=x
        return n._value

