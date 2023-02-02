#сортировка шелла

from random import randint

x = int(input("введите размер списка \n"))
nums = [randint(1, 100) for i in range(1, x)]
print(*nums)

step = len(nums) // 2
while step > 0:
    for i in range(step, len(nums)):
        tmp = nums[i]
        j = i
        while j >= step and nums[j - step] > tmp:
            nums[j], nums[j - step] = nums[j - step], nums[j]
            j -= step
            #print(*nums)
        nums[j] = tmp
    step //= 2
print(*nums)