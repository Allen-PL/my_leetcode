# __*__coding:utf-8__*__
# @ModuleName: 
# @Function: 
# @Author: pl
# @Time: 2022/2/23 11:59
"""
题目大意：给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
输入：head = [1,2]
输出：[2,1]
输入：head = []
输出：[]

解题思路：使用一个tmp变量作为中间传递值，将前一个节点的值给pre，后一个节点的值继续赋给cur，直到cur到链表的末尾为None停止
链接：https://leetcode-cn.com/problems/reverse-linked-list/solution/shi-pin-jiang-jie-die-dai-he-di-gui-hen-hswxy/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 迭代实现
    # def reverseList(self, head: ListNode) -> ListNode:
    #     pre = None
    #     cur = head
    #     while cur:
    #         # 将下一个节点赋给中间变量
    #         tmp = cur.next
    #         # 这个节点逆向，指向前面一个节点
    #         cur.next = pre
    #         # 交换位置，重复操作
    #         pre = cur
    #         cur = tmp
    #     return pre

    # 递归实现
    def reverseList(self, head: ListNode) -> ListNode:
        # 跳出递归，此时head是链表末尾最后一个值
        if head.next is None:
            print(head.val)
            return head
        # 自己调用自己，直到满足上方的条件，走到链表的末尾，最里面的函数返回上面head，链表末尾的值，
        p = self.reverseList(head.next)  # 最开始 p = reverseList(reverseList(reverseList(3)))
        # 后续函数的执行都是走这里，开始回溯
        head.next.next = head  #
        head.next = None

        return p


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


def main(line):
    head = lstToListNode(line)
    ret = Solution().reverseList(head)
    out = listNodeToLst(ret)

    print(out)


if __name__ == '__main__':
    line = [1, 2, 3]
    main(line)

