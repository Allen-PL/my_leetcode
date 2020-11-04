# __*__coding:utf-8__*__
# @ModuleName: #34 在排序数组中查找元素的第一个和最后一个元素
# @Function: 
# @Author: pl
# @Time: 2020/11/4 23:51

"""
题目：给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是O(log n) 级别。

如果数组中不存在目标值，返回[-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

"""


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """


if __name__ == '__main__':
    nums = [-1]
    target = -1
    print(searchRange(nums, target))