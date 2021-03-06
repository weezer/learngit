# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        ptr = head
        carry = 0
        while True:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            ptr.val = carry % 10
            carry /= 10

            if l1 != None or l2 != None or carry != 0:
                ptr.next = ListNode(0)
                ptr = ptr.next
            else:
                break
        return head

if __name__ == "__main__":
    answer = Solution()
    l1 = ListNode(2)
    l12 = ListNode(4)
    l13 = ListNode(3)
    l1.next=l12
    l12.next=l13
    l2 = ListNode(5)
    l22 = ListNode(6)
    l23 = ListNode(4)
    l2.next=l22
    l22.next=l23
    print answer.addTwoNumbers(l1, l2)

