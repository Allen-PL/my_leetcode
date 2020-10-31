# __*__coding:utf-8__*__
# @ModuleName: #9回文数
# @Function: 
# @Author: pl
# @Time: 2020/10/31 23:46

"""
题目：判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    y = x
    b_list = []
    result = 0
    if x < 0:
        return False
    else:
        while True:
            b_list.append(x % 10)
            x = x // 10
            if x == 0:
                break
        print(b_list)
        for index, num in enumerate(b_list[::-1]):
            print(index, num, result)
            result += num * 10 ** index
        if result == y or y == 0:
            return True
        return False


if __name__ == '__main__':
    x = 121
    print(isPalindrome(x))