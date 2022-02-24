# __*__coding:utf-8__*__
# @ModuleName: #3  无重复字符的最长子串
# @Function: 
# @Author: pl
# @Time: 2020/10/29 10:40

"""
题目大意：给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。

解题思路：设置双指针，一个指向窗口的左端（头指针head），一个指向窗口的右端的下一个元素（尾指针tail），则窗口大小为tail-head。
首先，不断移动尾指针，直到尾指针指向的元素在当前窗口中已存在；
然后，找到该元素在窗口中的位置，并将头指针指向该位置的下一个位置。
链接：
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        L = len(s)
        if L < 2:
            return L
        # 头尾指针
        head = 0
        tail = 1
        # 滑动窗口，保证不会出现重复的字符串
        cnt = 1
        while tail < L:
            # 第一步：尾指针不断后移，直到尾指针指向的字符串在滑动窗口中出现
            while tail < L and s[tail] not in s[head: tail]:
                tail += 1
            cnt = max(cnt, tail - head)
            if tail != L:
                # 第二步：将头指针移动到尾指针的下一个字符串
                head += s[head: tail].index(s[tail]) + 1
        return cnt


if __name__ == '__main__':
    s = 's'
    print(Solution().lengthOfLongestSubstring(s))
