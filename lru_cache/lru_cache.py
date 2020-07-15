# Allows the test file to import DoublyLinkedList from the other folder
import sys
sys.path.append("../")

from doubly_linked_list.doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.order_list = DoublyLinkedList()
        self.storage = {}
    
    def __len__(self):
        return self.length

    """ returns true if the key exists in this cache, false otherwise """
    def has_key(self, key):
        return key in self.storage

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # check if the key exists
        if not self.has_key(key) or self.length == 0:
            return None
        
        # find the node with this key
        node = self.order_list.find_node(key)
        
        # move that node to the end of the used-order list
        self.order_list.move_to_end(node)
        
        # return the value
        return self.storage[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if self.has_key(key):
            # overwriting an existing entry
            self.storage[key] = value

            # find existing node and move it to end
            node = self.order_list.find_node(key)
            self.order_list.move_to_end(node)
        else:
            # creating a new entry
            self.storage[key] = value
            
            # add new node to the end of the list
            self.order_list.add_to_tail(key)
            
            # if we are at the size limit, remove the oldest item
            if self.length == self.limit:
                # remove the oldest used entry from both the
                # order list and storage dict
                old_key = self.order_list.remove_from_head()
                del self.storage[old_key]
            else:
                # not at the limit, just added the new item
                self.length += 1
