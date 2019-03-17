# _*_ coding:utf-8 _*_


def bubble_sort(lists):
    # 计算列表的长度
    n = len(lists)
    for j in range(n-1):
        count = 0
        # 用count记录已经完好的次数
        for i in range(0, n-1-j):
            if lists[i] > lists[i+1]:
                lists[i], lists[i+1] = lists[i+1], lists[i]

            count += 1

        if count == 0:
            break


if __name__ == '__main__':
    alist = [54, 26, 111,93, 77, 44, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    bubble_sort(alist)
    print("新列表为：%s" % alist)
