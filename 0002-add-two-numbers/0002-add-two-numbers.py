class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy

        carry = 0

        while l1 or l2 or carry:

            if l1:
                num1 = l1.val
            else:
                num1 = 0

            if l2:
                num2 = l2.val
            else:
                num2 = 0

            total = num1 + num2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next