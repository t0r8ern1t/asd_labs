#поразрядная сортировка

from random import randint
import math

x = int(input("введите размер списка \n"))
nums = [randint(10, 10000) for i in range(0, x)]
print(*nums)

digits = int(math.log10(max(nums))) + 1
rang = 10

for i in range(digits):
    lists = [[] for k in range(rang)]
    for num in nums:
        tmp = int((num // 10**i) % 10)
        lists[tmp].append(num)
    nums = []
    for j in range(rang):
        nums += lists[j]
    #print(nums)
print(*nums)
