# пирамидальная сортировка

from random import randint


def make_heap(nums, length, index):
    maxindex = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and nums[maxindex] < nums[left]:
        maxindex = left

    if right < length and nums[maxindex] < nums[right]:
        maxindex = right

    if maxindex != index:
        nums[index], nums[maxindex] = nums[maxindex], nums[index]
        make_heap(nums, length, maxindex)
    #print(*nums)


def heap_sort(nums):
    length = len(nums)

    for i in range(length, -1, -1):
        make_heap(nums, length, i)

    for i in range(length-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        make_heap(nums, i, 0)


x = int(input("введите размер списка \n"))
nums = [randint(1, 100) for i in range(0, x)]
print(*nums)

heap_sort(nums)

print(*nums)