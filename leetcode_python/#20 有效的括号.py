# __*__coding:utf-8__*__
# @ModuleName: #20 有效的括号
# @Function: 
# @Author: pl
# @Time: 2020/11/1 22:12
"""
题目：给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。

有效字符串需满足：
- 左括号必须用相同类型的右括号闭合。
- 左括号必须以正确的顺序闭合。
* 注意空字符串可被认为是有效字符串。

"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return False
    default = ['()', '{}', '[]']
    stack = []
    flag = True
    for sign in list(s):
        if not stack or sign in ['(', '{', '[']:
            stack.append(sign)
        else:
            if (stack.pop(-1) + sign) not in default:
                flag = False
                break
    if stack:
        return False
    return flag


if __name__ == '__main__':
    s = ""
    print(isValid(s))