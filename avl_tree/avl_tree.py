"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        # check height of left subtree
        lefth = -1
        if self.node.left:
            lefth = self.node.left.update_height()
        # check height of right subtree
        righth = -1
        if self.node.right:
            righth = self.node.right.update_height()
        # save highest one, add one to count self
        self.height = (lefth if lefth > righth else righth) + 1
        # return it for recursion to work
        return self.height

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        # count number of nodes on left side
        n_left = 0
        if self.node.left:
            n_left = self.node.left.count_nodes()
        # count number of nodes on right side
        n_right = 0
        if self.node.right:
            n_right = self.node.right.count_nodes()
        # difference is the balance factor
        self.balance = n_left - n_right
    
    """
    Counts the number of nodes in this tree (recursive)
    """
    def count_nodes(self):
        # count nodes right left
        n_left = 0
        if self.node.left:
            n_left = self.node.left.count_nodes()
        # count nodes on the right
        n_right = 0
        if self.node.right:
            n_right = self.node.right.count_nodes()
        # return sum, add 1 for self
        return n_left + n_right + 1

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent.
    """
    def left_rotate(self):
        # This first solution is how I'd like to do it, but the test requires
        # that this AVLTree object remains the root

        # # set aside the right child
        # child = self.node.right
        # # if that child has a left child, make it the right subtree of this node
        # if child.node.left:
        #     self.node.right = child.node.left
        # # set this node as the old child's left child
        # child.node.left = self

        # This second solution matches the test by creating a new AVLTree
        # instance, moving values around, and removing an unneeded instance

        # Create a new tree node, copy this key into it, preserve left subtree
        temp = self.node.left
        self.node.left = AVLTree(Node(self.node.key))
        self.node.left.node.left = temp

        # If right child had a left subtree, move it to the new node's right
        if self.node.right.node.left:
            self.node.left.node.right = self.node.right.node.left
        
        # Copy right child's value to here (root)
        self.node.key = self.node.right.node.key

        # Set this node's right subtree to the old right child's right subtree
        self.node.right = self.node.right.node.right

        # The old node.right no longer has any references to it
        

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        # child = self.node.left
        # if child.node.right:
        #     self.node.left = child.node.right
        # child.node.right = self

        # Create a new tree node, copy this key into it, preserve right subtree
        temp = self.node.right
        self.node.right = AVLTree(Node(self.node.key))
        self.node.right.node.right = temp

        # If left child had a right subtree, move it to the new node's left
        if self.node.left.node.right:
            self.node.right.node.left = self.node.left.node.right
        
        # Copy left child's value to here (root)
        self.node.key = self.node.left.node.key

        # Set this node's left subtree to the old left child's left subtree
        self.node.left = self.node.left.node.left

        # The old node.left no longer has any references to it

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        pass
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        pass
