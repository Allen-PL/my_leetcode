package main

import "strings"

/*
题目大意：给定一种规律 pattern和一个字符串str，判断 str 是否遵循相同的规律。
这里的遵循指完全匹配，例如，pattern里的每个字母和字符串str中的每个非空单词之间存在着双向连接的对应规

解题思路：判断pattern和s的长度是否对应，在长度对应的情况下利用map结构将迭代所有的s和对应的pattern存起来，那么往后迭代就要去判断map中是否存在新的对应，同时还要考虑对应关系是否正确（对应管
系就是指pattern有相同的元素，但是对应的s元素不一致，反之，做好这些限定条件就ok了，主要关注的就是界限条件）

*/

func wordPattern(pattern string, s string) bool {
	tmp_map := map[string]byte{}
	i := 0
	if len(pattern) != len(strings.Split(s, " ")) {
		return false
	}
	for index, element := range strings.Split(s, " ")  {
		is_exist, ok := tmp_map[element]
		tmp_count := 0
		// 键值存在
		if ok {
			if pattern[index] != is_exist {
				return false
			}
			// 考虑s和pattern自己组的元素是否对应
			for key, value := range tmp_map {
				// 与tmp_map中value比较
				if  pattern[index] == value {
					tmp_count++
				}
				// 与tmp_map中key比较
				if element == key {
					tmp_count++
				}
			}
			// 不对应，count的值就是基数，反之就是偶数
			if tmp_count % 2 == 1  {
				return false
			}
			tmp_count = 0

			tmp_map[element] = pattern[index]
			continue
		} else {
			// map中不存在，还得考虑键-值是否存在map中，存在了不就表示不符合规律么
			for _, value := range tmp_map {
				// 与tmp_map中value比较
				if  pattern[index] == value {
					return false
				}
			}
			tmp_map[element] = pattern[index]
			i++
			continue
		}
	}

	return true
}

func main() {
	pattern1 := "abba"
	str1 := "dog cat cat dog"
	pattern2 := "abba"
	str2 := "dog cat cat fish"
	pattern3 := "aaaa"
	str3 := "dog cat cat dog"
	pattern4 := "abba"
	str4 := "dog dog dog dog"
	pattern5 := "aba"
	str5 := "cat dog cat"

	println((wordPattern(pattern1, str1)))
	println((wordPattern(pattern2, str2)))
	println((wordPattern(pattern3, str3)))
	println((wordPattern(pattern4, str4)))
	println((wordPattern(pattern5, str5)))


}