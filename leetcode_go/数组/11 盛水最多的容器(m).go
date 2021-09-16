package main

import "fmt"

/*
* 题目：给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0)。
* 找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
*
* 解题思路：双向指针，首尾两个指针不断缩小范围确定的矩形的大小，时间复杂度O(n)
*/

func maxArea(height []int) int {
	tmpMaxArea := 0
	start := 0
	end := len(height) - 1

	for start < end {
		var h int
		if height[start] < height[end] {
			h = height[start]
			start++
		} else {
			h = height[end]
			end--
		}

		area := h * (end - start + 1)
		if area > tmpMaxArea {
			tmpMaxArea = area
		}
	}
	return tmpMaxArea

}

func main() {
	height := []int{1,8,6,2,5,4,8,3,7}
	fmt.Println(maxArea(height))
}