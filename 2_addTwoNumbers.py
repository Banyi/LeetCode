'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


def reverse_node_val(ListNode):
    s_val = ''
    while ListNode is not None:
        s_val += str(ListNode.val)
        ListNode = ListNode.next
    return int(s_val[::-1])
    

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = str(reverse_node_val(l1) + reverse_node_val(l2))[::-1]
        head = new_node = ListNode(val[0])
        for i in range(1, len(val)):
            new_node.next = ListNode(val[i])
            new_node = new_node.next
        return head
