# __*__coding:utf-8__*__
# @ModuleName: #1 两数之和
# @Function: 
# @Author: pl
# @Time: 2020/10/28 15:14
from typing import Dict


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap: Dict = dict()
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num], index]
        hashmap.setdefault(num, index)
    return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    print(twoSum(nums, 9))

'''
题目：给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

时间复杂度：O(n)
'''
