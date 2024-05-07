# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        value = ""

        a = head
        while a != None:
            value += str(a.val)
            a = a.next

        result = str(int(value)*2)
        result = result[::-1]

        head = None
        for x in result:
            head = ListNode(int(x), next=head)

        return head