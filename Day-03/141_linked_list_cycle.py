class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Linked List: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2


slow = node1
fast = node1

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        print(True)
        break
else:
    print(False)




# Leetcode Problem 141: Linked List Cycle


# class Solution:
#     def hasCycle(self, head):

#         slow = head
#         fast = head

#         while fast and fast.next:

#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 return True

#         return False