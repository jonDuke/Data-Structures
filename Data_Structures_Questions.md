Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?

  - O(n)
  - In the worst case, the list needs to allocate more memory and ends up with the "doubling problem"

2. What is the runtime complexity of `push` using a linked list?

  - O(1)
  - Adding to either end of a linked list is O(1)

3. What is the runtime complexity of `pop` using a list?

  - O(1)
  - Removing from a list is O(1)

4. What is the runtime complexity of `pop` using a linked list?

  - O(1)
  - Removing from a linked list is O(1)

5. What is the runtime complexity of `len` using a list?

  - O(1)
  - Getting the length of a list is O(1)

6. What is the runtime complexity of `len` using a linked list?

  - O(n)
  - Getting the length of a linked list requires iterating through and counting each node.

## Queue

1. What is the runtime complexity of `enqueue` using a list?

  - O(n)  (worst case, when the list has to allocate more memory)
  - Same as before, this is just adding to a list.
  - If you insert at index 0 and treat index -1 as the front of the queue, then this would always be O(n) since the list would have to shift each entry in memory.

2. What is the runtime complexity of `enqueue` using a linked list?

  - O(1)
  - Same as before, this just adds a single node to the linked list.

3. What is the runtime complexity of `dequeue` using a list?

  - O(n) or O(1)
  - If index -1 is the front of the queue, then this is O(1) since you would just remove the last item of the list.
  - If index 0 is the front of the queue, then each item in memory would need to be shifted.

4. What is the runtime complexity of `dequeue` using a linked list?

  - O(1)
  - Again, just removing one node.  Works the same in either direction.

5. What is the runtime complexity of `len` using a list?

  - O(1)
  - Same as with stack

6. What is the runtime complexity of `len` using a linked list?

  - O(n)
  - Same as with stack

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

4. What is the runtime complexity of `for_each`?
    
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
