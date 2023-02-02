#сортировка посредством выбора

from random import randint

x = int(input("введите размер списка \n"))
nums = [randint(1, 100) for i in range(0, x)]
print(*nums)

min = 2**31 + 1

for i in range(len(nums)):
    m, pos = min, 0
    for j in range(i, len(nums)):
        if nums[j] < m:
            m = nums[j]
            pos = j
    nums[pos], nums[i] = nums[i], nums[pos]
print(*nums)