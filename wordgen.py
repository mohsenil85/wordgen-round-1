# vim: tabstop=9 expandtab shiftwidth=4 softtabstop=4
# python 3??

from collections import defaultdict
import random

dictionary = defaultdict(list)

wordlist = "/usr/share/dict/cracklib-small"

def get_words():
    for line in open(wordlist):
        line += '@@'

        word_to_dict(dictionary, line)


def word_to_dict(dictionary, word):
    d = dictionary
    t = word
    for i in range(len(t) - 2):
        k = t[i] + t[i+1]
        v = t[i+2]
        if d.__contains__(k):
            d[k].append(v)
        else:
            d[k] = list(v)
def create_letter(dictionary):
    d = dictionary
    seed = random.choice(list(d.keys()))
    #print("seed =" + seed)
    letter = random.choice(d.get(seed))
    if letter == '@' or letter == '\n' or letter == '\'':
        return '%'
    else:
        return letter

def create_word(length):
    word = ""
    while len(word) < length:
        letter =  create_letter(dictionary)
        if letter != '%':
            word += letter
    return word



if __name__ == "__main__":
    get_words()
    print("word(3) = " + create_word(3))
    print("word(4) = " + create_word(4))
    print("word(8) = " + create_word(8))

