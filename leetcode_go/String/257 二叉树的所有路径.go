package main

import (
	"fmt"
	"reflect"
)

/**
题目大意：给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
叶子节点 是指没有子节点的节点。

解题思路：
*/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}


func genTree(lst []int) *TreeNode {

	t := new(TreeNode)
	for i := 0; i < len(lst); i++  {
		element := lst[i]
		if reflect.TypeOf(element) != nil {
			t.Val = element
			t.Left = genTree(lst)
			t.Right = genTree(lst)
		}
	}
	return t

}

func PrintTree(node *TreeNode){
	if node == nil {
		return
	}
	fmt.Println(node.Val)
	PrintTree(node.Left)
	PrintTree(node.Right)
}

//func binaryTreePaths(root *TreeNode) []string {
//
//}

func main() {

	root := []int{1, 2, 3, nil, 5}

	tree := genTree(root)
	PrintTree(tree)

	//println(binaryTreePaths(*tree))
}





