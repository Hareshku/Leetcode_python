# class Solution:
#     def addTwoNumbers(
#         self, l1: Optional[ListNode], l2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         dummy = ListNode()
#         carry, curr = 0, dummy
#         while l1 or l2 or carry:
#             s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
#             carry, val = divmod(s, 10)
#             curr.next = ListNode(val)
#             curr = curr.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return dummy.next


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            s = v1 + v2 + carry

            carry, val = divmod(s, 10)

            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# Helper function to create linked list
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


# Helper to print linked list
def print_list(node):
    while node:
        print(node.val, end="")
        node = node.next
        if node:
            print(" -> ", end="")
    print()


# Test
l1 = build_list([2,4,3])
l2 = build_list([5,6,4])

s = Solution()
result = s.addTwoNumbers(l1, l2)

print_list(result)