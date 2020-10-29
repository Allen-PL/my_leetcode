# __*__coding:utf-8__*__
# @ModuleName: #2 两数相加
# @Function: 
# @Author: pl
# @Time: 2020/10/28 16:51
from typing import List


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if len(l1) > len(l2):
        length = len(l1)
        l2 += [0]*(length - len(l2))
    else:
        length = len(l2)
        l1 += [0]*(length - len(l1))
    new_list = zip(l1, l2)
    # print(list(new_list))
    # for index, tup in enumerate(new_list):
    #     left = index ** 10 * (tup[0] + tup[1])
    result: List = []
    a = 0
    for tup in list(new_list):
        if tup[0] + tup[1] > 9:
            result.append(tup[0] + tup[1] - 10)
            a = 1
        else:
            result.append(tup[0] + tup[1] + a)
            a -= 1
    num1 = [10 ** index * num for index, num in enumerate(l1)]
    num2 = [10 ** index * num for index, num in enumerate(l2)]
    num3 = [10 ** index * num for index, num in enumerate(result)]
    left = right = 0
    for i in num1 + num2:
        left += i
    for i in num3:
        right += i
    if left == right:
        return result
    else:
        return None


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print(addTwoNumbers(l1, l2))