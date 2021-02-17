#Linked list practice
class Node ():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None 
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        index_counter = 0 
        temp_node = self.head #[0,1,2] Sample LL
        
        if index == 0 and temp_node != None:
            return temp_node.data
            
        while index_counter <= index-1:
            if temp_node == None :
                return -1
            else:
                temp_node = temp_node.next
                index_counter +=1
            
        return temp_node.data
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        current_head = self.head
        if current_head == None:
            add_node = Node(val)
            self.head = add_node
            self.tail = add_node
        else:
            add_node = Node(val,current_head)
            self.head = add_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current_tail = self.tail
        if current_tail == None:
            add_node = Node(val)
            self.tail = add_node
            self.head = add_node
        else:
            add_node = Node(val)
            self.tail.next = add_node
            self.tail = add_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val 'before' the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        temp_node = self.head
        index_counter = 0
        
        if index == 0:
            self.addAtHead(val)
        
        else:
            while index_counter <= index:

                if index_counter == index-1: #[0,1,X,2,3] #index= 2 => 1.next =x, x.next = 2
                    previous_node = temp_node
                    next_node = temp_node.next
                    new_node = Node(val,next_node)
                    previous_node.next = new_node

                elif index_counter  == index:
                    self.addAtTail(val)

                index_counter +=1
                temp_node = temp_node.next
            
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        ctr = 0
        current = self.head
        
        prev = None
        while current != None and ctr < index: #will only go into this loop if index is 1 or greater
            prev = current
            current = current.next
            if current != None:
                ctr += 1

        # delete the node
        if prev == None:
            self.head = None
            return
        
        # delete the current node
        prev.next = current.next
        # if tail was deleted, move tail back
        if current == self.tail:
            self.tail = prev

