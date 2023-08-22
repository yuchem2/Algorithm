# baekjoon Problem1920
# input: sequence of number
# output: Is x in the sequence?
# 05-31-2023

import sys


def find(num, array, l, r):
    while l < r:
        mid = (l+r)//2
        if num == array[mid]:
            return 1
        elif num < array[mid]:
            r = mid
        else:
            l = mid + 1
    return 0


def problem1920():
    n = int(input())
    num_list = list(map(int, input().split()))
    m = int(input())
    problem = list(map(int, input().split()))

    num_list.sort()
    for i in range(m):
        sys.stdout.write(str(find(problem[i], num_list, 0, n))+"\n")


if __name__ == '__main__':
    problem1920()
