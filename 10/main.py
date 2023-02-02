# сортировка слиянием

from random import randint


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


x = int(input("введите размер списка \n"))
nums = [randint(1, 100) for i in range(0, x)]
print(*nums)

merge_sort(nums, 0, len(nums))

print(*nums)