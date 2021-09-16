# __*__coding:utf-8__*__
# @ModuleName: #14 最长公共前缀
# @Function: 
# @Author: pl
# @Time: 2020/11/1 12:53

"""
题目：编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。
"""


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    result = ''
    flag = False
    m_s = len(strs[0])
    s_n = 0
    for index, shortest_s in enumerate(strs):
        if len(shortest_s) < m_s:
            m_s = len(shortest_s)
            s_n = index
    first_s_l = list(strs.pop(s_n))
    for num in range(len(first_s_l)):
        for s in strs:
            s_l = list(s)
            if first_s_l[num] != s_l[num]:
                flag = True
                break
        if not flag:
            result += first_s_l[num]
    return result


if __name__ == '__main__':
    strs = ['flower', "flow", "flight"]
    print(longestCommonPrefix(strs))