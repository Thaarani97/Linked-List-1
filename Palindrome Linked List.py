#TC:O(n)
#SC:O(1)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.findMid(head)
        midnext = mid.next
        mid.next = None
        p1 = self.reverse(midnext)
        p2 = head
        
        while p1:
            if p1.val==p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        return True      
    
    def findMid(self,head):
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverse(self,head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev