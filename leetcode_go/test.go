package main

import "fmt"

type tree struct {
	root int
	leftNode *tree
	rightNode *tree
}

func genTree(lst []int) *tree {
	start := 0
	length := len(lst)

	if start >= length {
		return nil
	}
	t := new(tree)
	if length != 0 {
		t.root = lst[start]
		t.leftNode = genTree(lst)
		t.rightNode = genTree(lst)
	} else {
		return nil
	}
	return t


}

func PrintTree(node *tree){
	if node == nil {
		return
	}
	fmt.Println(node.root)
	PrintTree(node.leftNode)
	PrintTree(node.rightNode)
}

func test(root *tree) {

}


func main() {
	lst := []int{1,2,3}

	tree := genTree(lst)
	PrintTree(tree)

	//test(lst)
}