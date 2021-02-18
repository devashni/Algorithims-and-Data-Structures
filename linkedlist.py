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

        def add(self, value):
        if self.head == None:
            self.head = Node(value, None)
            self.tail = self.head
        else:
            self.tail.next = Node(value, None)
            self.tail = self.tail.next
        return

    def print(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

def print_nodes(node1):
    print("going to print the list now!")
    cur = node1

    while cur != None:
        print(cur.data)
        cur = cur.next

def add_node(cur, value):
    if cur == None:
        return Node(value, None)
    else:
        cur.next = Node(value, None)
        return cur.next

# Create first element of the list.
# node1 = None
# cur = node1

# for i in range(1, 5):
#     cur = add_node(cur, i)
#     if i == 1:
#         node1 = cur

# print_nodes(node1)

lst = LinkedList()

lst.add(1)
lst.add(2)
lst.add(3)
lst.add(4)

lst.print()

    def reverseList(self, head: ListNode) -> ListNode:
        #input validity check
        if head == None:
            return None
        
        #set the previous_pointer variable
        previous_pt = None
        
        while True:
            #save the 'next' node in chain in nxt variable
            nxt = head.next
            
            #update the .next of the current node to previous_pointer
            head.next = previous_pt
            
            #update previous_pointer to current node
            previous_pt = head
            
            #point Linked List head to the new head node
            if nxt != None:
                head = nxt
            else:
                return head