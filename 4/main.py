#сортировка методом прочесывания

from random import randint

x = int(input("введите размер списка \n"))
nums = [randint(1, 100) for i in range(0, x)]
print(*nums)

step = len(nums) - 1

while step != 0:
    for i in range(len(nums) - step):
        if nums[i] > nums[i+step]:
            nums[i], nums[i+step] = nums[i+step], nums[i]
    step -= 1

print(*nums)