package main

import "fmt"

/*
* 题目：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
* 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。
*
* 解题思路：借助map，也就是字典，如果找到了就返回，否则就将值存进map中，只需要遍历一遍就能找到，时间复杂度O(n)
*/

func ToSum(list []int, target int) []int {
	dict := make(map[int]int)
	for i := 0; i < len(list); i++ {
		another := target - list[i]
		if _, ok := dict[another]; ok {
			return []int{dict[another], i}
		}
		dict[list[i]] = i
	}
	return nil
}

func main() {
	list := []int{1,2,3,4,5}
	target := 9
	result := ToSum(list, target)
	fmt.Println(result)
}