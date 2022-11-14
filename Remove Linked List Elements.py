#TC: O(n)
#SC: O(1)
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head
        prev = dummyhead
        curr = dummyhead.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next #previous is there in the same position but changing the next of the previous
                curr = curr.next
            else:
                prev = curr
                curr = curr.next            
        return dummyhead.next
        