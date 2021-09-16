# __*__coding:utf-8__*__
# @ModuleName: #5 最长回文子串
# @Function: 
# @Author: pl
# @Time: 2020/10/29 16:18

"""
题目：给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    length = len(s)
    l_s = list(s)
    num = 0
    if length in [1, 2]:
        return ''.join(list(s)[0])
    while length > 1:
        median = length // 2
        l_s.insert(0, 1)
        l_s_b = list(s)
        for i in range(num):
            for _ in range(i):
                l_s_b.pop(0)
            a = l_s_b[:length]
            left = a[:median]
            right = a[-median:]
            if left == right[::-1]:
                return ''.join(a)
        num += 1
        length -= 1


if __name__ == '__main__':
    s = "acadeagdfhrrawaergfaw"
    print(longestPalindrome(s))

