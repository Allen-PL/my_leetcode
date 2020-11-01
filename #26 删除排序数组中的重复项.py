# __*__coding:utf-8__*__
# @ModuleName: #26 删除排序数组中的重复项
# @Function: 
# @Author: pl
# @Time: 2020/11/1 22:42

"""
题目：给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


示例1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。

"""


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return []
    middle = nums[0]
    a = 0
    for index, num in enumerate(nums[1:]):
        index = index - a
        print(a)
        if num == middle:
            nums.pop(index)
            a += 1
        else:
            middle = num
    return nums


if __name__ == '__main__':
    nums = [1, 2]
    print(removeDuplicates(nums))