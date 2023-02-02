"""
На вход подаётся строка, состоящая из скобок. Программа должна определить
правильность введённого скобочного выражения. Савкин сказал, что
программа должна работать на русском языке: "Введите строку",
"Строка не существует", "Строка существует" и т.п.
"""

while True:
    hello = input("Введите строку: \n")
    s = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    storage = []
    count = -1
    res = True

    for char in hello:
        if char in s.values():
            storage.append(char)
            count += 1
        else:
            if count == -1:
                res = False
                break
            count -= 1
            if storage.pop() != s[char]:
                res = False
                break

    if res and count == -1:
        print("Правильная скобочная последовательность")
    else:
        print("Неправильная скобочная последовательность")
    break
