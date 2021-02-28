# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):

        pointer1 = head
        pointer2 = head
        count = 0
        while pointer1:
            count += 1

            pointer1 = pointer1.next

            if count > n + 1:
                pointer2 = pointer2.next
        if pointer2 == head:
            if not head.next:
                return None
            if count == n:
                return pointer2.next
        pointer2.next = pointer2.next.next
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def flashback(head):


    if head.next:
        flashback(head.next)

    print(head.val)

flashback(head)
