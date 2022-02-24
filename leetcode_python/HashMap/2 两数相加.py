# __*__coding:utf-8__*__
# @ModuleName: 两数相加
# @Function: 
# @Author: pl
# @Time: 2020/10/28 16:51
"""
题目大意：给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

输入：l1 = [0], l2 = [0]
输出：[0]
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]


解题思路：
链接：

"""


class ListNode:

    def __init__(self, val, next=0):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r = re
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        if (carry > 0):
            r.next = ListNode(1)
        return re.next


# 列表转链表
def lstToListNode(lst):
    # 创建一个空节点，其实算是一个头节点
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in lst:
        ptr.next = ListNode(number)
        ptr = ptr.next
    # 这个节点的next就是真正的头结点
    ptr = dummyRoot.next
    return ptr


# 链表转列表
def listNodeToLst(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print(Solution().addTwoNumbers(l1, l2))
