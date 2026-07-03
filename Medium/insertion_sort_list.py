class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))

        curr = head

        while curr:
            nxt = curr.next

            # Find insertion position
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            curr = nxt

        return dummy.next