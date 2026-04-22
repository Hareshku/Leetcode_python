from typing import Optional

# Define ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, p = None, head
        while p:
            q = p.next
            p.next = pre
            pre = p
            p = q
        return pre

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
node_list = ListNode(1,
             ListNode(2,
             ListNode(3,
             ListNode(4,
             ListNode(5)))))

obj = Solution()
result = obj.reverseList(node_list)

# Print result
while result:
    print(result.val, end=" -> ")
    result = result.next
print("NULL")