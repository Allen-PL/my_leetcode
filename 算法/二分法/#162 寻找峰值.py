# __*__coding:utf-8__*__
# @ModuleName: #162 寻找峰值
# @Function: 
# @Author: pl
# @Time: 2020/11/5 23:13
"""
题目：峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
    或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是(logN)时间复杂度的。
"""


def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) >> 1 + left
        if nums[mid] < nums[mid - 1] and mid > 0:
            right = mid
        elif nums[mid] < nums[mid + 1] and mid < len(nums):
            left = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    nums = [1,2,3, 7,7,7,7,7,7,7,7,8,9]
    target = 7
    print(findPeakElement(nums))