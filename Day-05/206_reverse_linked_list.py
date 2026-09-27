class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


prev = None
current = head

while current:

    nextNode = current.next
    current.next = prev

    prev = current
    current = nextNode


# Print reversed linked list
# current = prev

# while current:
#     print(current.val, end=" ")
#     current = current.next


# # Leetcode Problem 206: Reverse Linked List

# class Solution:
#     def reverseList(self, head):

#         prev = None
#         current = head

#         while current:

#             nextNode = current.next
#             current.next = prev

#             prev = current
#             current = nextNode

#         return prev