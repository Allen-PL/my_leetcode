# __*__coding:utf-8__*__
# @ModuleName: 算法
# @Function: 
# @Author: pl
# @Time: 2020/11/4 8:58

def binary_search(lst, num):
    left = 0
    right = len(lst) - 1
    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == num:
            return middle
        elif lst[middle] < num:
            left = middle + 1
        else:
            right = middle - 1
    return None


if __name__ == '__main__':
    print(binary_search([1,2,3,4], 1))