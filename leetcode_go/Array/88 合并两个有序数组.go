package main

/**
题目：给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

解题思路：为了尽量少的移动数组中的数据，将nums1中的最大数据和nums2中的最大数据进行比较，较大的就放在nums1的最后面，不要忘记了nums2中可能还有更小的数据，所以在遍历完nums2将其加入nums1
*/

func merge(nums1 []int, m int, nums2 []int, n int) {
	for p := m + n; m > 0 && n > 0; p-- {
		if nums1[m-1] <= nums2[n-1] {
			nums1[p-1] = nums2[n-1]
			n--
		} else {
			nums1[p-1] = nums1[m-1]
			m--
		}
	}
	for ; n > 0; n-- {
		nums1[n-1] = nums2[n-1]
	}
}


func main() {
	nums1 := []int{1, 2, 3, 4, 0, 0, 0, 0}
	nums2 := []int{1, 2, 3, 4}
	m := 4
	n := 4
	merge(nums1, m, nums2, n)
}
