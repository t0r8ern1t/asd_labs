#сортировка вставками

from random import randint

x = int(input("введите размер списка \n"))
nums = [randint(1, 100) for i in range(0, x)]
print(*nums)

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        pos = i
        while pos > 0:
            if nums[pos] < nums[pos-1]:
                nums[pos], nums[pos-1] = nums[pos-1], nums[pos]
                pos -= 1
            else:
                break
print(*nums)