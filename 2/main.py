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

#функция из лабораторной №1, проверяет правильность расставления скобок
def check_parenthesis(arr):
    while True:
        hello = arr
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
            return True
        else:
            return False

#разделяем строку на список элементов и преобразовываем числа в int
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

#возвращает последнее значение списка
def last(arr):
    return arr[len(arr)-1]

#смотрим пустой ли список
def if_empty(arr):
    return len(arr) == 0

#арифметические операции
def count_two(b, a, sign):
    if sign == '+':
        return a+b
    if sign == '-':
        return a-b
    if sign == '*':
        return a*b
    if sign == '/':
        return a/b

#основная функция подсчета
def count(s):
    i = 0
    expression = separate(s)
    numbers = []
    signs = []
    parenthesis = []

    #каждый элемент списка кладем либо в список чисел, либо в список символов
    #отдельный список скобок для проверки, скобки также дублируются в signs
    for elem in expression:
        if elem.isdigit():
            numbers.append(int(elem))
        elif elem == '(':
            signs.append(elem)
            parenthesis.append(elem)

            #если встречается закрывающаяся скобка, выполняем все действия до ближайшей открывающей
            #выводит ошибку, если скобки стоят криво (см. второй пример)
        elif elem == ')':
            parenthesis.append(elem)
            i = len(signs) - 1
            while signs[i] != '(':
                res = count_two(numbers.pop(), numbers.pop(), signs.pop())
                numbers.append(res)
                i -= 1
                if i == 0 and signs[i] != '(':
                    print("ошибка в расставлении скобок")
                    return False
            signs.pop()

            #встречаем - подсчитываем последнее значение независимо от приоритета и выводим ответ
        elif elem == "=":
            res = count_two(numbers.pop(), numbers.pop(), signs.pop())
            numbers.append(res)
            if not check_parenthesis(parenthesis):
                print("ошибка в расставлении скобок(")
                return False
            if if_empty(signs):
                print(last(numbers))
                return True
            else:
                print("ошибка в расставлении знаков операций")
                return False
        else:
            if if_empty(signs):
                signs.append(elem)
            elif last(signs) in exep:
                signs.append(elem)
            #если приоритет нового действия больше - закидываем символ в список символов и идем дальше
            elif priority[elem] > priority[last(signs)]:
                signs.append(elem)
            #если приоритет меньше, то считаем предыдущее действие, заменяем последные два числа в numbers промежуточным значением
            #и записываем в signs новую операцию не выполняя ее
            else:
                res = count_two(numbers.pop(), numbers.pop(), signs.pop())
                signs.append(elem)
                numbers.append(res)




s = '(0+9-(8+999))*(678-677)/2='
count(s)
#print(count(s))

s2 = '(0+9-((8+999))*(678-677)/2='
count(s2)
#print(count(s2))