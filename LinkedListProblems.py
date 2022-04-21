
#Homework 1
def interweavelinkedList(head):
    count = 0
    node = head

    while node.next != None:
        count += 1
        node = node.next
    first_half_count = count // 2

    node = head
    first_count = 0
    while node.next != None and first_count != first_half_count + 1:
        node = node.next
        first_count += 1

    fNode = head
    second_count = 0

    while fNode.next != None and second_count != first_half_count:
        fNode = fNode.next
        second_count += 1
    fNode.next = None

    return weaveTwoArr(head, node)
# O(n)


def weaveTwoArr(head1, head2):
    head = head1
    node = head2
    node1 = head1.next
    node2 = head2.next
    head.next = node
    while node1 != None and node2 != None:
        current_node_1 = node1
        current_node_2 = node2
    
        node1 = node1.next
        node2 = node2.next
    
        node.next = current_node_1
        node.next.next = current_node_2
    
        node = node.next.next

    while node1 != None:
        node.next = node1
        node = node.next
        node1 = node1.next
    
    while node2 != None:
        node.next = node2
        node = node.next
        node2 = node2.next
    
    return head

# Homework 2
def rotateArr(head, k):
    for j in range(k):
        node = head.next
        new_head = head.next
        head.next = None
        while node.next != None:
            node = node.next
            node.next = head
            head = new_head
    return new_head

# Homework 3
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


# Homework 4
def valueFromLastNode(head, k):
    # O(1)
    node = head
    # O(1)
    seen_list =[]
    # O(1)
    count = 0
    # O(n)
    while node.next != None:
        # O(1)
        seen_list.append(node.value)
        # O(1)
        node = node.next
        # O(1)
        i = len(seen_list) - 1
    # O(n)
    while i != 0:
    # O(1)
        if i == count:
            # O(1)
            return seen_list[i]
        else :
            # O(1)
            count += 1
            # O(1)
            i -= 1
