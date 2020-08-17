from collections import Counter
import operator

def most_frequent(word):
    # c = Counter(word)
    # print(c.most_common())
    # for k,_ in c.most_common():
    #     print(k)
    res = {}
    for c in word:
        res[c] = res.get(c, 0) + 1
    sorted_res = sorted(res.items(), key=lambda item: item[1], reverse=True)
    for k, v in sorted_res:
        print(k, v)

def test_methatiesis_pair(word1, word2):
    return sorted(tuple(word1)) == sorted(tuple(word2))


def find_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.strip().replace("\n", "")
        word_set = tuple(sorted(list(word)))
        anagrams_list = anagrams.get(word_set, [])
        anagrams_list.append(word)
        anagrams[word_set] = anagrams_list
    return anagrams


if __name__ == '__main__':

    most_frequent('ghjhjhhjfgfghgchchnnbnbn')
    print(test_methatiesis_pair("converse", "conserve"))

    with open('words.txt', 'r') as fp:
        words = fp.readlines()
        results = find_anagrams(words)
        for item in results.values():
            print(item)
