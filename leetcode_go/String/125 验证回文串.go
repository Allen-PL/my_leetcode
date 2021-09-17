package main

import "strings"

/*
题目说明：给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

解题思路：前后同步找，注意界限，判断失败往前走一格，往后退一格
*/

// 判断 c 是否是字符或者数字
func isChar(c byte) bool {
	if ('a' <= c && c <= 'z') || ('0' <= c && c <= '9') {
		return true
	}
	return false
}


func isPalindrome(s string) bool {
	len_s := len(s)
	tmp_s := strings.ToLower(s)
	i := 0
	j := len_s - 1
	if (len_s == 0) {
		return true
	}
	for (i < j) {
		for i < j && !isChar(tmp_s[i]) {
			i++
		}
		for i < j && !isChar(tmp_s[j]) {
			j--
		}
		if (tmp_s[i] != tmp_s[j]) {
			return false
		}
		i++
		j--
	}
	return true
}

func main() {
	s := "race a car"
	println(isPalindrome(s))

}