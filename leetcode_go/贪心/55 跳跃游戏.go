package main

import "fmt"

/*
题目大意：给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

解题思路：

*/

func canJump(nums []int) bool {

	for index, num  := range nums {
		if num == 0 {
			// 开始等于0，gg
			if index == 0 {
				if len(nums) == 1 {
					return true
				}
				return false
			}

			i := 1
			for index - 1  >= 0 {
				if nums[index - 1] < i {
					if index - 1 == 0 {
						return false
					}
				}
				if nums[index - 1] == 0 {
					if index == len(nums) {
						return true
					}
				}
				i++
				index--
			}

		}
	}

	return true
}


func main() {
	//nums := []int{2,3,1,1,4}
	nums := []int{3,2,1,0,4}
	//nums := []int{2,0,0}
	fmt.Println(canJump(nums))
}
