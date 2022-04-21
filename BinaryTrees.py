# Given a binary search tree, reverse the order of its values by modifying the nodes’ links.

# Homework 1
def reverseOrder(root):
    if root != None:
        a = reverseOrder(root.left)
        b = reverseOrder(root.right)
    
        root.left = b
        root.right = a
    
    return(root)


# Homework 5
def isBalanced(root):
    # check to see if there is a tree
    if root == None:
        return False

    # check to see if the root .left is greater than the root
    if root.left != None and root.left.value > root.value:
        return False

    # check to see if the right is less than the root
    if root.right != None and root.right.value < root.value:
        return False

    # check to see the left and the right are binary search trees return          false if not
    if (isBalanced(root.left) == False or isBalanced(root.right) == False):
        return False

    # return true if all conditions are met
    return True

