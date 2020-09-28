"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    """
    The left subtree of a node contains only nodes with values lesser than the node’s value.
    The right subtree of a node contains only nodes with values greater than or equal to the node’s value.
    The left and right subtree each must also be a binary search tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new nodes value is less than the current nodes value
        if value < self.value:
            # if there is no left child already here
            if not self.left:
                # add the new node to the left
                new_node = BSTNode(value)
                self.left = new_node
                # create a BSTNode and encapsulate the value in it then set it to the left
            else:
            # otherwise call insert on the left node
                self.left.insert(value)
        else:
        # otherwise (the new nodes value is greaterthan or equal to the current node value)
            if not self.right:
            # if there is no right child already here
                new_node = BSTNode(value)
                self.right = new_node
                # add the new node to the right
                # create a BSTNode and encapsulate the value in it then set it to the right
            else:
            # otherwise call insert on the right node
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value of the current node matches the target
            # return True
        if self.value == target:
            return True

        # check if the target is less than the current nodes value
        if target < self.value:
            # if there is no left child already here
            if not self.left:
                return False
            else:
                # return a call of contains on the left child passing in the target value
                return self.left.contains(target)
        else:
        # otherwise (the target is greater than the current nodes value)
            # if there is no right child already here
            if not self.right:
                return False
            else:
                # return a call of contains on the right child passing in the target value
                return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        # check for an empty tree
            # return None
        if not self:
            return None

        # ----------------------------------------------
        # recursive approach
        # check if there is no node to the right
            # return the nodes value
        # return a call to get max on the right child
        if not self.right:
            return self.value
        else:
            return self.right.get_max()


        # -----------------------------------------------

        # iterative aproach

        # initialise the max value

        # get a ref to the current node

        # loop while there is still a current node
            # if the current value is greater than the max value, update the max value
            # move on to the next right node
        
        # return the max value
        # max_val = 0
        # current = self
        # while current:
        #     if current.value > max_val:
        #         max_val = current.value
        #         current = current.right

        # return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function passing in the current nodes value

        # if there is a node to the left
            # call the function on the left value
        
        # if there is a node to the right
            # call the function on the right node
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

  