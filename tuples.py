

def find_anagrams(wrds):
    anagrams = {}
    for word in wrds:
        word = word.strip().replace("\n", "")
        word_set = tuple(sorted(list(word)))
        anagrams_list = anagrams.get(word_set, [])
        anagrams_list.append(word)
        anagrams[word_set] = anagrams_list
    return anagrams


if __name__ == '__main__':
    with open('words.txt', 'r') as fp:
        words = fp.readlines()
        results = find_anagrams(words)
        for item in results.values():
            print(item)

