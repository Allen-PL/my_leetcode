# __*__coding:utf-8__*__
# @ModuleName: #101 对称二叉树
# @Function: 
# @Author: pl
# @Time: 2020/11/2 22:39

"""
题目：给定一个二叉树，检查它是否是镜像对称的。


例如，二叉树[1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
"""


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    print(root.left)
    if not root:
        return True
    def dfs(left, right):
        pass

    return dfs(root.left, root.right)



if __name__ == '__main__':
    root = [1, 2,1, 3,3,4,5]
    print(isSymmetric(root))
