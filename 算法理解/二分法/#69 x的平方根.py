# __*__coding:utf-8__*__
# @ModuleName: #69 x
# @Function: 
# @Author: pl
# @Time: 2020/11/4 23:14
"""
题目：实现int sqrt(int x)函数。

计算并返回x的平方根，其中x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
    由于返回类型是整数，小数部分将被舍去。

"""

# todo 有点意思
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    left = 0
    right = x
    while left < right:
        # mid = (left + right) // 2  # 中值取得是左边的（因为舍掉小数部分所以不符合题意）
        mid = (left + right + 1) >> 1  # 中值取右边的
        square = mid * mid
        if square > x:
            right = mid - 1
        else:
            left = mid
    return left


if __name__ == '__main__':
    num = 8785757
    print(mySqrt(num))