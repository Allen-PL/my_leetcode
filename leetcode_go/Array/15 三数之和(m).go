package main

import (
	"fmt"
	"sort"
)

/*
* 题目：给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
* 注意：答案中不可以包含重复的三元组。
*
* 解题思路：排序 + 双指针，将时间复杂度控制在O(n),
*
*/

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	result, start, end, index, addNum, length := make([][]int, 0), 0, 0, 0, 0, len(nums)
	// 这里是这样子考虑的，确定左边的最小值，和右边的最大值，然后再最小值和最大值之间循环的，直到找到条件的那个数字，然后双指针向里面收缩,每次循环一遍
	for index = 1; index < length - 1; index++ {
		// 因为index是从小往大开始的，多个相同的数据保证始终相同的最后两个数字
		start, end = 0, length - 1
		if index > 1 && nums[index] == nums[index-1] {
			start = index - 1
		}
		for start < index && end > index {
			// 控制不会出现重复的数组(因为面的相同的数据匹配到了就不能重复pass，就算前面的数据没有匹配到也是跳过，所以这样控制很合理)
			if start > 0 && nums[start] == nums[start - 1] {
				start++
				continue
			}
			// 控制不会出现重复的数组
			if end < length - 1 && nums[end] == nums[end + 1] {
				end--
				continue
			}
			addNum = nums[start] + nums[end] + nums[index]
			if addNum == 0 {
				result = append(result, []int{nums[start], nums[index], nums[end]})
				start++
				end--
			} else if addNum > 0 {
				end--
			} else {
				start++
			}
		}
	}
	return result
}


func main() {
	//nums := []int{1, -1, 3, 0, 5, 6, 2, -9, -11}
	nums := []int{0, 0, 0, 0}
	fmt.Println(threeSum(nums))
}
