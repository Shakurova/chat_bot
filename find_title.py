# -*- coding: utf-8 -*-

import ujson
import nltk
from nltk.util import ngrams
import editdistance


def find_title(text, movie_names):

    text = text.lower()

    # Generate ngrams
    token = nltk.word_tokenize(text)
    ngrm = []
    for i in range(1, 5):
        for t in ngrams(token, i):
            ngrm.append(t)

    min = ('', 100)
    for ngr in ngrm:

        for title in movie_names:
            # print(title, ' '.join(ngr), editdistance.eval(' '.join(ngr), title))
            if editdistance.eval(' '.join(ngr), title) < min[1] and editdistance.eval(' '.join(ngr), title) < len(title)/3:
                min = (title, editdistance.eval(' '.join(ngr), title))  # the closes movie

    if min[0] != '':
        return min[0]
    else:    # if nothing was found
        return None


if __name__ == '__main__':

    movie_names = open('movie_names.txt', 'r').read().split('\n')
    # movie_db = ujson.load(open('../nice_amazon2_lower.json', 'r'))

    # input = ['Hi! Can you give me a review of Disappeared', 'Hi! Can you give me a review of Diasppeared', 'What was the score of La Bamba?', 'What was the score of Bamba?',
    #          'Can you recommend me something like Full House movie?']

    # for text in input:
    #     print(find_title(text, movie_names, movie_db))