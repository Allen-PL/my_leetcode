# __*__coding:utf-8__*__
# @ModuleName: #287 寻找重复数
# @Function: 
# @Author: pl
# @Time: 2020/11/6 22:59

"""
题目:给定一个包含n + 1 个整数的数组nums，其数字都在 1 到 n之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

"""
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    left = 1
    right = len(nums) - 1
    while left < right:
        mid = (left + right + 1) >> 1

        cut = 0
        for num in nums:
            if num <= mid:
                cut += 1

        if cut > mid:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    nums = [1, 2, 3, 7,8, 9]
    print(lengthOfLIS(nums))