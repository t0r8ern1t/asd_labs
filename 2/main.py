"""
На вход подаётся математическое выражение. Элементы - числа.
Операции - "+ - * /". Также есть скобочки. Окончанием выражения
служит "=". Программа должна вывести результат выражения
"""

priority = {'+': 1,
            '-': 1,
            '*': 2,
            '/': 2}
exep = ['(', ')']


def separate(s):
    arr = []
    elem = ''
    for i in range(len(s)):
        if s[i].isdigit():
            elem += s[i]
        else:
            if elem != '':
                arr.append(elem)
                elem = ''
            arr.append(s[i])
    return arr


def last(arr):
    return arr[len(arr)-1]


def if_empty(arr):
    return len(arr) == 0


def count_two(b, a, sign):
    if sign == '+':
        return a+b
    if sign == '-':
        return a-b
    if sign == '*':
        return a*b
    if sign == '/':
        return a/b


def count(s):
    i = 0
    expression = separate(s)
    numbers = []
    signs = []
    for elem in expression:
        if elem.isdigit():
            numbers.append(int(elem))
        elif elem == '(':
            signs.append(elem)
        elif elem == ')':
            i = len(signs) - 1
            if if_empty(signs):
                print("ошибка в расставлении скобок")
                return False
            while signs[i] != "(":
                #print(numbers, signs, i, signs[i])
                if i == 0 and signs[i] != "(":
                    print("ошибка в расставлении скобок")
                    return False
                res = count_two(numbers.pop(), numbers.pop(), signs.pop())
                numbers.append(res)
                i -= 1
            if last(signs) in exep:
                signs.pop()
            else:
                print("ошибка")
                return False
        elif elem == "=":
            res = count_two(numbers.pop(), numbers.pop(), signs.pop())
            numbers.append(res)
            if if_empty(signs):
                print(last(numbers))
                return True
            else:
                print("ошибка в расставлении знаков операций или скобок")
                return False
        else:
            if if_empty(signs) or last(signs) in exep:
                signs.append(elem)
            elif priority[elem] > priority[last(signs)]:
                signs.append(elem)
            else:
                res = count_two(numbers.pop(), numbers.pop(), signs.pop())
                signs.append(elem)
                numbers.append(res)




s = '(0+9-(8+999))*(678-677)/2='
count(s)

s2 = '(0+9-(8+999))*((678-677)/2='
count(s2)