class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        t = slow.next
        slow.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(t)
        
        dummy = ListNode()
        cur = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 or l2
        return dummy.next


# helper functions
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# test
head = build_list([4,2,1,3])
obj = Solution()
sorted_head = obj.sortList(head)
print_list(sorted_head)