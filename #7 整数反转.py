# __*__coding:utf-8__*__
# @ModuleName: #7 整数反转
# @Function: 
# @Author: pl
# @Time: 2020/10/30 11:00

"""
题目：给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
tip: 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    s_x = str(abs(x))
    r_s_x = ''.join(list(s_x)[::-1])
    r_x = int(r_s_x)
    if r_x > (2**31 - 1) or r_x < -2**31:
        return 0
    if x < 0:
        return 0 - r_x
    return r_x


if __name__ == '__main__':
    x = -1534236469
    print(reverse(x))