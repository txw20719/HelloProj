import socket    #引入套接字
import threading    #引入并行


def getsumss(lists):
    if len(lists) == 1:
        return lists.pop()
    p = lists.pop()
    print(p)
    return p + getsumss(lists)


def count(lists):
    if not lists:
        return 0
    return 1 + count(lists[1:])


def getmax(lists):
    if not lists:
        return 0
    max = lists.pop()
    for x in lists:
        if max < x:
            max = x

    return max


def bisearch(lists, x):
    if not lists:
        return -1
    mid = int(len(lists)/2)
    if lists[mid] == x:
        return mid
    elif lists[mid] > x:
        return bisearch(lists[0:mid], x)
    else:
        return bisearch(lists[mid+1:], x)


lis = [1, 2, 3, 4, 5]
x = input('请输入需要查找的数字：')

print('查找的数在列表中的位置：{0}'.format(bisearch(lis, float(x))))
print('最大数为：{0}'.format(getmax(lis)))
print('长度为：{0}'.format(count(lis)))
print('总和为：{0}'.format(getsumss(lis)))

