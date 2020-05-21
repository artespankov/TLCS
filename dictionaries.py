import random
import string
import time

from lists import in_bisect

def generate_words_file():
    with open('words.txt', 'w') as file:
        for i in range(10000):
            word = ''.join(random.choices(
                string.ascii_uppercase + string.ascii_lowercase + string.digits,
                k=random.randrange(100)))
            word += "\n"
            file.write(word)


def read_file():
    data = {}
    with open('words.txt', 'r') as file:
        for word in file.readlines():
            data[word] = random.sample([1, 2, 3, 17, 55, 20], k=5)
    return data

def read_file_to_list():
    data = []
    with open('words.txt', 'r') as file:
        for word in file.readlines():
            data.append(word)
    return data


def check_in_dict():
    start = time.time()
    data = read_file()
    print("ATGFMkkgf" in data)
    print(time.time() - start)


def check_in_list():
    start = time.time()
    data = read_file_to_list()
    print("ATGFMkkgf" in data)
    print(time.time() - start)

def check_in_list_bisect():
    start = time.time()
    data = read_file_to_list()
    print(in_bisect(data, "ATGFMkkgf"))
    print(time.time() - start)




if __name__ == '__main__':
    check_in_dict()
    check_in_list()
    check_in_list_bisect()