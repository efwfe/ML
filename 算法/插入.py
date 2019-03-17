# _*_ coding:utf-8 _*_


def insert(lists):
    lenth = len(lists)
    for j in range(lenth):
        for i in range(j, 0, -1):
            if lists[i] < lists[i - 1]:
                lists[i], lists[i - 1] = lists[i - 1], lists[i]
            else:
                break


if __name__ == '__main__':
    l = [1, 2, 54, 6, 2, 3,3,3]
    insert(l)
    print(l)
