#!/usr/bin/env python

import string

expected = ['the', 'and', 'to', 'of', 'i', 'you', 'a', 'my', 'hamlet', 'in']


def clean_data(doc):
    data = [i.strip().lower() for i in doc.split()]
    for i in range(len(data)):
        data[i] = strip_punctuation(data[i])
    return data


def strip_punctuation(word):
    for ch in string.punctuation:
        word = word.replace(ch, '')
    return word


def count_words():
    wc = {}
    document = open('hamlet.txt', 'r').read()
    data = clean_data(document)

    for word in data:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
    top_k = sorted(wc.items(), key=lambda x: x[1], reverse=True)

    return [i[0] for i in top_k[:10]]


if __name__ == '__main__':
    print('Most Frequent Words...')
    answer = count_words()

    print('Answer: %s' % answer)
    assert(answer == expected)
    print('SUCCESS!')
