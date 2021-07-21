import random


# 生成随机数
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


# 将序列进行划分，以序列最末值为基准，记为x
def partition(lists, p, r):
    x = lists[r]
    i = p - 1
    # 排序划分，小于x的在前面，大于的在后面
    for j in range(p, r):
        if lists[j] <= x:
            i = i + 1
            lists[i], lists[j] = lists[j], lists[i]
    # x放在中间
    lists[i + 1], lists[r] = lists[r], lists[i + 1]
    return i + 1


# 快速排序，反复调用划分排序函数
def quick_sort(lists, p, r):
    if p < r:
        q = partition(lists, p, r)
        quick_sort(lists, p, q - 1)
        quick_sort(lists, q + 1, r)


if __name__ == "__main__":
    # 随机数生成，生成(1,10000)内的5000个随机数
    lists = list(random_int_list(1, 10000, 5000))
    print("排序前的序列为：")
    for i in lists:
        print(i, end=",")
    print("\n排序后的序列为：")
    quick_sort(lists, 0, len(lists) - 1)
    for i in lists:
        print(i, end=",")
