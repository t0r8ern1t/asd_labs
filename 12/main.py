# внешняя многофазная сортировка

import random
from itertools import islice


def fill_rand(name):
    f = open(name, 'w')
    for i in range(20):
        f.write(str(random.randint(1, 100)) + '\n')
    f.close()


def merge_sort(nums, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(nums, start, mid)
        merge_sort(nums, mid, end)
        merge_list(nums, start, end)


def merge_list(nums, start, end):
    mid = (start + end) // 2
    left = nums[start:mid]
    right = nums[mid:end]
    k, i, j = start, 0, 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    if start + i < mid:
        while k < end:
            nums[k] = left[i]
            i += 1
            k += 1
    if mid + j < end:
        while k < end:
            nums[k] = right[j]
            j += 1
            k += 1


def multiphase_sort(name):
    f = open(name, 'r')
    i = 0
    for k in range(2):
        arr = []
        for j in range(10):
            arr.append(int(f.readline()))
        merge_sort(arr, 0, len(arr))
        print(arr)
        name = str(k+1) + '.txt'
        f2 = open(name, 'w')
        for j in range(10):
            f2.write(str(arr[j])+'\n')
    f.close()
    f2.close()

    for k in range(2):
        arr = []
        f1 = open('1.txt', 'r')
        f2 = open('2.txt', 'r')
        if k == 1:
            for s in range(5):
                f1.readline()
                f2.readline()
        for j in range(5):
            arr.append(int(f1.readline()))
            arr.append(int(f2.readline()))
        merge_sort(arr, 0, len(arr))
        f = open('output.txt', 'a')
        print(k, arr)
        for j in range(10):
            f.write(str(arr[j])+'\n')


name = 'input.txt'
fill_rand(name)
multiphase_sort(name)