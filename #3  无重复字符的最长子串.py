# __*__coding:utf-8__*__
# @ModuleName: #3  无重复字符的最长子串
# @Function: 
# @Author: pl
# @Time: 2020/10/29 10:40


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    length = len(s)
    ls = list(s)
    for num in range(length, 0, -1):
        for i in range(length - num):
            s_l = ls[:num]
            if set(s_l) == num:
                return num
    return None




if __name__ == '__main__':
    s = 'kasl'
    lengthOfLongestSubstring(s)