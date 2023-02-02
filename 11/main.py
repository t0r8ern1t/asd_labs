# быстрая сортировка

import random

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        randnum = random.choice(nums)
        less = [i for i in nums if i < randnum]
        equal = [i for i in nums if i == randnum]
        bigger = [i for i in nums if i > randnum]
        #print(randnum, less)
        return quick_sort(less) + equal + quick_sort(bigger)


x = int(input("введите размер списка \n"))
nums = [random.randint(1, 100) for i in range(0, x)]
print(*nums)

nums = quick_sort(nums)

print(*nums)

