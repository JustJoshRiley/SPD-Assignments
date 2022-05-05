# Given an array of k singly-linked lists, each of whose values are in sorted order, 
# combine all nodes (do not create new nodes) into one singly-linked list 
# with all values in order.
def combineLists(arr):
    # O(1)
    i = 0
    # O(n)
    mergedLists = mergeTwoLinkedLists(arr[i], arr[i+1])
    # O(1)
    i = 2
  # O(k) *
    while i <= len(arr) - 1 :
    # O(n)
        mergedLists = mergeTwoLinkedLists(mergedLists, arr[i])
    # O(1)
        i += 1
    # O(1)
    return mergedLists

# 0(n) + O(k * n) -> O(k * n)

def mergeTwoLinkedLists(head1, head2):
    # O(1)
    head = None
    # O(1)
    head.next = None
  # O(1) *
    if head1.value < head2.value:
        # O(1)
        head = head1
        # O(1)
        node1 = head1.next
        # O(1)
        node2 = head2
    else :
        # O(1)
        head = head2
        # O(1)
        node2 = head2.next
        # O(1)
        node1 = head1
    # O(1)
    node = head
  # O(n) *
    while node1.next != None and node2.next != None:
    # O(1)
        if node1.value < node2.value:
            # O(1)
            node.next = node1
            # O(1)
            node1 = node1.next
            # O(1)
            node = node.next
        # O(1)
        else :
            # O(1)
            node.next = node2
            # O(1)
            node2 = node2.next
            # O(1)
            node = node.next
        #O(n)
    while node1.next != None:
        # O(1)
        node.next = node1
        # O(1)
        node1 = node1.next
        # O(1)
        node = node.next
    #O(n)
    while node2.next != None:
        # O(1)
        node.next = node2
        # O(1)
        node2 = node2.next
        # O(1)
        node = node.next

    return head


# Given a binary search tree, convert it into a sorted doubly-linked list by 
# modifying the original tree nodes (do not create new nodes).
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

#Let’s say a binary tree is "super balanced" if the difference between the depths 
# of any two leaf nodes is at most one. Write a function to check if a binary tree is 
# "super balanced".
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