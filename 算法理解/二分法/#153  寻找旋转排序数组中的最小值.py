# __*__coding:utf-8__*__
# @ModuleName: #153  寻找旋转排序数组中的最小值
# @Function: 
# @Author: pl
# @Time: 2020/11/6 0:00

"""
题目：假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组[0,1,2,4,5,6,7] 可能变为[4,5,6,7,0,1,2] 。

请找出其中最小的元素。

示例 1：

输入：nums = [3,4,5,1,2]
输出：1
示例 2：

输入：nums = [4,5,6,7,0,1,2]
输出：0
示例 3：

输入：nums = [1]
输出：1

提示：

1 <= nums.length <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数都是 唯一 的
nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转

"""


def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """


if __name__ == '__main__':
    nums = [1,2,3, 7,7,7,7,7,7,7,7,8,9]
    target = 7
    print(findMin(nums))