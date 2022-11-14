#TC:O(n)
#SC:O(1)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        cycle = False
        
        if not head:
            return head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                cycle = True
                break
        
        if cycle == False:
            return None
        
        slow = head
        
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        
        return slow