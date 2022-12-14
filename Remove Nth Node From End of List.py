#TC:    O(n)
#SC:    O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        cnt = 0
        
        while (cnt<n):
            cnt+=1
            p1 = p1.next
        
        if (p1 == None):
            return head.next
               
        while (p1.next!=None):
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next
        return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        p2 = dummy
        while n+1:
            p1 = p1.next
            n-=1
       
        while p1:
            p1=p1.next
            p2=p2.next
            
        p2.next = p2.next.next
        
        return dummy.next