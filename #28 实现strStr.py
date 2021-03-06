# __*__coding:utf-8__*__
# @ModuleName: #28 实现strStr
# @Function: 
# @Author: pl
# @Time: 2020/11/1 22:56

"""
题目：实现strStr()函数。

给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

"""


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    n_l = list(needle)
    h_l = list(haystack)
    for index, s in enumerate(h_l):
        if n_l[0] == s:
            if haystack[index:index+len(n_l)] == needle:
                return index
    return -1


if __name__ == '__main__':
    haystack = "heldaalo"
    needle = "dasa"
    print(strStr(haystack, needle))