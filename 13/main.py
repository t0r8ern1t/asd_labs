# Дан текстовый файл с некоторым текстом на русском или английском
# языках произвольной длины (организовать чтение). Выбрав некоторую
# хеш-функцию, создать хеш-таблицу с:
# “с наложением”

hashtable = [[] for i in range(100)]
additional = ['.', ',', '!', '?', '...', ';', ':', '(', ')', '"', "'"]


def get_key(data):
    sum = 0
    for letter in list(data):
        sum += ord(letter)
    return sum


def hash_function(data):
    size = 100
    return get_key(data) % size


def find_free(index):
    for i in range(0, 100):
        if not hashtable[i]:
            return i
        if i == 99:
            return -1


def add_data(data):
    index = hash_function(data)
    # print(index, hashtable[index])
    if len(hashtable[index]) != 0:
        index = find_free(index)
        if index == -1:
            return
        else:
            # print(data, index)
            hashtable[int(index)] = [get_key(data), data]
    else:
        hashtable[index] = [get_key(data), data]


def add_from_file(name):
    f = open(name, 'r')
    text = f.read().split()
    for word in text:
        if word[0] in additional:
            word = word[1:]
        if word[len(word)-1] in additional:
            word = word[:len(word)-1]
        if find_free(0) != -1:
            add_data(word)
        else:
            print("no free slots")
            f.close()
            return
    f.close()


def add_to_file(name):
    f = open(name, 'w')
    for i in range(100):
        if len(hashtable[i]) != -1:
            s = str(i) + ". " + str(hashtable[i][0]) + " - " + str(hashtable[i][1]) + "\n"
            f.write(s)

name = "input.txt"
add_from_file(name)
name = "output.txt"
add_to_file(name)


