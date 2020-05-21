def read_file():
    results = []
    count_ttl = 0
    fin = open('words.txt', 'r')

    for line in fin.readlines():
        word = line.strip()
        if 'e' in word:
            results.append(word)
        else:
            count_ttl += 1
    fin.close()
    return results, count_ttl


def count_percentage(res, count):
    return count * 100 / len(res)


def avoid(word, forbidden_chars):
    purified = ''
    for char in word:
        if char in forbidden_chars:
            continue
        else:
            purified += char
    return purified


def should_be_avoided(word, forbidden_chars):
    for char in word:
        print(char)
        print(forbidden_chars)
        print()
        if char in forbidden_chars:
            print("Should be")
            return
    print("Shouldn't")
    return

def count_not_containing(forbidden):
    count = 0
    cnt = 0
    fin = open('words.txt', 'r')
    for line in fin.readlines():
        word = line.strip()
        flag = True
        for chr in word:
            if chr in forbidden:
                flag = False
        if flag:
            count += 1
        cnt += 1
    print(cnt, count)
    return count


def uses_all(chr_list):
    cnt = 0
    fin = open('words.txt', 'r')
    for line in fin.readlines():
        word = line.strip()
        use_all = True
        for chr in chr_list:
            if chr not in word:
                use_all = False
        if use_all:
            cnt += 1
            print(word)
    print(cnt)

def is_abecedarian():
    fin = open('words.txt', 'r')
    cnt = 0
    for line in fin.readlines():
        word = line.strip()
        flag = True
        for i in range(1, len(word)):
            if word[i] < word[i-1]:
                flag = False
        if flag:
            print(word)
            cnt += 1
    print(cnt)


def check_tree_characters(word):

    if len(word) <=2:
        return False
    if word[2] == word[0] and word[1] == word[0]:
        print(word)
        return True
    else:
        return check_tree_characters(word[2:])


def has_tree_characters():
    fin = open('words.txt', 'r')
    for line in fin.readlines():
        word = line.strip()
        check_tree_characters(word)


def is_triple_double(word):
    cnt = 0
    i = 1
    while i < len(word):
        if word[i] == word[i-1]:
            cnt += 1
            i += 2
            if cnt == 3:
                return True
        else:
            cnt = 0
            i += 1
    return None


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


def is_palindrome(string):
    return string[::-1] == string


def find_solution():
    for j in range(100000, 1000000):
        i = j
        string = str(i)
        first_check = string[(len(string)-4):]
        if is_palindrome(first_check):
            i+=1
            string = str(i)
            second_check = string[(len(string) - 5):]
            if is_palindrome(second_check):
                i+=1
                string = str(i)
                third_check = string[1:-1]
                if is_palindrome(third_check):
                    i+=1
                    string=str(i)
                    if is_palindrome(string):
                        print(j)
                        print(i)



def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.

    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start + length]
    return s[::-1] == s


def check(i):
    """Checks if the integer (i) has the desired properties.

    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i + 1, 1, 5) and
            has_palindrome(i + 2, 1, 4) and
            has_palindrome(i + 3, 0, 6))


def check_all():
    """Enumerate the six-digit numbers and print any winners.
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


def find_age():
    for i in range(11, 99):
        for j in range(99, 11):
            if str(i) == str(j):
                print(i, j)






if __name__ == '__main__':
    # find_solution()
    # check_all()
    find_age()
