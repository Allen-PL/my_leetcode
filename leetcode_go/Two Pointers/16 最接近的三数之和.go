package main

import (
	"fmt"
	"math"
	"sort"
)

/*
题目大意：给定一个包括n个整数的数组nums和一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

*/
func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	start := 0
	end := len(nums) - 1
	tmp_abs_min := nums[end] - nums[start]
	middle_num := 0
	for end - start > 2{
		tmp_num := nums[start] + nums[end] - target
		if tmp_num < tmp_abs_min {
			for num, _ := range nums[start + 1: end - 1] {
				tmp := int(math.Abs(float64(num - tmp_num)))
				if tmp < tmp_abs_min {
					tmp_abs_min = tmp
					middle_num = num
				}
			}
			if tmp_abs_min - nums[start] > tmp_abs_min - nums[end] {
				end--
			} else {
				start++
			}
		}
	}
	return nums[start] + nums[end] + middle_num
}


func main() {
	nums := []int{-1,2,1,-4}
	target := 1
	fmt.Println(threeSumClosest(nums, target))
}