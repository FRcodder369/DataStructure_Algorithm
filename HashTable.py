
hash_list = {x: [] for x in range(1, 11)}

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

def add(name):
    index = hash_function(name)
    hash_list[index].append(name)

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')


def lookup(name):
    index1 = hash_function(name)
    index2 = hash_list[index1].index(name)
    return index1, index2

add('Stuart')
print(lookup('Stuart'))
print(hash_list)