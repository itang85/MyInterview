# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = num2 = ''
        while l1 or l2:
            if l1:
                num1 = str(l1.val) + num1
                l1 = l1.next
            if l2:
                num2 = str(l2.val) + num2
                l2 = l2.next
        l_sum = int(num1) + int(num2)
        cur = None
        for num in str(l_sum):
            cur = ListNode(int(num), cur)

        return cur
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

l1 = node1
node1.next = node2
node2.next = node3

l2 = node4
node4.next = node5

solu = Solution()
print(solu.addTwoNumbers(l1, l2))
