package main

import "fmt"

/*
* 题目：给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
* 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
* 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
*
*
*/

func removeElement(nums []int, val int) int {

	for index, num := range(nums) {
		if num == val {
			nums = append(nums[:index], nums[index+1:]...)
		}
	}
	return len(nums)
}


func main() {
	nums := []int{3,5,2,3}
	fmt.Println(removeElement(nums, 3))
}