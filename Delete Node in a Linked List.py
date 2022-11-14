#TC:O(n)
#SC:O(1)

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextnode = node.next
        node.val = nextnode.val
        node.next = nextnode.next