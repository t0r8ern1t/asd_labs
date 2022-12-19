# Дан текстовый файл с некоторым текстом на русском или английском
# языках произвольной длины (организовать чтение). Выбрав некоторую
# хеш-функцию, создать хеш-таблицу с:
# “со списками”

hashtable = [[[] for j in range(10)] for i in range(100)]
additional = ['.', ',', '!', '?', '...', ';', ':', '(', ')', '"', "'"]


#получаем сумму символов
def get_key(data):
    sum = 0
    for letter in list(data):
        sum += ord(letter)
    return sum


#хэш-функция - целая часть от деления на размер таблицы
def hash_function(data):
    size = 100
    return get_key(data) % size




def find_free(index):
    for i in range(0, 10):
        if not hashtable[index][i]:
            return i
        if i == 9:
            return -1


def add_data(data):
    index = int(hash_function(data))
    #print(index, find_free(index))
    jndex = find_free(index)
    if jndex == -1:
        print("no free slots")
    else:
        hashtable[index][int(jndex)] = [get_key(data), data]


def add_from_file(name):
    f = open(name, 'r')
    text = f.read().split()
    for word in text:
        if word[0] in additional:
            word = word[1:]
        if word[len(word)-1] in additional:
            word = word[:len(word)-1]
        if find_free(hash_function(word)) != -1:
            add_data(word)
        else:
            print("no free slots")
            f.close()
            return
    f.close()


def add_to_file(name):
    f = open(name, 'w')
    for i in range(100):
        s = str(i) + ". "
        for j in range(10):
            if len(hashtable[i][j]) != 0:
                s += " - " + str(hashtable[i][j])
        s += "\n"
        f.write(s)

name = "input.txt"
add_from_file(name)
name = "output.txt"
add_to_file(name)

