class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree1Root = TreeNode(2)
tree1Root.left = TreeNode(1)
tree1Root.right = TreeNode(3)

tree2Root = TreeNode(8)
tree2Root.left = TreeNode(7)
tree2Root.left.left = TreeNode(6)
tree2Root.right = TreeNode(9)
tree2Root.right.right = TreeNode(10)

def printTree(root):
    print(root.value)
    horizNotNoneCnt = 0
    if root.left != None:
        horizNotNoneCnt += 1
    if root.right != None:
        horizNotNoneCnt += 1
    
    horiz = [root.left, root.right]

    while horizNotNoneCnt > 0:
        horizNotNoneCnt = 0
        front = []
        s = ""
        for node in horiz:
            if node:
                s += str(node.value)
                horizNotNoneCnt += 1
                front.append(node.left)
                front.append(node.right)
            else:
                s += "-"
                front.append(None)
                front.append(None)
            s += ","
        print(s)

        horiz = front



# Homework 1
# Given a binary search tree, reverse the order of its values by modifying the nodes’ links.
def reverseOrder(root):
    if root != None:
        a = reverseOrder(root.left)
        b = reverseOrder(root.right)
    
        root.left = b
        root.right = a
    
    return(root)

# Homework 2 (6)
# Given a binary search tree containing integers and a target integer, 
# come up with an efficient way to locate two nodes in the tree whose sum is equal to the target value.
def find_all_nodes(root, unique_nodes):
    if root.left:
        find_all_nodes(root.left)
    if root.right:
        find_all_nodes(root.right)
    
    unique_nodes.add(root.val)

def find_nodes_add_to_target(root, target):
    unique_nodes = set()
    if not root:
        return None
    find_all_nodes(root, unique_nodes)
    for val in unique_nodes:
        if target - val in unique_nodes:
            return(val, target - val)
    return None

# Homework 3 (7)
# Given a binary tree containing numbers, find the maximum sum path 
# (the path that has the largest sum of node values). The path may start and end at any node in the tree.
def max_sum_path(root, max_vals):
    if not root:
        return 0
    left_path = max_sum_path(root.left)
    right_path = max_sum_path(root.right)
    max_vals.append(max(root.val, root.val + left_path, root.val + right_path, root.val + left_path + right_path))
    return max(root.val, root.val + left_path, root.val + right_path, root.val + left_path + right_path)

def max_path(root):
    max_vals = []
    max_sum_path(root, max_vals)
    return max(max_vals)



# Homework 4 (8)
# Let’s say a binary tree is "super balanced" if the difference 
# between the depths of all pairs of leaf nodes is at most one. 
# Write a function to check if a binary tree is "super balanced".
def find_depth(root, current_depth, depth_list):
    if root.left:
        find_depth(root.left, current_depth + 1, depth_list)
    if root.right:
        find_depth(root.right, current_depth + 1, depth_list)
    if not root.left and not root.right:
        depth_list.append(current_depth)

def is_super_balanced(root):
    depth_list = []
    find_depth(root, 0, depth_list)
    return max(depth_list) - min(depth_list) <= 1


# Homework 5 (1)
# Given a binary tree, check whether it is a valid binary search tree (values in order).
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

# Homework 6 (2)
# Given a binary search tree, convert it into a sorted doubly-linked 
# list by modifying the original tree nodes (do not create new nodes).
def traverse_tree(root, ordered_list):
    if root:
        traverse_tree(root.left)
        ordered_list.append(root)
        traverse_tree(root.right)

def convert_tree_to_list(root):
    ordered_list = []
    traverse_tree(root, ordered_list)
    for i in range(len(ordered_list)):
        if i == 0:
            ordered_list[i].left = None
        else :
            ordered_list[i].left = ordered_list[i - 1]
        if i == len(ordered_list) - 1:
            ordered_list[i].right == None
        else :
            ordered_list[i].right = ordered_list[i + 1]