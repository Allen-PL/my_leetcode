package main

import "fmt"

/*
题目大意：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

一句话点醒梦中人：n阶楼梯，每次只能走1或2，那么dp[n] = dp[n-1] + dp[n-2]。走最后一步到n阶楼梯，那么最后一步只能是1或者2,那么将这两种走法相加就是n最终的走法了.
使用递归的写法肯定在时间复杂度商是通过不了的，那么知道他的原理和规律就可以从底层往上走去实现算法
*/

func climbStairs(n int) int {
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	a := 1
	b := 2
	for n >= 3 {
		mid := a + b
		a = b
		b = mid
		n--
	}
	return b
}

func main() {
	n := 50
	fmt.Println(climbStairs(n))
}
