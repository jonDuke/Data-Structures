"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create and add the new node
        new_node = ListNode(value, prev=None, next=self.head)
        self.length += 1

        # if we had an old head, update it's previous link
        if self.head:
            self.head.prev = new_node
        
        # update head (and tail if necessary)
        self.head = new_node
        if self.length == 1:
            self.tail = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # return None if list is empty
        if self.length == 0:
            return None
        
        value = self.head.value  # save value to return later

        # remove links to the old head
        self.head = self.head.next
        self.length -= 1

        # if that was the last node, update tail too
        if self.length == 0:
            self.tail = None

        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create and add the new node
        new_node = ListNode(value, prev=self.tail)
        self.length += 1

        # if we had an old tail, update it's previous link
        if self.tail:
            self.tail.next = new_node
        
        # update tail (and head if necessary)
        self.tail = new_node
        if self.length == 1:
            self.head = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # return None if list is empty
        if self.length == 0:
            return None
        
        value = self.tail.value  # save value to return later

        # remove links to the old tail
        self.tail = self.tail.prev
        self.length -= 1

        # if that was the last node, update head too
        if self.length == 0:
            self.head = None

        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # link nodes before and after together
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.next

        # update head and tail pointers
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # return None if list is empty
        if self.length == 0:
            return None
        
        # assume first value we see is highest
        max = self.head.value
        current = self.head.next

        # go through all values in list, saving them if they are higher
        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next
        
        return max
