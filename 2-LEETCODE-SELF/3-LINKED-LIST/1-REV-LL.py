class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next=None
        prev=None
        current=head
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next
        return prev
        