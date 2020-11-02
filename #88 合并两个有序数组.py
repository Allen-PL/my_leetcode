# __*__coding:utf-8__*__
# @ModuleName: #88 合并两个有序数组
# @Function: 
# @Author: pl
# @Time: 2020/11/2 22:37

"""
题目：给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。

说明：
初始化nums1 和 nums2 的元素数量分别为m 和 n 。
你可以假设nums1有足够的空间（空间大小大于或等于m + n）来保存 nums2 中的元素。

示例：
输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出：[1,2,2,3,5,6]
"""


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    index = 0
    count = n
    for num1 in nums1[-n-1::-1]:
        # print(num1)
        print(nums1)
        if not count:
            break
        for num2 in nums2[::-1]:
            print(nums2)
            if num2 > num1:
                index += 1
                nums1[-index] = nums2[-index]
                count -= 1
            else:
                index += 1
                nums1[-index] = num1

                break

    return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge(nums1, m, nums2, n))